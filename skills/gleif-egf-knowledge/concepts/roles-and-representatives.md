---
id: roles-and-representatives
prefLabel: "Roles and Representatives"
altLabels: ["vLEI Ecosystem Stakeholder", "vLEI User"]
depth: 0
broader: []
narrower: ["ecr-person", "gleif-authorized-representative", "legal-entity-representatives", "oor-person", "qualified-vlei-issuer", "qvi-authorized-representative"]
related: []
---

# Roles and Representatives

## Definition

Roles and Representatives is the top-level domain encompassing all organizational and individual roles within the vLEI Ecosystem. It defines the complete stakeholder hierarchy from GLEIF as the governing authority, through Qualified vLEI Issuers as credential-issuing intermediaries, to Legal Entities and their various authorized representatives. Each tier has designated representatives who perform specific functions: GLEIF Authorized Representatives (GARs) manage GLEIF's identifiers and authorize QVI operations, QVI Authorized Representatives (QARs) conduct identity verification and credential issuance, and Legal Entity representatives (DARs, LARs) manage entity-level credential operations. The hierarchy also includes OOR Persons and ECR Persons who hold role-specific credentials.

## Key Facts

- The vLEI Ecosystem has a strict three-tier organizational hierarchy: GLEIF (governing authority) delegates to QVIs (credential issuers), which serve Legal Entities (credential holders)
- Every tier requires designated authorized representatives who hold cryptographic keys and operate within multi-signature groups for their respective identifier operations
- GARs are split into Internal GARs (managing the GIDA for internal operations) and External GARs (managing the GEDA for QVI-facing operations)
- QVIs must have at least two QARs operating in a multi-sig group, with a mandatory dual-QAR workflow where separate QARs verify identity and co-sign credential issuance
- LARs are designated by Designated Authorized Representatives (DARs), who have the higher-level authority to execute agreements and authorize qualification checklists
- vLEI Ecosystem Stakeholders include all participants who follow EGF requirements: GLEIF, QVIs, Legal Entities, OOR Persons, ECR Persons, and vLEI Users
- Individual credential types (QVI, LE, OOR, ECR credentials) are covered under the vLEI Credentials domain rather than this domain

## Rules & Constraints

- Each representative tier can only operate within its designated scope: GARs at the GLEIF-to-QVI level, QARs at the QVI-to-LE level, and LARs/DARs at the entity level
- A QVI must maintain at least two QARs at all times to satisfy the dual-QAR workflow requirement for credential issuance
- DARs have signing authority that LARs do not possess, specifically the authority to execute the vLEI Issuer Qualification Agreement and designate LARs
- All authorized representatives must undergo identity verification before being granted their roles
- Representatives at every tier must participate in multi-signature groups appropriate to their organizational context
- Role credentials (OOR and ECR) bind natural persons to specific organizational or engagement roles, distinct from the representative functions of GARs, QARs, LARs, and DARs

## Examples

- **GLEIF as Governing Authority**: GLEIF serves as both the Governing Authority (setting policy) and Administering Authority (executing operations) of the vLEI EGF, operating through its GARs
- **QVI Dual-QAR Workflow**: When issuing a Legal Entity vLEI Credential, one QAR performs the identity verification of the Legal Entity representative while a second QAR co-signs the credential issuance, ensuring separation of duties
- **DAR Designating LARs**: A Legal Entity's Designated Authorized Representative executes the contract with a QVI and then designates one or more LARs to handle ongoing credential operations
- **OOR Person**: A Chief Executive Officer of a Legal Entity who holds an OOR vLEI Credential binding their identity to their official organizational role

## Navigation

- **Up**: *(top-level concept)*
- **Down**: [ECR Person](./ecr-person.md), [GLEIF Authorized Representative](./gleif-authorized-representative.md), [Legal Entity Representatives](./legal-entity-representatives.md), [OOR Person](./oor-person.md), [Qualified vLEI Issuer](./qualified-vlei-issuer.md), [QVI Authorized Representative](./qvi-authorized-representative.md)
- **Related**: *(none)*
