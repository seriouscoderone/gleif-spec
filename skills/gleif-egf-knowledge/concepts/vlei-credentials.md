---
id: vlei-credentials
prefLabel: "vLEI Credentials"
altLabels: ["Verifiable LEI", "Verifiable LEI Credential", "vLEI", "vLEI Credential"]
depth: 0
broader: []
narrower: ["acdc", "credential-chain", "credential-exchange", "credential-lifecycle", "vlei-credential-schema", "vlei-credential-types"]
related: []
---

# vLEI Credentials

## Definition

A vLEI Credential is a verifiable credential within the vLEI Ecosystem implemented as an Authentic Chained Data Container (ACDC) that cryptographically binds a Legal Entity Identifier to a KERI Autonomic Identifier. Every vLEI Credential must support JSON serialization, include Self-Addressing Identifiers (SAIDs) for tamper-evident immutability, and comply with its specific vLEI Credential Governance Framework. Unlike traditional LEI assignments, vLEI Credentials are cryptographically verifiable digital artifacts that enable automated trust decisions without relying on centralized directories.

## Key Facts

- vLEI Credentials are not W3C Verifiable Credentials in the traditional sense; they use the ACDC format, which is a compliant external proof format of the W3C VC 2.0 specification with distinctive features including normative chaining support
- Every credential carries a SAID computed from its content, making the credential and its data mutually tamper-evident with approximately 128 bits of cryptographic strength
- All vLEI Credential signatures must use the Ed25519 algorithm encoded in the CESR proof format
- The vLEI Ecosystem defines five primary credential types: QVI vLEI Credential, Legal Entity vLEI Credential, OOR vLEI Credential, ECR vLEI Credential, and the QVI Authorization vLEI Credential family
- Credentials exist in three serialization forms: fully-expanded (Form 1), fully-compressed (Form 2), and schema-compressed (Form 3), allowing flexible disclosure
- GLEIF serves as the Root of Trust for the entire credential hierarchy, anchoring all downstream credentials through cryptographic chaining

## Rules & Constraints

- A vLEI Credential can only be issued when the underlying LEI has an Entity Status of Active and a Registration Status of Issued, Pending Transfer, or Pending Archival in the Global LEI System
- Each credential must comply with its specific vLEI Credential Governance Framework, which defines identity verification requirements, issuance workflows, and revocation conditions
- Revocation of any credential in the chain invalidates all downstream credentials that reference it as a source
- Credential issuance requires prior completion of both Identity Assurance (to at least IAL2) and Identity Authentication via KERI challenge-response protocols
- QVI-issued credentials require a dual-QAR workflow where two separate QVI Authorized Representatives participate in each issuance

## Examples

- **QVI vLEI Credential**: Issued by GLEIF to authorize an organization as a Qualified vLEI Issuer, enabling it to issue credentials to Legal Entities
- **Legal Entity vLEI Credential**: Issued by a QVI to a Legal Entity, binding the entity's LEI to a KERI AID as the root entity-level credential
- **OOR vLEI Credential**: Issued by a QVI to a person holding an Official Organizational Role such as Chief Executive Officer, validated against external sources
- **ECR vLEI Credential**: Issued to a person in an Engagement Context Role, which may be issued by either a QVI or directly by the Legal Entity itself

## Disambiguation

> **vLEI Credentials** vs **LEI**: An LEI is a 20-character alphanumeric code registered in the Global LEI System under ISO 17442. A vLEI Credential is a cryptographically verifiable ACDC that wraps an LEI with digital signatures and chaining, enabling automated verification.

> **vLEI Credentials** vs **W3C Verifiable Credentials**: While ACDCs are a compliant external proof format of the W3C VC 2.0 specification, they have distinctive features including normative credential chaining through source links, KERI-based key management, and graduated disclosure that differentiate them from typical VC implementations.

## Navigation

- **Up**: *(top-level concept)*
- **Down**: [Authentic Chained Data Container](./acdc.md), [Credential Chain](./credential-chain.md), [Credential Exchange](./credential-exchange.md), [Credential Lifecycle](./credential-lifecycle.md), [vLEI Credential Schema](./vlei-credential-schema.md), [vLEI Credential Types](./vlei-credential-types.md)
- **Related**: *(none)*
