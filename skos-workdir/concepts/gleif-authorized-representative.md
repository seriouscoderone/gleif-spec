---
id: gleif-authorized-representative
prefLabel: "GLEIF Authorized Representative"
altLabels: ["External GAR", "External GLEIF Authorized Representative", "GAR"]
depth: 1
broader: ["roles-and-representatives"]
narrower: []
related: ["delegation-hierarchy"]
---

# GLEIF Authorized Representative

## Definition

A GLEIF Authorized Representative (GAR) is an individual authorized by GLEIF to hold cryptographic keys, perform identity verification, and approve key management operations within the vLEI Ecosystem. GARs are divided into two functional categories: Internal GARs, who manage the GLEIF Internal Delegated AID (GIDA) for internal ecosystem participation, and External GARs, who manage the GLEIF External Delegated AID (GEDA) for QVI-facing operations including QVI credential issuance and QVI AID delegation. GARs operate at the highest operational tier of the vLEI trust hierarchy, directly below the GLEIF Root AID.

## Key Facts

- Internal GARs and External GARs serve distinct operational functions, managing separate delegated identifiers (GIDA and GEDA respectively) under the GLEIF Root AID
- External GARs are responsible for conducting identity verification of QVI Authorized Representatives before QVI vLEI Credentials can be issued
- External GARs must approve QVI rotation events that occur less than six months after the previous rotation, providing oversight of unusual key management activity
- GARs operate within multi-signature groups with weighted thresholds, meaning no single GAR can unilaterally authorize key events or credential operations
- GARs do not interact directly with Legal Entities or their representatives; their operational scope is limited to the GLEIF-to-QVI level of the trust hierarchy
- Both Internal and External GAR groups follow policies that mirror the GLEIF Root AID policies, with the GIDA having relaxed TEE requirements compared to the Root AID

## Rules & Constraints

- GARs must undergo identity verification themselves before being authorized to perform their representative functions
- All GAR key management operations require multi-signature authorization meeting the weighted threshold specified for their respective delegated AID
- External GARs must conduct OOBI sessions with QARs for identity verification, including real-time audio and video participation and cryptographic Challenge Message exchange
- External GARs must review and approve any QVI key rotation occurring within six months of the last rotation
- Internal GARs and External GARs cannot substitute for each other; each manages only their designated delegated AID
- GARs must comply with the GLEIF Continuity Policy ensuring survival of control authority even if individual GARs become unavailable

## Examples

- **External GAR QVI Onboarding**: During QVI qualification, External GARs conduct an OOBI session with the incoming QVI's Authorized Representatives, verify their identities through Challenge Messages, and then use the GEDA to issue the QVI vLEI Credential and delegate the QVI's AID
- **Internal GAR Ecosystem Participation**: Internal GARs use the GIDA to participate in vLEI ecosystem infrastructure activities and hold vLEI Credentials on behalf of GLEIF as an internal entity
- **External GAR Rotation Approval**: A QVI requests an emergency key rotation only four months after its previous rotation; External GARs review the circumstances and approve the rotation event before it can proceed
- **GAR Multi-Sig Key Event**: When the GEDA requires a key rotation, multiple External GARs each sign the rotation event with their individual keys, and the event is authorized only when the weighted threshold is met

## Disambiguation

> **GLEIF Authorized Representative (GAR)** vs **QVI Authorized Representative (QAR)**: GARs represent GLEIF and operate at the GLEIF-to-QVI level, managing GLEIF's delegated AIDs and verifying QVI representatives. QARs represent a specific QVI and operate at the QVI-to-Legal Entity level, performing identity verification of entity representatives and issuing credentials. GARs authorize QVIs; QARs serve Legal Entities.

## Navigation

- **Up**: [Roles and Representatives](./roles-and-representatives.md)
- **Down**: *(none)*
- **Related**: [Delegation Hierarchy](./delegation-hierarchy.md)
