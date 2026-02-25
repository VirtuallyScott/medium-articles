#!/usr/bin/env bash
# Python Linting Helper Script
# Runs flake8, pylint, or available Python linters

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Running Python linters...${NC}"

# Find script directory and repository root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Find all .py files (excluding common directories)
mapfile -t PYTHON_FILES < <(find "$REPO_ROOT" -type f -name "*.py" \
    ! -path "*/venv/*" \
    ! -path "*/.venv/*" \
    ! -path "*/env/*" \
    ! -path "*/node_modules/*" \
    ! -path "*/__pycache__/*" \
    ! -path "*/.tox/*" \
    ! -path "*/build/*" \
    ! -path "*/dist/*")

if [ ${#PYTHON_FILES[@]} -eq 0 ]; then
    echo -e "${YELLOW}No Python files found${NC}"
    exit 0
fi

echo -e "${YELLOW}Found ${#PYTHON_FILES[@]} Python file(s) to check${NC}"
echo ""

LINTER_FOUND=false
LINT_FAILED=false

# Try flake8 first
if command -v flake8 &> /dev/null; then
    LINTER_FOUND=true
    echo -e "${GREEN}Running flake8...${NC}"
    flake8 --version
    echo ""
    
    if flake8 "${PYTHON_FILES[@]}" --max-line-length=120 --extend-ignore=E203,W503; then
        echo -e "${GREEN}✓ flake8 passed!${NC}"
    else
        echo -e "${RED}✗ flake8 found issues${NC}"
        LINT_FAILED=true
    fi
    echo ""
fi

# Try pylint if available
if command -v pylint &> /dev/null; then
    LINTER_FOUND=true
    echo -e "${GREEN}Running pylint...${NC}"
    pylint --version | head -n 1
    echo ""
    
    if pylint "${PYTHON_FILES[@]}" --max-line-length=120 --disable=C0114,C0115,C0116; then
        echo -e "${GREEN}✓ pylint passed!${NC}"
    else
        echo -e "${RED}✗ pylint found issues${NC}"
        LINT_FAILED=true
    fi
    echo ""
fi

# Try ruff if available (modern fast linter)
if command -v ruff &> /dev/null; then
    LINTER_FOUND=true
    echo -e "${GREEN}Running ruff...${NC}"
    ruff --version
    echo ""
    
    if ruff check "${PYTHON_FILES[@]}"; then
        echo -e "${GREEN}✓ ruff passed!${NC}"
    else
        echo -e "${RED}✗ ruff found issues${NC}"
        LINT_FAILED=true
    fi
    echo ""
fi

# If no linter found
if [ "$LINTER_FOUND" = false ]; then
    echo -e "${YELLOW}No Python linter found${NC}"
    echo -e "${YELLOW}Install one with:${NC}"
    echo -e "${YELLOW}  pip install flake8${NC}"
    echo -e "${YELLOW}  pip install pylint${NC}"
    echo -e "${YELLOW}  pip install ruff${NC}"
    echo -e "${YELLOW}Or: brew install ruff${NC}"
    exit 1
fi

# Exit with appropriate code
if [ "$LINT_FAILED" = true ]; then
    echo -e "${RED}✗ Python linting found issues${NC}"
    exit 1
else
    echo -e "${GREEN}✓ All Python linters passed!${NC}"
    exit 0
fi
