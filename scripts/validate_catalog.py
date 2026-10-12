"""Check record relationships, links, provenance and generated outputs."""
import json
from catalog import validate

if __name__=='__main__':
    print(json.dumps({'validation':'passed','counts':validate()},indent=2))
