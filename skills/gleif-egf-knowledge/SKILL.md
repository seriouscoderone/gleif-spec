---
name: vlei-egf-knowledge
description: >
  Domain knowledge base for the vLEI Ecosystem Governance Framework. Contains 42
  concepts organized by SKOS taxonomy. Use when answering questions about
  verifiable Legal Entity Identifiers, KERI infrastructure, ACDC credentials, and vLEI governance.
---

# vLEI Ecosystem Governance Framework Knowledge Skill

## How to Use This Skill

This is a **pre-synthesized knowledge base** — not a search engine. Each concept file contains
a complete, standalone summary (~600 words) organized by SKOS semantic relationships.

### Recommended: Subagent Invocation

This skill is best invoked in a **subagent** via the Task tool so the concept files load into
a separate context window rather than the main conversation. This keeps the primary context
clean for the user's actual work.

**Example invocation pattern:**

```
Task tool call:
  subagent_type: "general-purpose"
  prompt: |
    You are a vLEI domain expert. Read the skill at:
    /path/to/skills/gleif-egf-knowledge/SKILL.md

    Then answer this question: {user's question}

    Use the concept files in concepts/ to find the answer.
    Follow navigation links (Up/Down/Related) if the answer spans concepts.
    Cite which concept files you referenced.
```

### Query Strategy

1. **Identify the concept** — find the most relevant concept for the user's question
2. **Read the concept file** — load `concepts/{slug}.md` (~2-4K tokens)
3. **Follow navigation links** — if the answer spans concepts, follow Up/Down/Related links
4. **Answer from the concept file** — cite facts directly; don't guess beyond what's written

### When You Need More Context

- **Broader context**: Follow the "Up" navigation link to the parent concept
- **More detail**: Follow "Down" links to narrower child concepts
- **Adjacent topics**: Follow "Related" links for cross-cutting associations
- **Overview**: Read `concept-map.md` for the full taxonomy tree

## Concept Map

See [concept-map.md](./concept-map.md) for the full navigable tree.

### Top-Level Concepts

- [KERI Infrastructure](concepts/keri-infrastructure.md) — Cryptographic identity infrastructure (KERI protocol, AIDs, witnesses, key management)
- [Roles and Representatives](concepts/roles-and-representatives.md) — Organizational actors (GLEIF, QVIs, Legal Entities, authorized representatives)
- [Trust and Qualification](concepts/trust-and-qualification.md) — Trust assurance, identity verification, qualification programs
- [vLEI Credentials](concepts/vlei-credentials.md) — Credential types, schemas, ACDC format, issuance chains, and lifecycle
- [vLEI Ecosystem Governance](concepts/vlei-ecosystem-governance.md) — Governance framework, policies, agreements, risk, and compliance

## Taxonomy

Full taxonomy data is in [taxonomy.json](./taxonomy.json) with 42 concepts
across 3 depth levels.

| Depth | Count | Role |
|-------|-------|------|
| 0 — Top | 5 | Domain pillars |
| 1 — Mid | 30 | Core topics |
| 2 — Leaf | 7 | Specific details |

## Concepts Directory

All concept files are in `concepts/`:

- [Authentic Chained Data Container](concepts/acdc.md)
- [Annual vLEI Issuer Qualification](concepts/annual-qualification.md)
- [Assurance Dimensions](concepts/assurance-dimensions.md)
- [Autonomic Identifier](concepts/autonomic-identifier.md)
- [Credential Chain](concepts/credential-chain.md)
- [Credential Exchange](concepts/credential-exchange.md)
- [Credential Lifecycle](concepts/credential-lifecycle.md)
- [Cryptographic Primitives](concepts/cryptographic-primitives.md)
- [Delegation Hierarchy](concepts/delegation-hierarchy.md)
- [ECR Person](concepts/ecr-person.md)
- [ECR vLEI Credential](concepts/ecr-vlei-credential.md)
- [GLEIF](concepts/gleif.md)
- [GLEIF Authorized Representative](concepts/gleif-authorized-representative.md)
- [Global LEI System](concepts/global-lei-system.md)
- [Identity Verification](concepts/identity-verification.md)
- [KERI Infrastructure](concepts/keri-infrastructure.md)
- [Key Management](concepts/key-management.md)
- [Legal Entity](concepts/legal-entity.md)
- [Legal Entity Representatives](concepts/legal-entity-representatives.md)
- [Out-of-Band Introduction](concepts/oobi-protocol.md)
- [OOR Person](concepts/oor-person.md)
- [OOR vLEI Credential](concepts/oor-vlei-credential.md)
- [vLEI Issuer Qualification Program](concepts/qualification-program.md)
- [Qualified vLEI Issuer](concepts/qualified-vlei-issuer.md)
- [QVI Authorization vLEI Credential](concepts/qvi-auth-vlei-credential.md)
- [QVI Authorized Representative](concepts/qvi-authorized-representative.md)
- [QVI Self-Issuance](concepts/qvi-self-issuance.md)
- [Risk Assessment](concepts/risk-assessment.md)
- [Roles and Representatives](concepts/roles-and-representatives.md)
- [Security Infrastructure](concepts/security-infrastructure.md)
- [Service Level Management](concepts/service-level-management.md)
- [Trust and Qualification](concepts/trust-and-qualification.md)
- [TrustMark](concepts/trustmark.md)
- [vLEI Credential Schema](concepts/vlei-credential-schema.md)
- [vLEI Credential Types](concepts/vlei-credential-types.md)
- [vLEI Credentials](concepts/vlei-credentials.md)
- [vLEI Ecosystem Governance](concepts/vlei-ecosystem-governance.md)
- [Information Trust Policies](concepts/vlei-ecosystem-information-trust-policies.md)
- [vLEI Issuer Qualification Agreement](concepts/vlei-issuer-qualification-agreement.md)
- [vLEI Reporting API](concepts/vlei-reporting-api.md)
- [vLEI Software](concepts/vlei-software.md)
- [Witness and Watcher Networks](concepts/witness-and-watcher-network.md)

## Source Attribution

- **Source documents**: 24 files
- **Created**: 2026-02-18
- **Generated by**: skos-distillation-skill
