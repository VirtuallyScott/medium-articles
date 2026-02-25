#!/usr/bin/env bash
# ShellCheck Helper Script
# Runs shellcheck on shell scripts

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Running shellcheck...${NC}"

# Check if shellcheck is installed
if ! command -v shellcheck &> /dev/null; then
    echo -e "${RED}Error: shellcheck is not installed${NC}"
    echo -e "${YELLOW}Install with: brew install shellcheck${NC}"
    echo -e "${YELLOW}Or visit: https://www.shellcheck.net/${NC}"
    exit 1
fi

echo -e "${GREEN}ShellCheck version:${NC}"
shellcheck --version | head -n 2
echo ""

# Find all .sh files in the repository
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Find all shell scripts
mapfile -t SHELL_SCRIPTS < <(find "$REPO_ROOT" -type f -name "*.sh" ! -path "*/.*" ! -path "*/node_modules/*")

if [ ${#SHELL_SCRIPTS[@]} -eq 0 ]; then
    echo -e "${YELLOW}No shell scripts found${NC}"
    exit 0
fi

echo -e "${YELLOW}Found ${#SHELL_SCRIPTS[@]} shell script(s) to check${NC}"
echo ""

# Run shellcheck
if shellcheck "${SHELL_SCRIPTS[@]}"; then
    echo -e "${GREEN}✓ ShellCheck passed!${NC}"
    exit 0
else
    echo -e "${RED}✗ ShellCheck found issues${NC}"
    exit 1
fi
