#!/usr/bin/env bash
#
# Convert all PDFs in egf-docs-part1/ and egf-docs-part2/ to markdown.
# Output goes to staged/ with the same directory structure.
#
# Usage: ./convert-pdfs.sh
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
STAGED_DIR="$SCRIPT_DIR/staged"
SOURCE_DIRS=("egf-docs-part1" "egf-docs-part2")

mkdir -p "$STAGED_DIR"

converted=0
skipped=0
failed=0

for src_dir in "${SOURCE_DIRS[@]}"; do
    src_path="$SCRIPT_DIR/$src_dir"
    if [[ ! -d "$src_path" ]]; then
        echo "Warning: $src_dir not found, skipping"
        continue
    fi

    out_dir="$STAGED_DIR/$src_dir"
    mkdir -p "$out_dir"

    for pdf in "$src_path"/*.pdf "$src_path"/*.PDF; do
        [[ -f "$pdf" ]] || continue

        basename="$(basename "$pdf")"
        name="${basename%.*}"
        md_file="$out_dir/${name}.md"

        # Skip if markdown already exists and is newer than the PDF
        if [[ -f "$md_file" && "$md_file" -nt "$pdf" ]]; then
            echo "SKIP (up to date): $basename"
            ((skipped++))
            continue
        fi

        echo "CONVERTING: $basename"
        if marker_single "$pdf" \
            --output_format markdown \
            --output_dir "$out_dir" \
            --disable_image_extraction 2>&1; then
            # marker_single creates a subdirectory named after the file; move the .md up
            marker_out_dir="$out_dir/${name}"
            if [[ -d "$marker_out_dir" ]]; then
                mv "$marker_out_dir"/*.md "$md_file" 2>/dev/null || true
                rm -rf "$marker_out_dir"
            fi
            echo "  -> $md_file"
            ((converted++))
        else
            echo "  FAILED: $basename"
            ((failed++))
        fi
    done
done

echo ""
echo "Done: $converted converted, $skipped skipped (up to date), $failed failed"
