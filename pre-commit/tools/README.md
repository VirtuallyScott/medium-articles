# Pre-commit Tools

This directory contains linting and validation tools for enforcing organizational standards.

## Files

### Configuration
- **`approved-verbs.yml`** - Source of truth for approved verbs used in verb-noun naming conventions

### Shell Script Tools
- **`validate-shell.sh`** - Runs ShellCheck on all shell scripts
- **`validate-shell-naming.py`** - Validates shell script naming conventions

### Python Script Tools
- **`validate-python.sh`** - Runs Python linters (flake8, pylint, or ruff)
- **`validate-python-naming.py`** - Validates Python script naming conventions

### Ansible Tools
- **`validate-ansible.sh`** - Runs ansible-lint on Ansible playbooks
- **`lint-rules/`** - Custom ansible-lint rules directory

---

## Naming Conventions

All scripts (shell, Python, and Ansible) must follow the **verb-noun** naming pattern with approved verbs.

### Approved Verbs

See [`approved-verbs.yml`](approved-verbs.yml) for the source of truth.

Current approved verbs (alphabetized):
- apply, audit, bootstrap, build, cleanup, configure, create, deploy, destroy
- disable, enable, harden, initialize, install, migrate, promote, publish
- register, remove, rotate, sync, test, update, upgrade, validate, verify

**Verbs to avoid:** do, fix, misc, run, stuff, temp

---

## Shell Scripts

### Requirements
- Must follow `verb-noun.sh` pattern
- Use lowercase only
- Use hyphens as separators (not underscores)
- Start with an approved verb
- Must have `.sh` extension

### Valid Examples
```bash
✓ build-image.sh
✓ deploy-application.sh
✓ configure-network.sh
✓ validate-release.sh
✓ rotate-secrets.sh
```

### Invalid Examples
```bash
✗ run-stuff.sh           # 'run' is not an approved verb
✗ BuildImage.sh          # Not lowercase
✗ deploy_app.sh          # Uses underscores instead of hyphens
✗ main.sh                # Doesn't follow verb-noun pattern
✗ do-things.sh           # 'do' is not an approved verb
```

### Manual Validation

Check naming convention:
```bash
python3 tools/validate-shell-naming.py path/to/script.sh
```

Run ShellCheck:
```bash
bash tools/validate-shell.sh
```

---

## Python Scripts

### Requirements
- Must follow `verb-noun.py` pattern
- Use lowercase only
- Use hyphens as separators (not underscores)
- Start with an approved verb
- Must have `.py` extension

**Exceptions:** The following files are automatically skipped from naming validation:
- `__init__.py`, `__main__.py` - Python package files
- `setup.py`, `conftest.py`, `manage.py` - Configuration files
- `test_*.py`, `*_test.py` - Test files
- Files in `venv/`, `.venv/`, `build/`, `dist/` directories

### Valid Examples
```python
✓ build-package.py
✓ deploy-service.py
✓ validate-config.py
✓ migrate-database.py
✓ create-user.py
```

### Invalid Examples
```python
✗ run-stuff.py           # 'run' is not an approved verb
✗ BuildPackage.py        # Not lowercase
✗ deploy_app.py          # Uses underscores instead of hyphens
✗ main.py                # Doesn't follow verb-noun pattern
✗ do-things.py           # 'do' is not an approved verb
```

### Manual Validation

Check naming convention:
```bash
python3 tools/validate-python-naming.py path/to/script.py
```

Run Python linters:
```bash
bash tools/validate-python.sh
```

---

## Ansible Playbooks

### Requirements
- Must follow `verb-noun.yml` pattern
- Use lowercase only
- Use hyphens as separators (not underscores)
- Start with an approved verb
- Must have `.yml` or `.yaml` extension

### Valid Examples
```yaml
✓ build-image.yml
✓ deploy-application.yml
✓ configure-network.yml
✓ validate-release.yml
✓ rotate-secrets.yml
```

### Invalid Examples
```yaml
✗ run-stuff.yml          # 'run' is not an approved verb
✗ BuildImage.yml         # Not lowercase
✗ deploy_app.yml         # Uses underscores instead of hyphens
✗ main.yml               # Doesn't follow verb-noun pattern
✗ do-things.yml          # 'do' is not an approved verb
```

### Manual Validation

Run ansible-lint:
```bash
ansible-lint ansible/
```

Or use the helper script:
```bash
bash tools/validate-ansible.sh
```

---

## Pre-commit Integration

All checks are integrated with pre-commit. Install pre-commit hooks:

```bash
pre-commit install
```

Run all checks:
```bash
pre-commit run --all-files
```

Run specific checks:
```bash
# Shell scripts
pre-commit run shellcheck --all-files
pre-commit run shell-naming --all-files

# Python scripts
pre-commit run python-lint --all-files
pre-commit run python-naming --all-files

# Ansible
pre-commit run ansible-lint --all-files
```

---

## Adding New Approved Verbs

1. Edit `tools/approved-verbs.yml`
2. Add the new verb in alphabetical order under `approved_verbs:`
3. Optionally add deprecated verbs to `avoid_verbs:` for documentation
4. All validators will automatically pick up the change

Example:
```yaml
approved_verbs:
  - apply
  - backup  # <-- New verb added
  - bootstrap
  # ... rest of verbs
```

---

## Installation

### Required Tools

**For Shell Scripts:**
```bash
# macOS
brew install shellcheck

# Linux
apt-get install shellcheck  # Debian/Ubuntu
yum install shellcheck      # RHEL/CentOS
```

**For Python:**
```bash
# Choose one or more linters
pip install flake8
pip install pylint
pip install ruff
# or
brew install ruff
```

**For Ansible:**
```bash
pip install ansible-lint ansible-core
# or
brew install ansible-lint
```

**For Pre-commit:**
```bash
pip install pre-commit
# or
brew install pre-commit
```

### Python Dependencies

The naming validators require PyYAML:
```bash
pip install pyyaml
```

---

## Philosophy

This naming convention follows the **PowerShell verb-noun discipline**, which:
- Improves discoverability
- Makes intent clear from the filename
- Enables autocomplete-friendly organization
- Maintains consistency across teams
- Prevents vague names like "run-stuff" or "misc-things"

By enforcing approved verbs, we ensure:
- **Clarity**: Scripts have specific, well-defined purposes
- **Consistency**: Similar actions use similar verbs across the codebase
- **Maintainability**: New team members can quickly understand what scripts do
- **Quality**: Avoiding vague verbs forces better design decisions
