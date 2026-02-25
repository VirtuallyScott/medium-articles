# Naming Standard for Scripts and Automation
Inspired by PowerShell's verb-noun discipline

---

# Purpose

Establish a consistent, predictable naming convention for:

- **Shell scripts** (*.sh)
- **Python scripts** (*.py)
- **Ansible playbooks** (*.yml)
- **Ansible roles**
- Major automation entry points

Goals:

- Improve readability
- Reduce review friction
- Encourage architectural clarity
- Make intent obvious from filenames
- Avoid naming debates in MRs

This document is a living standard and may evolve over time.

---

# 1. Shell Script Naming Convention

## Format: verb-noun.sh

Shell scripts perform actions. They should start with an approved verb and describe the primary target or outcome.

Examples:

- `build-image.sh`
- `deploy-application.sh`
- `validate-config.sh`
- `configure-network.sh`
- `cleanup-logs.sh`
- `sync-repository.sh`
- `rotate-credentials.sh`
- `bootstrap-environment.sh`
- `test-connectivity.sh`
- `migrate-database.sh`

### Rules

- Lowercase only
- Hyphen-separated
- Single responsibility per script
- No generic names like `run.sh`, `main.sh`, `script.sh`
- Must start with an approved verb (see section 5)

---

# 2. Python Script Naming Convention

## Format: verb-noun.py

Python scripts perform actions. They should start with an approved verb and describe the primary target or outcome.

Examples:

- `build-package.py`
- `deploy-service.py`
- `validate-release.py`
- `configure-settings.py`
- `cleanup-cache.py`
- `sync-data.py`
- `create-user.py`
- `migrate-schema.py`
- `test-endpoints.py`
- `update-inventory.py`

### Rules

- Lowercase only
- Hyphen-separated
- Single responsibility per script
- No generic names like `run.py`, `main.py`, `script.py`
- Must start with an approved verb (see section 5)

### Exceptions (Automatically Skipped)

The following Python files are exempt from the naming convention:
- `__init__.py`, `__main__.py` - Python package files
- `setup.py`, `conftest.py`, `manage.py` - Configuration/framework files
- `test_*.py`, `*_test.py` - Test files following pytest/unittest conventions
- Files in virtual environments (`venv/`, `.venv/`, `env/`)
- Build artifacts (`build/`, `dist/`, `__pycache__/`)

---

# 3. Ansible Playbook Naming Convention

## Format: verb-noun.yml

Playbooks orchestrate actions. Therefore, they should start with an approved verb and describe the primary target or outcome.

Examples:

- `build-image.yml`
- `publish-vhd.yml`
- `apply-stig.yml`
- `validate-release.yml`
- `rotate-secrets.yml`
- `bootstrap-host.yml`
- `configure-network.yml`
- `deploy-agent.yml`
- `cleanup-artifacts.yml`
- `sync-repository.yml`

### Rules

- Lowercase only
- Hyphen-separated
- Single responsibility per playbook
- No generic names like `run.yml`, `main.yml`, `test.yml`

---

# 4. Ansible Role Naming Convention

## Format: lowercase_with_underscores

Roles represent reusable capabilities, not actions.

Examples:

- `image_build`
- `azure_publish`
- `stig_hardening`
- `fips_kernel`
- `vault_auth`
- `package_install`
- `system_configuration`
- `release_validation`

### Rules

- Lowercase
- Underscores only
- No hyphens
- Noun or capability oriented
- Stable names (roles become internal APIs)

Why underscores?

- Required for collection compatibility
- Aligns with Ansible-lint expectations
- Matches Python identifier rules

---

# 5. Approved Verb List (All Scripts)

Use clear, intentional verbs for all scripts (shell, Python, and Ansible playbooks). Avoid vague ones.

**Source of truth:** `tools/approved-verbs.yml`

### Core Verbs

- build
- publish
- apply
- configure
- deploy
- install
- validate
- test
- rotate
- create
- destroy
- remove
- cleanup
- bootstrap
- initialize
- migrate
- sync
- update
- upgrade
- enable
- disable
- harden
- audit
- verify
- register
- promote

### Avoid

- run
- do
- fix
- stuff
- misc
- temp

If a new verb is needed, propose and document it.

---

# 6. Approved Noun Examples

Nouns should reflect infrastructure objects, outcomes, or domains.

### Infrastructure

- image
- vhd
- ami
- vm
- host
- network
- firewall
- repository
- artifact
- package
- kernel
- service
- container
- cluster

### Security

- stig
- fips
- secrets
- credentials
- policy
- compliance
- baseline
- audit

### Process / Lifecycle

- release
- build
- validation
- registration
- bootstrap
- deployment
- promotion

Combine clearly:

- build-image
- publish-vhd
- apply-stig
- validate-release
- register-image
- rotate-secrets

---

# 7. Design Philosophy

**Scripts (Shell/Python/Playbooks) = Actions**  
**Roles = Capabilities**  

If it sounds like something you *do*, it is a script.

If it sounds like something you *have* or *provide*, it is probably a role.

Examples:

**Shell Script:**
`deploy-application.sh`

**Python Script:**
`validate-config.py`

**Ansible Playbook:**
`apply-stig.yml`

**Ansible Role:**
`stig_hardening`

---

## Cross-Language Consistency

When the same operation exists in multiple languages, use the same verb-noun combination:

- `build-image.sh` (shell)
- `build-image.py` (Python)
- `build-image.yml` (Ansible)

This makes it clear they serve similar purposes and improves discoverability.

---

# 8. Quick Review Checklist

When reviewing an MR:

**Shell Script (.sh):**
- Does it follow verb-noun.sh?
- Is the verb on the approved list?
- Is the noun precise?
- Is it lowercase and hyphen-separated?

**Python Script (.py):**
- Does it follow verb-noun.py?
- Is the verb on the approved list?
- Is the noun precise?
- Is it lowercase and hyphen-separated?
- Is it a special file that should be skipped? (setup.py, __init__.py, etc.)

**Ansible Playbook (.yml):**
- Does it follow verb-noun.yml?
- Is the verb on the approved list?
- Is the noun precise?
- Is it lowercase and hyphen-separated?

**Ansible Role:**
- Is it lowercase_with_underscores?
- Is it capability-oriented?
- Would this name make sense inside a collection?

---

# 9. Enforcement

This naming standard is enforced via pre-commit hooks:

- **Shell scripts:** `validate-shell-naming.py`
- **Python scripts:** `validate-python-naming.py`
- **Ansible playbooks:** Custom ansible-lint rule (`ORG001`)

All validators reference the same source of truth: `tools/approved-verbs.yml`

To test compliance:
```bash
# Run all naming checks
pre-commit run shell-naming --all-files
pre-commit run python-naming --all-files
pre-commit run ansible-lint --all-files

# Or run all pre-commit hooks
pre-commit run --all-files
```

---

# 10. Living Standard

This document is intentionally opinionated but flexible.

Changes to approved verbs or patterns should be:
- Proposed
- Reviewed
- Documented

Consistency over preference.

Clarity over ego.
