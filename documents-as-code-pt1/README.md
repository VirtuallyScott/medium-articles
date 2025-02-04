# Documents as Code - Part 1

This project demonstrates using Mermaid diagrams as code documentation.

## Structure

- `mermaid/`: Directory containing Mermaid diagram source files
  - `basic-flow.mmd`: Basic flowchart example
  - `git-branches.mmd`: Git branching diagram example
- `generate-diagrams.sh`: Conversion script for generating PNGs
- `mermaid/output/`: Generated diagram images (auto-created)

## Requirements

- Node.js
- mermaid-cli: `npm install -g @mermaid-js/mermaid-cli`

## Usage

1. Edit/create `.mmd` files in the `mermaid/` directory
2. Generate diagrams:

```bash
chmod +x generate-diagrams.sh
./generate-diagrams.sh
```

## Why Mermaid?

- Version control friendly
- Easy to modify
- Text-based format
- Integration with documentation workflows
