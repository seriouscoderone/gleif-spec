#!/usr/bin/env python3
"""Compile concept entries from agent output files into extraction-log.json."""
import json
import re
import os

OUTPUT_FILES = [
    "/private/tmp/claude-501/-Users-seriouscoderone-code-gleif-spec/tasks/ab73fb8.output",
    "/private/tmp/claude-501/-Users-seriouscoderone-code-gleif-spec/tasks/a72a503.output",
    "/private/tmp/claude-501/-Users-seriouscoderone-code-gleif-spec/tasks/a15d23f.output",
    "/private/tmp/claude-501/-Users-seriouscoderone-code-gleif-spec/tasks/ae1e51a.output",
]

STAGED_DIR = "/Users/seriouscoderone/code/gleif-spec/staged"


def extract_json_array_from_output(filepath):
    """Extract the JSON array of concepts from an agent output JSONL file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    all_arrays = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            msg = obj.get('message', {})
            if not isinstance(msg, dict):
                continue
            for content_item in msg.get('content', []):
                if not isinstance(content_item, dict):
                    continue
                if content_item.get('type') != 'text':
                    continue
                text = content_item.get('text', '')
                if 'prefLabel' not in text:
                    continue
                # Extract JSON from ```json ... ``` blocks
                matches = re.findall(r'```(?:json)?\s*(\[[\s\S]*?\])\s*```', text)
                for match in matches:
                    try:
                        arr = json.loads(match)
                        if isinstance(arr, list) and len(arr) > 0 and isinstance(arr[0], dict) and 'prefLabel' in arr[0]:
                            all_arrays.append(arr)
                    except json.JSONDecodeError:
                        pass
        except json.JSONDecodeError:
            continue

    if all_arrays:
        # Return the largest array (most complete)
        return max(all_arrays, key=len)
    return []


def get_all_staged_docs():
    """Get list of all staged markdown files."""
    docs = []
    for root, dirs, files in os.walk(STAGED_DIR):
        for f in files:
            if f.endswith('.md'):
                docs.append(f)
    return sorted(docs)


def main():
    all_entries = []
    source_refs = set()

    for output_file in OUTPUT_FILES:
        print(f"Processing: {os.path.basename(output_file)}")
        entries = extract_json_array_from_output(output_file)
        print(f"  Found {len(entries)} entries")
        all_entries.extend(entries)
        for e in entries:
            sr = e.get('sourceRef', '')
            if sr:
                source_refs.add(sr)

    print(f"\nTotal raw entries: {len(all_entries)}")
    print(f"Unique source docs referenced: {len(source_refs)}")
    for sr in sorted(source_refs):
        print(f"  - {sr}")

    # Get all staged docs
    all_docs = get_all_staged_docs()

    extraction_log = {
        "schemeTitle": "vLEI Ecosystem Governance Framework",
        "sourceDir": "staged/",
        "processedDocs": all_docs,
        "entries": all_entries
    }

    output_path = "/Users/seriouscoderone/code/gleif-spec/skos-workdir/extraction-log.json"
    with open(output_path, 'w') as f:
        json.dump(extraction_log, f, indent=2)

    print(f"\nWrote extraction-log.json with {len(all_entries)} entries across {len(all_docs)} processed docs")


if __name__ == '__main__':
    main()
