---
id: acdc
prefLabel: "Authentic Chained Data Container"
altLabels: ["ACDC", "ACDC Fully-Compressed Form", "ACDC Fully-Expanded Form", "ACDC Schema-Compressed Form", "ACDC Source", "Form 1", "Form 2", "Form 3", "Rules Section", "Source Link", "Sources Section"]
depth: 1
broader: ["vlei-credentials"]
narrower: []
related: ["cryptographic-primitives", "vlei-credential-schema"]
---

# Authentic Chained Data Container

## Definition

The Authentic Chained Data Container (ACDC) is a specification and data container format for verifiable credentials, originally developed under the Trust over IP Foundation. ACDCs provide the underlying data model for all vLEI Credentials, supporting cryptographic chaining through source links, composable JSON Schema definitions, multiple serialization formats, Ricardian contracts in the Rules section, and chain-link confidentiality for privacy-preserving disclosure. Its security model is derived from KERI, making it tightly integrated with the Autonomic Identifier infrastructure that underpins the vLEI Ecosystem.

## Key Facts

- ACDCs exist in three forms: Fully-Expanded (Form 1) embeds the complete schema, attributes, and rules; Fully-Compressed (Form 2) replaces each section with its SAID; Schema-Compressed (Form 3) replaces only the schema section with its SAID while keeping other sections expanded
- The Sources section within an ACDC chains it to its source credentials by including their SAIDs, enabling delegated authorization restrictions and creating the verifiable provenance chain
- The Rules section allows issuers to impose usage restrictions on the credential or its attributes, functioning as a machine-readable Ricardian contract
- ACDCs support Graduated Disclosure, allowing holders to selectively reveal different portions of credential data in response to different presentation requests
- Contractually Protected Disclosure enables credential presentation under contractual terms that govern how disclosed information may be used by the verifier
- Every ACDC section (schema, attributes, rules, sources) carries a SAID for content-based immutability verification
- ACDCs are a compliant external proof format of the W3C Verifiable Credential 2.0 specification, but with distinctive features not found in typical VC implementations

## Rules & Constraints

- All ACDC credentials in the vLEI Ecosystem must support JSON serialization and use Ed25519 signatures encoded in CESR proof format
- Each ACDC must include a SAID computed over its content, providing approximately 128 bits of cryptographic strength for tamper evidence
- Source Links in the Sources section must reference valid, non-revoked source credentials; a broken link renders the credential unverifiable
- The Rules section SAID must be verified independently to ensure the usage restrictions have not been modified
- Graduated Disclosure does not support all-or-nothing presentation; it specifically enables partial and contextual data sharing at the field level

## Examples

- **Fully-Expanded OOR Credential**: An OOR vLEI Credential presented with all sections visible, including the complete schema definition, role attributes, source chain, and usage rules
- **Schema-Compressed Presentation**: A verifier receives an ECR vLEI Credential where only the schema SAID is included; the verifier resolves the full schema from the vLEI Credential Schema Registry
- **Source Link Chain**: A QVI OOR AUTH vLEI Credential's Sources section contains the SAID of the Legal Entity vLEI Credential and the SAID of the QVI vLEI Credential, establishing the authorization chain
- **Rules-Based Restriction**: An ACDC's Rules section specifies that the credential may only be presented for regulatory compliance purposes, not for marketing

## Disambiguation

> **ACDC** vs **W3C Verifiable Credential**: While ACDCs are a compliant external proof format of W3C VC 2.0, they provide normative chaining support, KERI-based security, graduated disclosure, and Ricardian contracts that are distinctive to the ACDC specification.

> **ACDC Source Links** vs **Credential Chain**: Source Links are the specific technical mechanism (SAID references in the Sources section) within an ACDC. The Credential Chain is the broader trust hierarchy concept that emerges when multiple ACDCs are linked through their Sources sections.

## Navigation

- **Up**: [vLEI Credentials](./vlei-credentials.md)
- **Down**: *(none)*
- **Related**: [Cryptographic Primitives](./cryptographic-primitives.md), [vLEI Credential Schema](./vlei-credential-schema.md)
