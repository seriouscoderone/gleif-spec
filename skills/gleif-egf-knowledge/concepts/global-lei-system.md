---
id: global-lei-system
prefLabel: "Global LEI System"
altLabels: ["GLEIS", "Global LEI Repository", "Global Legal Entity Identifier System", "ISO 17442", "LEI Issuer", "ROC", "Regulatory Oversight Committee"]
depth: 1
broader: ["vlei-ecosystem-governance"]
narrower: []
related: ["legal-entity"]
---

# Global LEI System

## Definition

The Global LEI System (GLEIS) is the worldwide infrastructure established under the oversight of the Regulatory Oversight Committee (ROC) -- an organization of regulators from multiple jurisdictions charged by the G-20 -- for the unique identification of legal entities participating in financial transactions through Legal Entity Identifiers. Operated and managed by GLEIF, the system contains the Global LEI Repository, a database holding all current and historical LEIs and LEI reference data. The LEI standard is codified in ISO 17442, which defines the identifier format, assignment rules, and application in digital certificates.

## Key Facts

- The LEI is standardized under ISO 17442, consisting of Part 1 (LEI assignment) and Part 2 (application in digital certificates), providing a globally unique alphanumeric code for each legal entity
- The Regulatory Oversight Committee (ROC) was established by the G-20 to provide regulatory oversight of GLEIF and the Global LEI System across multiple jurisdictions
- LEI Issuers are organizations separately accredited by GLEIF to validate legal entity information and register new LEIs -- they are distinct from Qualified vLEI Issuers, which issue verifiable credentials
- The Global LEI Repository maintained by GLEIF is the authoritative source for all LEI data, serving as the foundation upon which vLEI Credentials reference entity identity
- Every vLEI Credential containing an LEI must be based on an LEI with an Entity Status of "Active" and a Registration Status of "Issued," "Pending Transfer," or "Pending Archival"
- The system predates the vLEI Ecosystem and serves broader financial regulation and reporting purposes beyond verifiable credentials

## Rules & Constraints

- Legal Entities must maintain their LEI in Active status and valid registration status for their vLEI Credentials to remain valid
- If a Legal Entity's LEI Entity Status changes from Active, the Qualified vLEI Issuer must initiate involuntary revocation of the associated vLEI Credentials
- LEI Issuers operate under separate accreditation from GLEIF and are not interchangeable with Qualified vLEI Issuers
- The Global LEI Repository data is publicly accessible, providing transparency for financial counterparties and regulatory bodies
- ISO 17442 compliance is mandatory for all LEI assignments within the system

## Examples

- **Financial transaction identification**: A bank uses LEIs from the Global LEI System to uniquely identify counterparties in derivatives transactions, as required by post-2008 financial regulations
- **vLEI Credential foundation**: A Legal Entity's LEI, retrieved from the Global LEI Repository, is embedded in its Legal Entity vLEI Credential, cryptographically binding the internationally recognized identifier to a KERI AID
- **Regulatory reporting**: National regulators use LEI data from the GLEIS to monitor legal entity activities across jurisdictions, leveraging the ROC oversight structure

## Disambiguation

> **Global LEI System** vs **vLEI Ecosystem**: The Global LEI System is the underlying infrastructure for registering and maintaining Legal Entity Identifiers as standardized alphanumeric codes. The vLEI Ecosystem builds on top of this by wrapping LEIs in cryptographically verifiable ACDC credentials using KERI technology. The GLEIS predates the vLEI and serves broader regulatory purposes.

## Navigation

- **Up**: [vLEI Ecosystem Governance](./vlei-ecosystem-governance.md)
- **Down**: *(none)*
- **Related**: [Legal Entity](./legal-entity.md)
