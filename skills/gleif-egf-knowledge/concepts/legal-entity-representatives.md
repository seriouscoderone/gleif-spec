---
id: legal-entity-representatives
prefLabel: "Legal Entity Representatives"
altLabels: ["DAR", "Designated Authorized Representative", "LAR", "LAR Lead", "Legal Entity Authorized Representative"]
depth: 1
broader: ["roles-and-representatives"]
narrower: []
related: ["legal-entity", "qvi-auth-vlei-credential"]
---

# Legal Entity Representatives

## Definition

Legal Entity Representatives are the authorized individuals who act on behalf of a Legal Entity within the vLEI Ecosystem, divided into two distinct roles. Designated Authorized Representatives (DARs) hold signing authority to execute agreements such as the vLEI Issuer Qualification Agreement, authorize qualification checklists, and designate or replace Legal Entity Authorized Representatives. Legal Entity Authorized Representatives (LARs) manage day-to-day credential operations, including requesting the issuance and revocation of Legal Entity vLEI Credentials, OOR vLEI Credentials, and ECR vLEI Credentials, with a LAR Lead initiating multi-sig group creation.

## Key Facts

- DARs are the only representatives authorized to execute the vLEI Issuer Qualification Agreement and to designate or replace LARs
- LARs operate in a multi-signature group to prevent unilateral credential operations, with a LAR Lead coordinating the group's AID inception
- LARs issue QVI Authorization vLEI Credentials (QVI AUTH) to Qualified vLEI Issuers, providing cryptographic authorization for the issuance or revocation of specific role credentials
- The DAR-to-LAR designation chain provides a clear chain of accountability: the Legal Entity designates DARs, who in turn designate LARs
- Both DARs and LARs must undergo identity verification (Identity Assurance and Identity Authentication) by a QVI Authorized Representative before they can act in their roles
- A sole-employee entity may operate with a single-signer threshold as a special exception to the multi-sig requirement

## Rules & Constraints

- Only DARs may execute binding agreements on behalf of the Legal Entity; LARs cannot sign qualification agreements
- LARs must complete identity assurance at a minimum of IAL2 (NIST 800-63A) or via an approved digital identity scheme
- A QAR or third-party service may assist in performing Identity Assurance of LARs, but the QAR must be able to view and confirm the third-party's verification results
- When a LAR leaves the organization or is no longer authorized, the Legal Entity must initiate revocation of that LAR's credentials and designate a replacement through the DAR
- LARs request credential issuance and revocation through QVI Authorization vLEI Credentials, which form part of the internal credential chain and are not presented to external verifiers

## Examples

- **DAR executing an agreement**: A company's Chief Legal Officer, designated as a DAR, signs the vLEI Issuer Qualification Agreement with GLEIF on behalf of the Legal Entity and designates three LARs for ongoing operations
- **LAR requesting OOR credential issuance**: A LAR issues a QVI OOR Authorization vLEI Credential to the QVI, instructing it to issue an OOR vLEI Credential for a newly appointed board director
- **LAR Lead initiating multi-sig group**: The LAR Lead coordinates the inception event for the Legal Entity's multi-sig AID, establishing the group that will collectively authorize credential operations
- **LAR revoking a credential**: When a C-suite officer departs, a LAR issues a QVI AUTH credential instructing the QVI to revoke the departing officer's OOR vLEI Credential

## Disambiguation

> **Legal Entity Representatives (DAR/LAR)** vs **QVI Authorized Representative (QAR)**: DARs and LARs represent the Legal Entity and act on the entity's behalf in credential-related matters. QARs represent the Qualified vLEI Issuer and perform identity verification and credential issuance. They interact across the issuer-holder boundary.

## Navigation

- **Up**: [Roles and Representatives](./roles-and-representatives.md)
- **Down**: *(none)*
- **Related**: [Legal Entity](./legal-entity.md), [QVI Authorization vLEI Credential](./qvi-auth-vlei-credential.md)
