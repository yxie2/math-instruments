"""Run finite batch checks from copies without replacing recorded results."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='A new directory for copied programs, data and results')
    parser.add_argument('--jobs', type=int, default=4)
    parser.add_argument('--timeout', type=float, default=600,
                        help='Maximum seconds per batch')
    args = parser.parse_args()
    if args.jobs < 1 or args.timeout <= 0:
        parser.error('jobs and timeout must be positive')
    output = args.output.resolve()
    if output.exists():
        parser.error('Output already exists; choose a new directory to preserve earlier results')
    output.mkdir(parents=True)
    scripts = sorted((ROOT / 'batches').glob('B*/verification/check_instruments.py'))

    def run(script):
        batch = script.parents[1].name
        destination = output / batch
        shutil.copytree(script.parent, destination)
        started = time.monotonic()
        result = {'batch': batch,
                  'program_sha256': sha256(script.read_bytes()).hexdigest()}
        try:
            process = subprocess.run(
                [sys.executable, '-X', 'utf8', str(destination / script.name)],
                cwd=ROOT, capture_output=True, text=True, encoding='utf-8',
                timeout=args.timeout)
            result['exit_code'] = process.returncode
            (destination / 'execution.txt').write_text(
                process.stdout + process.stderr, encoding='utf-8')
        except subprocess.TimeoutExpired:
            result.update(exit_code=None, error='Per-batch timeout exceeded')
        result['seconds'] = round(time.monotonic() - started, 3)
        print(f"{batch}: {'passed' if result['exit_code'] == 0 else 'FAILED'}", flush=True)
        return result

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(run, script) for script in scripts]
        results = [future.result() for future in as_completed(futures)]
    summary = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Finite programs only; no source headline theorem or Lean proof certified.',
        'python': sys.version.split()[0],
        'batches': sorted(results, key=lambda result: result['batch']),
        'passed': bool(results) and all(result['exit_code'] == 0 for result in results),
    }
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    return 0 if summary['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
