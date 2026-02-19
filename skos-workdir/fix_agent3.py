#!/usr/bin/env python3
"""Extract JSON from agent 3 output (which may lack closing code block markers)."""
import json
import re

filepath = "/private/tmp/claude-501/-Users-seriouscoderone-code-gleif-spec/tasks/a15d23f.output"

with open(filepath, 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    try:
        obj = json.loads(line)
        msg = obj.get('message', {})
        if not isinstance(msg, dict):
            continue
        for ci in msg.get('content', []):
            if not isinstance(ci, dict) or ci.get('type') != 'text':
                continue
            text = ci['text']
            if 'prefLabel' not in text:
                continue

            # Find JSON array after ```json marker
            m = re.search(r'```(?:json)?\s*(\[[\s\S]*)', text)
            if m:
                json_text = m.group(1).rstrip()
                # Remove trailing ``` if present
                if json_text.endswith('```'):
                    json_text = json_text[:-3].rstrip()

                try:
                    arr = json.loads(json_text)
                    print(f"Found {len(arr)} entries")

                    # Merge into extraction-log.json
                    log_path = "/Users/seriouscoderone/code/gleif-spec/skos-workdir/extraction-log.json"
                    with open(log_path, 'r') as f2:
                        log = json.load(f2)

                    log['entries'].extend(arr)
                    with open(log_path, 'w') as f2:
                        json.dump(log, f2, indent=2)

                    print(f"Merged. Total entries now: {len(log['entries'])}")
                except json.JSONDecodeError as e:
                    print(f"JSON error: {e}")
                    # Try to find last valid ]
                    last_bracket = json_text.rfind(']')
                    if last_bracket > 0:
                        try:
                            arr = json.loads(json_text[:last_bracket+1])
                            print(f"Found {len(arr)} entries (after truncation fix)")

                            log_path = "/Users/seriouscoderone/code/gleif-spec/skos-workdir/extraction-log.json"
                            with open(log_path, 'r') as f2:
                                log = json.load(f2)

                            log['entries'].extend(arr)
                            with open(log_path, 'w') as f2:
                                json.dump(log, f2, indent=2)

                            print(f"Merged. Total entries now: {len(log['entries'])}")
                        except json.JSONDecodeError as e2:
                            print(f"Still failed: {e2}")
    except json.JSONDecodeError:
        continue
