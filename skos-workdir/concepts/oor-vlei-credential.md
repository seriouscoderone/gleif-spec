---
id: oor-vlei-credential
prefLabel: "OOR vLEI Credential"
altLabels: ["Legal Entity Official Organizational Role vLEI Credential", "OOR Authorization vLEI Credential", "OOR Credential", "Official Organizational Role vLEI Credential", "QVI OOR AUTH vLEI Credential", "QVI OOR Authorization vLEI Credential"]
depth: 2
broader: ["vlei-credential-types"]
narrower: []
related: ["oor-person"]
---

# OOR vLEI Credential

## Definition

The OOR vLEI Credential (Official Organizational Role vLEI Credential) is a vLEI role credential that binds a natural person to a specific official organizational role at a Legal Entity. Unlike engagement context roles, the role must be validated against external official sources such as public business registries, certified entity documentation, or the ISO 5009 Official Organization Role Lists. The credential is issued by a Qualified vLEI Issuer through a credential chain that requires both a QVI OOR Authorization credential from a Legal Entity Authorized Representative and the dual-QAR issuance workflow.

## Key Facts

- The OOR vLEI Credential uses schema SAID EILRwno8cEnkGTi9cr7-PFg_IXTPx9fZ0r9snFFZ0nm at version 1.0.0 in the vLEI Credential Schema Registry
- Roles must be validated against ISO 5009 Official Organization Role Lists or equivalent external official sources, such as national business registries
- The OOR Person must provide explicit consent permitting publication of their name and role on the Legal Entity's LEI page on gleif.org
- The full issuance chain requires: Legal Entity vLEI Credential -> QVI OOR AUTH vLEI Credential (issued by LAR) -> OOR vLEI Credential (issued by QVI)
- The dual-QAR workflow is mandatory: one QAR performs identity verification and signs the credential, a second QAR approves and co-signs the issuance
- OOR credentials can be presented in any context -- in-person, online, or over the phone -- to satisfy Proof Requests from verifiers
- Only QVIs may issue OOR vLEI Credentials; unlike ECR credentials, Legal Entities cannot directly issue them

## Rules & Constraints

- The OOR Person's identity must be assured to at least IAL2 (NIST 800-63A) or through a GLEIF-approved digital identity scheme at High or Substantial Level of Assurance
- The role must be verifiable through official public sources, business registry documents, or certified entity documentation; informal or self-declared roles are not eligible
- A QVI must hold a valid QVI OOR AUTH credential from the Legal Entity's LAR before issuing the OOR vLEI Credential
- Revocation of the Legal Entity vLEI Credential cascades to all associated OOR credentials
- The QVI must report each OOR credential issuance and revocation to GLEIF via the vLEI Reporting API
- If the OOR Person leaves their official role, a voluntary revocation should be initiated by the LAR

## Examples

- **CEO Credential**: A QVI issues an OOR vLEI Credential to the CEO of a publicly listed company, with the CEO role validated against the company's public filing with the national business registry
- **Board Director Credential**: An OOR credential is issued to a board director whose appointment is recorded in the commercial register, with their consent for publication on the GLEIF LEI page
- **Revocation on Role Change**: When a CFO is replaced, the Legal Entity's LAR issues a QVI OOR AUTH authorizing revocation of the former CFO's credential, and the QVI issues a new OOR credential to the successor

## Disambiguation

> **OOR vLEI Credential** vs **ECR vLEI Credential**: OOR credentials cover official organizational roles validated against external sources (e.g., CEO, Board Director as defined in ISO 5009). ECR credentials cover engagement-specific roles defined by the Legal Entity itself (e.g., project manager, auditor).

> **OOR vLEI Credential** vs **Legal Entity vLEI Credential**: The Legal Entity credential identifies the organization and binds its LEI to a KERI AID. The OOR credential identifies a specific person acting in an official role at that organization.

## Navigation

- **Up**: [vLEI Credential Types](./vlei-credential-types.md)
- **Down**: *(none)*
- **Related**: [OOR Person](./oor-person.md)
