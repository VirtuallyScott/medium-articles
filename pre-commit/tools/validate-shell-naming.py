#!/usr/bin/env python3
"""
Shell Script Naming Convention Validator
Enforces verb-noun.sh naming pattern with approved verbs
"""

import re
import sys
from pathlib import Path
from typing import List, Set, Tuple

import yaml


def load_approved_verbs() -> Set[str]:
    """Load approved verbs from YAML configuration file."""
    verbs_file = Path(__file__).parent / "approved-verbs.yml"

    try:
        with open(verbs_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return set(data.get('approved_verbs', []))
    except Exception:
        print(f"Warning: Could not load verbs file: {verbs_file}", file=sys.stderr)
        # Fallback to hardcoded verbs if file cannot be loaded
        return {
            "apply", "audit", "bootstrap", "build", "cleanup",
            "configure", "create", "deploy", "destroy", "disable",
            "enable", "harden", "initialize", "install", "migrate",
            "promote", "publish", "register", "remove", "rotate",
            "sync", "test", "update", "upgrade", "validate", "verify"
        }


def check_filename(filename: str, approved_verbs: Set[str]) -> Tuple[bool, List[str]]:
    """
    Check if filename follows naming convention.

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    # Must match lowercase hyphen-separated pattern ending in .sh
    if not re.match(r"^[a-z0-9]+-[a-z0-9-]+\.sh$", filename):
        errors.append(
            f"'{filename}' does not match verb-noun.sh pattern (lowercase, hyphen-separated)"
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
        print("Usage: check-shell-naming.py <file1.sh> [file2.sh ...]")
        sys.exit(1)

    files_to_check = sys.argv[1:]
    all_valid = True

    for filepath in files_to_check:
        path = Path(filepath)

        # Skip non-.sh files
        if path.suffix != ".sh":
            continue

        filename = path.name
        is_valid, errors = check_filename(filename, approved_verbs)

        if not is_valid:
            all_valid = False
            print(f"\n❌ {filepath}")
            for error in errors:
                print(f"   {error}")

    if all_valid:
        print("✓ All shell scripts follow naming convention")
        sys.exit(0)
    else:
        print("\n❌ Some shell scripts do not follow naming convention")
        print(f"\nApproved verbs: {', '.join(sorted(approved_verbs))}")
        print("\nNaming pattern: verb-noun.sh")
        print("Examples: build-image.sh, deploy-application.sh, configure-network.sh")
        sys.exit(1)


if __name__ == "__main__":
    main()
