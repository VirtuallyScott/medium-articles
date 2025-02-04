#!/bin/bash

# Check if mmdc is available
if ! command -v mmdc &> /dev/null
then
    echo "Error: mermaid-cli (mmdc) is not installed."
    echo "Install with: npm install -g @mermaid-js/mermaid-cli"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p mermaid/output

# Process all Mermaid files
for file in mermaid/*.mmd; do
    if [ -f "$file" ]; then
        base_name=$(basename "$file" .mmd)
        mmdc -i "$file" -o "mermaid/output/${base_name}.png" \
            --backgroundColor white \
            --configFile mermaid/config.json
    fi
done

echo "Diagrams generated in mermaid/output/"
