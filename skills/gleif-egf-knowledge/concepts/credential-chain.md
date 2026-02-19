---
id: credential-chain
prefLabel: "Credential Chain"
altLabels: ["Chain of Trust", "Credential Chaining", "Provenance Chain", "Root of Trust", "vLEI Chain of Trust"]
depth: 1
broader: ["vlei-credentials"]
narrower: []
related: ["autonomic-identifier", "delegation-hierarchy"]
---

# Credential Chain

## Definition

The Credential Chain is the cryptographic chain of trust that underpins organizational identity in the vLEI Ecosystem. Implemented through ACDC source references and Self-Addressing Identifiers (SAIDs), it connects GLEIF as the root of trust through Qualified vLEI Issuers to Legal Entities and their representatives. Each credential in the chain embeds the SAID of one or more preceding credentials in its Sources section, creating a verifiable provenance path. Revocation of any credential in the chain automatically invalidates all downstream credentials that depend on it.

## Key Facts

- The chain flows in a strict hierarchy: GLEIF Root AID issues QVI vLEI Credentials, which enable QVIs to issue Legal Entity vLEI Credentials, which in turn enable OOR and ECR role credentials
- Chaining is implemented through the ACDC Sources section, where each credential includes the SAID of its source credential, creating tamper-evident linkage
- GLEIF provides both the organizational root of trust (as Governing Authority) and the cryptographic root of trust (through the GLEIF Root AID)
- There are actually two parallel chains: the Credential Chain for vLEI Credentials and the Delegated AID Chain of Trust for KERI identifier delegation; together they form the complete vLEI tree of trust
- The QVI Authorization vLEI Credential family (QVI OOR AUTH and QVI ECR AUTH) serves as an internal link in the chain between Legal Entity authorization and QVI-issued role credentials
- Chain verification requires resolving each source SAID back to its originating credential and confirming that no credential in the path has been revoked

## Rules & Constraints

- If GLEIF revokes a QVI vLEI Credential, all Legal Entity credentials and role credentials issued by that QVI become invalid after the grace period
- If a Legal Entity vLEI Credential is revoked, all OOR and ECR credentials chained from it are immediately invalidated
- Each credential must reference its source credentials through their SAIDs; missing or invalid source references break the chain and render the credential unverifiable
- The chain cannot be extended beyond what is defined in the vLEI Credential Governance Frameworks; no unauthorized credential types may be inserted
- Verifiers must traverse the full chain from the presented credential back to the GLEIF root to confirm validity

## Examples

- **Full OOR Chain**: GLEIF Root AID -> QVI vLEI Credential -> Legal Entity vLEI Credential -> QVI OOR AUTH vLEI Credential -> OOR vLEI Credential
- **ECR Direct Issuance Chain**: GLEIF Root AID -> QVI vLEI Credential -> Legal Entity vLEI Credential -> ECR vLEI Credential (issued directly by the Legal Entity, skipping QVI intermediation)
- **QVI Revocation Cascade**: When GLEIF revokes a QVI credential, the 90-day grace period activates while GLEIF transitions affected Legal Entities to new QVIs; after the grace period, all downstream credentials become invalid

## Disambiguation

> **Credential Chain** vs **Delegation Hierarchy**: The Credential Chain links vLEI Credentials through ACDC source references. The Delegation Hierarchy links KERI Autonomic Identifiers through cooperative delegation events. Both operate in parallel to establish the complete trust architecture.

> **Credential Chain** vs **ACDC Source Links**: Source Links are the technical mechanism (SAID references in the Sources section) that implement credential chaining. The Credential Chain is the broader concept of the trust hierarchy created by those links.

## Navigation

- **Up**: [vLEI Credentials](./vlei-credentials.md)
- **Down**: *(none)*
- **Related**: [Autonomic Identifier](./autonomic-identifier.md), [Delegation Hierarchy](./delegation-hierarchy.md)
