#!/usr/bin/env python3
"""
Python Script Naming Convention Validator
Enforces verb-noun.py naming pattern with approved verbs
"""

import re
import sys
import yaml
from pathlib import Path
from typing import List, Set, Tuple


def load_approved_verbs() -> Set[str]:
    """Load approved verbs from YAML configuration file."""
    verbs_file = Path(__file__).parent / "approved-verbs.yml"
    
    try:
        with open(verbs_file, 'r') as f:
            data = yaml.safe_load(f)
            return set(data.get('approved_verbs', []))
    except Exception as e:
        print(f"Warning: Could not load verbs file: {e}", file=sys.stderr)
        # Fallback to hardcoded verbs if file cannot be loaded
        return {
            "apply", "audit", "bootstrap", "build", "cleanup",
            "configure", "create", "deploy", "destroy", "disable",
            "enable", "harden", "initialize", "install", "migrate",
            "promote", "publish", "register", "remove", "rotate",
            "sync", "test", "update", "upgrade", "validate", "verify"
        }


def should_skip(filepath: Path) -> bool:
    """
    Determine if a Python file should be skipped from naming validation.
    
    Skips:
    - __init__.py files
    - Test files (test_*.py, *_test.py)
    - Setup/config files (setup.py, conftest.py, etc.)
    - Files in virtual environments or build directories
    """
    filename = filepath.name
    parts = filepath.parts
    
    # Skip special Python files
    if filename in ['__init__.py', '__main__.py', 'setup.py', 'conftest.py', 
                    'manage.py', 'wsgi.py', 'asgi.py']:
        return True
    
    # Skip test files (common patterns)
    if filename.startswith('test_') or filename.endswith('_test.py'):
        return True
    
    # Skip files in common directories to ignore
    skip_dirs = {'venv', 'env', '.venv', 'node_modules', 'build', 'dist', 
                 '.tox', '__pycache__', '.pytest_cache', 'site-packages'}
    if any(skip_dir in parts for skip_dir in skip_dirs):
        return True
    
    return False


def check_filename(filename: str, approved_verbs: Set[str]) -> Tuple[bool, List[str]]:
    """
    Check if filename follows naming convention.
    
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    # Must match lowercase hyphen-separated pattern ending in .py
    if not re.match(r"^[a-z0-9]+-[a-z0-9-]+\.py$", filename):
        errors.append(
            f"'{filename}' does not match verb-noun.py pattern (lowercase, hyphen-separated)"
        )
        return False, errors

    # Extract verb (first part before hyphen)
    verb = filename.split("-")[0]
    
    # Check if verb is approved
    if verb not in approved_verbs:
        errors.append(
            f"'{filename}' uses unapproved verb '{verb}'. "
            f"See tools/approved-verbs.yml for approved verbs."
        )
        return False, errors
    
    return True, []


def main():
    """Main entry point."""
    approved_verbs = load_approved_verbs()
    
    if len(sys.argv) < 2:
        print("Usage: validate-python-naming.py <file1.py> [file2.py ...]")
        sys.exit(1)
    
    files_to_check = sys.argv[1:]
    all_valid = True
    skipped_count = 0
    
    for filepath in files_to_check:
        path = Path(filepath)
        
        # Skip non-.py files
        if path.suffix != ".py":
            continue
        
        # Skip special files
        if should_skip(path):
            skipped_count += 1
            continue
            
        filename = path.name
        is_valid, errors = check_filename(filename, approved_verbs)
        
        if not is_valid:
            all_valid = False
            print(f"\n❌ {filepath}")
            for error in errors:
                print(f"   {error}")
    
    if all_valid:
        if skipped_count > 0:
            print(f"✓ All Python scripts follow naming convention ({skipped_count} file(s) skipped)")
        else:
            print("✓ All Python scripts follow naming convention")
        sys.exit(0)
    else:
        print("\n❌ Some Python scripts do not follow naming convention")
        print(f"\nApproved verbs: {', '.join(sorted(approved_verbs))}")
        print("\nNaming pattern: verb-noun.py")
        print("Examples: build-package.py, deploy-service.py, validate-config.py")
        print("\nNote: __init__.py, setup.py, test files, and other special files are skipped")
        sys.exit(1)


if __name__ == "__main__":
    main()
