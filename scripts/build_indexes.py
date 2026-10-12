"""Regenerate Markdown tables and JSON/CSV exports."""
import argparse
from catalog import build

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true',help='Fail if committed outputs are stale.')
    args=parser.parse_args()
    total,changed=build(check=args.check)
    print(f'{total} generated views checked; {len(changed)} updated.' if not args.check else f'{total} generated views are current.')
