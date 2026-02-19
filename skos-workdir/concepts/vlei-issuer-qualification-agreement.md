---
id: vlei-issuer-qualification-agreement
prefLabel: "vLEI Issuer Qualification Agreement"
altLabels: ["Ancillary Duties", "Appendix 7", "Core Duties", "Force Majeure", "Intellectual Property Rights in vLEIs", "Liquidated Damages", "Mediation and Arbitration", "No Sublicensing of Qualification", "QVI Records", "QVI-LE Contract Terms", "Qualification Agreement", "Qualified vLEI Issuer Records", "Qualified vLEI Issuer-Legal Entity Required Contract Terms", "Third Party Services", "Third-Party Service Provider", "Third-Party Services"]
depth: 1
broader: ["vlei-ecosystem-governance"]
narrower: []
related: ["qualified-vlei-issuer"]
---

# vLEI Issuer Qualification Agreement

## Definition

The vLEI Issuer Qualification Agreement is the binding legal contract between GLEIF and each Qualified vLEI Issuer that establishes the complete set of rights and obligations for participation in the vLEI Ecosystem. It covers core duties (EGF compliance, credential operations, records management), ancillary duties (cooperation during termination, credential assumption), intellectual property provisions, liability with liquidated damages, dispute resolution through mediation and arbitration, third-party services constraints, and required contract terms that QVIs must flow down to Legal Entities (Appendix 7).

## Key Facts

- Liquidated damages are calculated as USD 1.00 multiplied by the number of active vLEI Credentials for the last 12 months as documented in KERI logs, subject to reduction by a competent judge under Swiss law
- QVI Records must be retained for at least 10 years after the most recent update and made available to GLEIF upon request, covering all documents, procedures, data, and supporting evidence related to vLEI operations
- Third-party services may assist in performing Core Duties (such as identity assurance of LARs) but may not fully perform them; the QVI remains fully responsible and liable for compliance
- The agreement explicitly prohibits sublicensing of qualification status to any third party or making the qualification status available for use by any other entity
- Revisions to this agreement are reviewed and approved by GLEIF only and are not subject to public review, unlike some other EGF controlled documents
- The agreement includes seven appendices: NDA (1), Qualification Program Manual (2), Qualification Program Checklist (3), Contact Details (4), SLA (5), TrustMark Terms (6), and QVI-LE Contract Terms (7)

## Rules & Constraints

- Core Duties require QVIs to comply with the full vLEI Ecosystem Governance Framework and properly issue, maintain, and revoke vLEI Credentials
- Ancillary Duties include cooperation during termination and coordination for assumption of vLEI Credentials from terminated issuers
- Force Majeure provisions suspend contractual obligations during extraordinary situations such as natural disasters, war, or pandemics
- Dispute resolution follows a structured process of mediation followed by arbitration under Swiss law
- QVIs must incorporate the Required Contract Terms (Appendix 7) into their agreements with Legal Entities, ensuring downstream compliance
- The QVI does not acquire any intellectual property rights in vLEIs through the agreement

## Examples

- **Core Duty Compliance**: A QVI ensures all credential issuance follows the identity verification procedures specified in each credential framework, maintains KERI infrastructure per technical requirements, and reports all issuance/revocation events through the vLEI Reporting API
- **Third-Party Service Use**: A QVI engages an external identity verification provider to perform IAL2 identity assurance for LARs, but the QVI's QAR must independently review and confirm the third party's verification results
- **Liquidated Damages Calculation**: A QVI with 5,000 active vLEI Credentials over the past 12 months faces potential liquidated damages of USD 5,000 for material breach

## Disambiguation

> **vLEI Issuer Qualification Agreement** vs **vLEI Issuer Qualification Program**: The Agreement is the binding legal contract governing the ongoing QVI-GLEIF relationship, while the Qualification Program is the initial evaluation process a Candidate vLEI Issuer must pass to become qualified. The Program assesses readiness; the Agreement governs operations.

## Navigation

- **Up**: [vLEI Ecosystem Governance](./vlei-ecosystem-governance.md)
- **Down**: *(none)*
- **Related**: [Qualified vLEI Issuer](./qualified-vlei-issuer.md)
