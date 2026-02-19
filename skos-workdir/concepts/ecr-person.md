---
id: ecr-person
prefLabel: "ECR Person"
altLabels: ["ECR", "Engagement Context Role", "Engagement Context Role Person"]
depth: 1
broader: ["roles-and-representatives"]
narrower: []
related: ["ecr-vlei-credential"]
---

# ECR Person

## Definition

An ECR Person (Engagement Context Role Person) is a natural person serving in an Engagement Context Role at a Legal Entity, representing a function within a specific engagement context such as a project-based, contractual, or operational capacity. Unlike Official Organizational Role Persons, engagement context roles are defined by the Legal Entity itself and do not require validation against public registries or ISO 5009 role lists. This makes the ECR designation broader and more flexible, suitable for representing functional roles, consultants, project leads, or any person the entity needs to credential for a specific engagement.

## Key Facts

- ECR roles are defined entirely by the Legal Entity, giving organizations flexibility to credential persons for any engagement context they deem appropriate
- ECR vLEI Credentials support privacy-preserving graduated disclosure, allowing the holder to reveal only selected personally identifying information to verifiers
- ECR vLEI Credentials can be issued either by a Qualified vLEI Issuer (requiring a QVI ECR Authorization credential) or directly by the Legal Entity itself (LE Direct Issuance)
- The LE Direct Issuance pathway allows Legal Entities to issue ECR credentials without involving the QVI for each individual credential, reducing operational overhead
- ECR Persons undergo the same identity verification requirements as other credential holders -- IAL2 identity assurance and cryptographic identity authentication via OOBI sessions
- ECR credentials do not appear on the GLEIF LEI page by default, unlike OOR credentials which require public disclosure consent

## Rules & Constraints

- The Legal Entity defines the engagement context role and is solely responsible for the accuracy and appropriateness of the role designation
- When issued by a QVI, the ECR credential chain requires a QVI ECR Authorization credential from a LAR authorizing the specific issuance
- Identity assurance must still meet at least IAL2 (NIST 800-63A) or an approved digital identity scheme, regardless of whether the role is externally validated
- The ECR vLEI Credential must not assert trustworthiness of the Legal Entity itself; it only binds the person to the engagement context role
- Revocation follows the same patterns as other vLEI Credentials: voluntary (engagement ends) or involuntary (entity LEI status change or governance violation)
- Personally identifying information in ECR credentials is subject to graduated disclosure protections under the ACDC specification

## Examples

- **Project manager for a joint venture**: A Legal Entity credentials a project manager working on a cross-organizational initiative, enabling counterparties to verify their role without revealing unnecessary personal details
- **External consultant**: A consulting firm issues an ECR vLEI Credential to a consultant engaged on a client project, defining the engagement context as the specific advisory engagement
- **LE Direct Issuance for internal staff**: A large corporation uses LE Direct Issuance to credential departmental leads for internal systems access verification, bypassing the QVI for each individual credential
- **Contractual representative**: A person representing a Legal Entity in a specific contractual capacity receives an ECR credential scoped to that contract engagement

## Disambiguation

> **ECR Person** vs **OOR Person**: An ECR Person holds a role defined by the Legal Entity for a specific engagement context, with no requirement for external validation. An OOR Person holds a formally recognized official organizational role validated against external public sources and ISO 5009. ECR is broader and entity-defined; OOR is narrower and externally verified.

## Navigation

- **Up**: [Roles and Representatives](./roles-and-representatives.md)
- **Down**: *(none)*
- **Related**: [ECR vLEI Credential](./ecr-vlei-credential.md)
