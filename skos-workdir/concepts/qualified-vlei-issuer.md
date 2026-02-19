---
id: qualified-vlei-issuer
prefLabel: "Qualified vLEI Issuer"
altLabels: ["Candidate vLEI Issuer", "QVI"]
depth: 1
broader: ["roles-and-representatives"]
narrower: ["qvi-self-issuance"]
related: ["qualification-program", "service-level-management", "vlei-issuer-qualification-agreement"]
---

# Qualified vLEI Issuer

## Definition

A Qualified vLEI Issuer (QVI) is an organization that has been formally qualified by GLEIF through the vLEI Issuer Qualification Program and holds a valid QVI vLEI Credential, authorizing it to issue, maintain, and revoke Legal Entity vLEI Credentials, OOR vLEI Credentials, and ECR vLEI Credentials within the vLEI Ecosystem. The term also encompasses Candidate vLEI Issuers, which are organizations currently undergoing the qualification evaluation process but not yet authorized to issue credentials. A QVI is distinct from an LEI Issuer, which registers LEIs in the Global LEI System but does not issue verifiable credentials.

## Key Facts

- A QVI must operate with at least a 3-of-2 multisig signing scheme, requiring a minimum of two QVI Authorized Representatives (QARs) in a multi-signature group
- QVIs receive a delegated AID from GLEIF's External Delegated AID (GEDA), creating a cryptographic binding in the delegation hierarchy
- QVI qualification cannot be sublicensed -- no QVI may make its qualification status available to any third party
- QVIs must retain all records related to the vLEI Issuer Qualification Agreement for at least 10 years after the most recent update
- Liquidated damages for QVI non-compliance are calculated at USD 1.00 per active vLEI Credential over the trailing 12 months, as documented in KERI logs
- QVIs must report every issuance and revocation event to GLEIF through the vLEI Reporting API for publication on LEI pages
- Third-party services may assist QVI operations but cannot fully perform Core Duties, and the QVI remains fully liable for compliance

## Rules & Constraints

- A QVI must comply with the vLEI Ecosystem Governance Framework and all controlled documents at all times
- Key rotation events occurring less than six months from the previous rotation require prior approval from GLEIF External GARs
- If a QVI's vLEI Credential is revoked, a grace period applies before all downstream credentials (Legal Entity, OOR, ECR) are invalidated
- QVIs must install, test, and implement GLEIF-sponsored open-source vLEI software
- A QVI must maintain IT security policies sufficient to protect all vLEI services and designate an Information Security Manager
- Key compromise must be reported to GLEIF within 24 hours, followed by investigation, a recovery rotation event, and a published key recovery explanation
- QVIs are subject to Annual vLEI Issuer Qualification and may also face Extraordinary Qualification if documentation is found to be non-current

## Examples

- **Global trust service provider**: A multinational digital identity firm that completes the vLEI Issuer Qualification Program and receives a QVI vLEI Credential from GLEIF, enabling it to issue Legal Entity vLEI Credentials to corporate clients
- **Candidate undergoing evaluation**: A regional compliance services company that has applied to become a QVI and is completing the self-assessment checklist, letters of assurance, and conflict-of-interest evaluation
- **QVI self-issuance**: A Qualified vLEI Issuer that issues a Legal Entity vLEI Credential and OOR vLEI Credentials to itself as a Legal Entity, subject to GLEIF oversight

## Disambiguation

> **Qualified vLEI Issuer** vs **LEI Issuer**: A QVI issues cryptographically verifiable ACDC-based vLEI Credentials within the KERI ecosystem, whereas an LEI Issuer is an organization accredited by GLEIF to register LEI codes in the Global LEI System. The two serve fundamentally different functions despite both operating under GLEIF oversight.

## Navigation

- **Up**: [Roles and Representatives](./roles-and-representatives.md)
- **Down**: [QVI Self-Issuance](./qvi-self-issuance.md)
- **Related**: [vLEI Issuer Qualification Program](./qualification-program.md), [Service Level Management](./service-level-management.md), [vLEI Issuer Qualification Agreement](./vlei-issuer-qualification-agreement.md)
