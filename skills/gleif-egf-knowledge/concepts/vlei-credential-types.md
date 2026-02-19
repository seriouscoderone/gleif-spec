---
id: vlei-credential-types
prefLabel: "vLEI Credential Types"
altLabels: ["LE vLEI Credential", "Legal Entity vLEI Credential", "QVI Credential", "QVI vLEI Credential", "Qualified vLEI Issuer vLEI Credential", "vLEI Role Credential"]
depth: 1
broader: ["vlei-credentials"]
narrower: ["ecr-vlei-credential", "oor-vlei-credential", "qvi-auth-vlei-credential"]
related: []
---

# vLEI Credential Types

## Definition

The vLEI Ecosystem defines a structured hierarchy of credential types, each serving a distinct purpose in the chain of trust. At the top, the QVI vLEI Credential is issued by GLEIF to authorize organizations as Qualified vLEI Issuers. The Legal Entity vLEI Credential binds a Legal Entity's LEI to a KERI Autonomic Identifier. Role credentials -- the OOR vLEI Credential and ECR vLEI Credential -- bind natural persons to specific organizational or engagement roles. The QVI Authorization vLEI Credential family provides internal authorization for credential issuance and revocation operations.

## Key Facts

- The QVI vLEI Credential has schema SAID ELqriXX1-lbV9zgXP4BXxqJlpZTgFchll3cyjaCyVKiz at version 1.0.0 and is the only credential type issued directly by GLEIF
- The Legal Entity vLEI Credential (schema SAID EK0jwjJbtYLIynGtmXXLO5MGJ7BduX2vr2_MhM9QjAxZ) serves as the root entity credential from which all role credentials are chained
- OOR vLEI Credentials (schema SAID EILRwno8cEnkGTi9cr7-PFg_IXTPx9fZ0r9snFFZ0nm) require validation against external official sources or ISO 5009 role lists
- ECR vLEI Credentials (schema SAID EohcE9MV90LrygJuYN1N0c5XXNFkzwFxUBfQ24v7qeEY) support privacy-preserving graduated disclosure of personally identifying information
- Revocation of a QVI vLEI Credential triggers a grace period of up to 90 days during which GLEIF manages transition of affected Legal Entities to new QVIs
- Each credential type is governed by its own specific vLEI Credential Governance Framework document within the EGF

## Rules & Constraints

- If a QVI vLEI Credential is revoked, no further issuance, verification, or revocation of vLEIs is permitted during the grace period
- Role credentials (OOR and ECR) must chain to a valid Legal Entity vLEI Credential; revocation of the entity credential invalidates all downstream role credentials
- QVI-issued role credentials require a QVI Authorization credential from a Legal Entity Authorized Representative before the QVI may issue or revoke the credential
- Legal Entities may directly issue ECR vLEI Credentials but may not directly issue OOR vLEI Credentials or Legal Entity vLEI Credentials
- A QVI may self-issue a Legal Entity vLEI Credential and OOR vLEI Credentials to itself, subject to GLEIF oversight, though GLEIF may require third-party QVI issuance after a specified deadline

## Examples

- **QVI vLEI Credential**: GLEIF issues this credential to a financial services firm that has completed the vLEI Issuer Qualification Program, authorizing it to issue vLEI Credentials to Legal Entities
- **Legal Entity vLEI Credential**: A QVI issues this to a bank, cryptographically associating the bank's LEI with its KERI AID
- **OOR vLEI Credential**: A QVI issues this to a bank's Chief Financial Officer, binding the person to the CFO role validated against public registry records
- **ECR vLEI Credential**: The bank directly issues this to an external auditor engaged for a specific project, using Legal Entity Direct Issuance

## Disambiguation

> **vLEI Credential Types** vs **Credential Chain**: Credential types define the distinct categories of credentials (QVI, LE, OOR, ECR, AUTH), while the credential chain describes how instances of these types are cryptographically linked through ACDC source references.

> **QVI vLEI Credential** vs **QVI Authorization vLEI Credential**: The QVI vLEI Credential authorizes the QVI itself to participate in the ecosystem; the QVI Authorization credential family authorizes a QVI to issue or revoke specific role credentials on behalf of a Legal Entity.

## Navigation

- **Up**: [vLEI Credentials](./vlei-credentials.md)
- **Down**: [ECR vLEI Credential](./ecr-vlei-credential.md), [OOR vLEI Credential](./oor-vlei-credential.md), [QVI Authorization vLEI Credential](./qvi-auth-vlei-credential.md)
- **Related**: *(none)*
