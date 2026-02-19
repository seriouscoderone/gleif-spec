# gleif-spec

Pre-synthesized SKOS knowledge base for the **GLEIF vLEI Ecosystem Governance Framework (EGF v3.0)**, packaged as a Claude Code marketplace plugin.

42 concepts distilled from 24 EGF source documents, organized across 5 domain pillars:

- **KERI Infrastructure** — identifiers, key management, witnesses, delegation, cryptographic primitives
- **Roles and Representatives** — GLEIF, QVIs, Legal Entities, GARs, QARs, LARs, DARs
- **Trust and Qualification** — qualification programs, identity verification, risk assessment, SLAs
- **vLEI Credentials** — ACDC format, credential types, schemas, chains, exchange, lifecycle
- **vLEI Ecosystem Governance** — framework structure, information trust policies, agreements

## Installation

### From the CLI

```sh
claude plugin marketplace add seriouscoderone/gleif-spec
claude plugin install gleif-egf-knowledge@gleif-spec
```

### From inside Claude Code

```
/plugin marketplace add seriouscoderone/gleif-spec
/plugin install gleif-egf-knowledge@gleif-spec
```

### Project-level auto-install

Add to any project's `.claude/settings.json` so collaborators get the plugin automatically:

```json
{
  "extraKnownMarketplaces": {
    "gleif-spec": {
      "source": {
        "source": "github",
        "repo": "seriouscoderone/gleif-spec"
      }
    }
  },
  "enabledPlugins": {
    "gleif-egf-knowledge@gleif-spec": true
  }
}
```

## Usage

The plugin provides a **gleif-expert** subagent that answers vLEI/EGF questions using the concept files without loading them into your main context:

```
Task tool:
  subagent_type: "gleif-expert"
  prompt: "What is a Qualified vLEI Issuer and how does credential chaining work?"
```

You can also read concept files directly from `skills/gleif-egf-knowledge/concepts/`.

## Repository Structure

```
.claude-plugin/
  marketplace.json          Plugin registry
  plugin.json               Marketplace metadata
.claude/
  agents/gleif-expert.md    Read-only subagent for domain queries
  settings.json             Project plugin config
skills/gleif-egf-knowledge/
  SKILL.md                  Skill entry point
  taxonomy.json             42-concept SKOS taxonomy
  concept-map.md            Navigable tree view
  concepts/                 42 concept summaries (~600 words each)
skos-workdir/
  extraction-log.json       294 raw concept entries from 24 docs
  taxonomy.json             Working copy of taxonomy
  concepts/                 Working copy of concept files
  compile_extraction.py     Agent output parser
  fix_agent3.py             Truncated output fixer
staged/                     Source markdown files (gitignored)
```

## Source Documents

24 EGF v3.0 documents converted from PDF to markdown, covering the primary document, glossary, governance requirements, technical requirements (parts 1-3), credential frameworks (LE, OOR, ECR, QVI Auth, QVI Identifier), trust assurance framework, information trust policies, risk assessment, qualification agreement, and appendices 1-7.

## License

Apache-2.0
