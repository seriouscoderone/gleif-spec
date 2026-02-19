---
id: qvi-self-issuance
prefLabel: "QVI Self-Issuance"
altLabels: []
depth: 2
broader: ["qualified-vlei-issuer"]
narrower: []
related: []
---

# QVI Self-Issuance

## Definition

QVI Self-Issuance is the practice whereby a Qualified vLEI Issuer issues vLEI Credentials to itself in its capacity as a Legal Entity. Specifically, a QVI may issue a Legal Entity vLEI Credential and OOR vLEI Credentials to itself, subject to GLEIF oversight. This capability recognizes that QVIs are themselves legal entities that need vLEI Credentials for their own organizational identity, while introducing governance safeguards to manage the inherent conflict of interest in self-certification.

## Key Facts

- Self-issuance is currently permitted for Legal Entity vLEI Credentials and OOR vLEI Credentials only; it does not extend to ECR vLEI Credentials
- GLEIF retains the authority to require QVIs to contract with a third-party QVI for their own credentials after a future GLEIF-announced deadline, effectively ending self-issuance when the ecosystem has sufficient maturity and QVI coverage
- Self-issuance creates a unique trust dynamic where the issuer and holder are the same entity, requiring GLEIF oversight to compensate for the absence of an independent verification party
- The practice exists as a pragmatic accommodation for the early stages of the vLEI Ecosystem, when the number of QVIs may be insufficient to ensure every QVI can practically obtain credentials from another QVI
- QVI self-issued credentials must follow the same credential frameworks, identity verification procedures, and technical requirements as credentials issued to external Legal Entities
- Self-issued OOR vLEI Credentials still require role verification against official sources such as ISO 5009 role lists and public business registries

## Rules & Constraints

- Self-issuance is limited to Legal Entity vLEI Credentials and OOR vLEI Credentials; ECR vLEI Credentials are not within scope
- All self-issued credentials remain subject to GLEIF oversight, including reporting through the vLEI Reporting API
- GLEIF may set a future deadline after which QVIs must obtain their own credentials from a third-party QVI rather than self-issuing
- Self-issued credentials must comply with all applicable credential governance frameworks and technical requirements, with no relaxation of standards
- The QVI must maintain the same records and documentation for self-issued credentials as for any other credential issuance
- If GLEIF mandates third-party issuance, QVIs must transition within the specified timeframe or face non-compliance consequences

## Examples

- **Legal Entity Self-Issuance**: A QVI issues itself a Legal Entity vLEI Credential binding its own LEI to its KERI AID, following the same identity verification and credential issuance procedures it would use for any external client
- **OOR Self-Issuance**: A QVI issues OOR vLEI Credentials to its own CEO and Board Directors, verifying their roles against public registry records just as it would for any other Legal Entity's officers
- **Transition to Third-Party Issuance**: GLEIF announces a deadline requiring all QVIs to obtain credentials from another QVI; a QVI begins the process of engaging a peer QVI to replace its self-issued credentials before the deadline

## Disambiguation

> **QVI Self-Issuance** vs **Legal Entity Direct Issuance (ECR)**: QVI Self-Issuance refers to a QVI issuing credentials to itself as a Legal Entity, while Legal Entity Direct Issuance refers to any Legal Entity (not just QVIs) issuing ECR vLEI Credentials directly to its own engagement context role holders without going through a QVI. Self-issuance is about QVI organizational identity; direct issuance is about streamlined ECR credential operations.

## Navigation

- **Up**: [Qualified vLEI Issuer](./qualified-vlei-issuer.md)
- **Down**: *(none)*
- **Related**: *(none)*
