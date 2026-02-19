---
id: legal-entity
prefLabel: "Legal Entity"
altLabels: ["LE", "LEI", "Legal Entity Identifier"]
depth: 1
broader: ["vlei-ecosystem-governance"]
narrower: []
related: ["global-lei-system", "legal-entity-representatives"]
---

# Legal Entity

## Definition

A Legal Entity is a legal person or structure organized under the laws of any jurisdiction that is uniquely identified by a Legal Entity Identifier (LEI) as defined in ISO 17442, and is eligible to receive vLEI Credentials within the vLEI Ecosystem. The category includes corporations, partnerships, governmental organizations, and supranational bodies, but excludes natural persons who are not acting in a business capacity. Each Legal Entity in the vLEI Ecosystem holds a cryptographic binding between its LEI and a KERI Autonomic Identifier through the Legal Entity vLEI Credential.

## Key Facts

- Legal Entity Identifiers are standardized under ISO 17442 as unique alphanumeric codes assigned within the Global Legal Entity Identifier System
- A Legal Entity must maintain an LEI Entity Status of "Active" and an LEI Registration Status of "Issued," "Pending Transfer," or "Pending Archival" for its vLEI Credentials to remain valid
- Legal Entities participate in the vLEI Ecosystem through two types of representatives: Designated Authorized Representatives (DARs) for executing agreements and Legal Entity Authorized Representatives (LARs) for day-to-day credential operations
- The Legal Entity vLEI Credential serves as the root from which role credentials (OOR and ECR) are chained, meaning revocation of the entity credential invalidates all downstream role credentials
- Natural persons acting in a business capacity (such as sole proprietors) may qualify as Legal Entities under certain jurisdictions
- Legal Entities may choose to have ECR vLEI Credentials issued directly by themselves (LE Direct Issuance) rather than through a QVI

## Rules & Constraints

- A Legal Entity must have a valid, active LEI before any vLEI Credential can be issued to it
- If the LEI Entity Status changes from "Active" to any other status, the QVI must initiate involuntary revocation of the Legal Entity vLEI Credential
- Legal Entities must ensure their privacy policies adequately protect persons to whom OOR and ECR vLEI Credentials are issued
- The Legal Entity must comply with applicable data protection legislation, using the Swiss Federal Data Protection Act (FADP) as the minimum standard where no local legislation applies
- Legal Entities are responsible for designating and managing their DARs and LARs, and must provide qualified representatives for OOBI sessions and identity verification

## Examples

- **Multinational corporation**: A publicly traded company with an active LEI obtains a Legal Entity vLEI Credential from a QVI, then authorizes OOR credentials for its board directors and C-suite officers
- **Government agency**: A national regulatory body registered in the Global LEI System receives a Legal Entity vLEI Credential to enable verifiable digital signing by its authorized officials
- **Sole proprietor in business capacity**: An individual operating under a registered business entity with an LEI qualifies as a Legal Entity for vLEI Credential purposes

## Disambiguation

> **Legal Entity** vs **OOR Person / ECR Person**: A Legal Entity is the organization itself, identified by an LEI. OOR Persons and ECR Persons are natural individuals who represent that organization in specific roles. The Legal Entity holds the entity-level credential; the persons hold role-level credentials chained to it.

## Navigation

- **Up**: [vLEI Ecosystem Governance](./vlei-ecosystem-governance.md)
- **Down**: *(none)*
- **Related**: [Global LEI System](./global-lei-system.md), [Legal Entity Representatives](./legal-entity-representatives.md)
