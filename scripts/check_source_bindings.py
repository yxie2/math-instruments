"""Check pinned source bytes and label locations against a supplied source tree."""
from hashlib import sha256
from pathlib import Path
import argparse
import json
import os
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    args = parser.parse_args()
    source_root = args.source_root.resolve()
    if os.name == 'nt' and not str(source_root).startswith('\\\\?\\'):
        source_root = Path('\\\\?\\' + str(source_root))
    files = {}
    bindings = 0
    manifests = sorted((ROOT / 'sources' / 'batches').glob('B*.json'))
    for path in manifests:
        manifest = json.loads(path.read_text(encoding='utf-8'))
        for entry in manifest['files']:
            source = source_root / entry['path']
            digest = sha256(source.read_bytes()).hexdigest()
            if digest != entry['sha256']:
                raise ValueError(f"Source hash mismatch: {entry['path']}")
            if entry['path'] in files and files[entry['path']] != digest:
                raise ValueError(f"Conflicting source versions: {entry['path']}")
            files[entry['path']] = digest
        for locator in manifest['instrument_locators']:
            lines = (source_root / locator['path']).read_text(encoding='utf-8').splitlines()
            label_pattern = r'\\label(?:\[[^\]]+\])?\{' + re.escape(locator['label']) + r'\}'
            if not 1 <= locator['line'] <= len(lines) or not re.search(label_pattern, lines[locator['line'] - 1]):
                raise ValueError(f"Source label mismatch: {locator['instrument_id']} {locator['label']}")
            bindings += 1
    print(json.dumps({'status': 'passed', 'manifests': len(manifests),
                      'unique_source_files': len(files), 'label_bindings': bindings,
                      'scope': 'Byte and location audit only; no mathematical proof verification.'}, indent=2))


if __name__ == '__main__':
    main()
