---
id: ecr-vlei-credential
prefLabel: "ECR vLEI Credential"
altLabels: ["ECR Authorization vLEI Credential", "ECR Credential", "Engagement Context Role vLEI Credential", "LE Direct Issuance", "Legal Entity Direct Issuance", "Legal Entity Engagement Context Role vLEI Credential", "QVI ECR AUTH vLEI Credential", "QVI ECR Authorization vLEI Credential"]
depth: 2
broader: ["vlei-credential-types"]
narrower: []
related: ["ecr-person"]
---

# ECR vLEI Credential

## Definition

The ECR vLEI Credential (Engagement Context Role vLEI Credential) is a vLEI role credential that binds a natural person to a specific engagement context role at a Legal Entity. Unlike OOR credentials, the role is defined by the Legal Entity itself and does not require validation against public registries or ISO 5009 role lists. The ECR credential is unique among vLEI credential types in supporting two issuance paths: it may be issued by a Qualified vLEI Issuer as a value-added service, or directly by the Legal Entity itself through Legal Entity Direct Issuance. ECR credentials natively support privacy-preserving graduated disclosure of personally identifying information.

## Key Facts

- The ECR vLEI Credential uses schema SAID EohcE9MV90LrygJuYN1N0c5XXNFkzwFxUBfQ24v7qeEY at version 1.0.0, which includes fields for personally identifying information that may be selectively disclosed
- ECR is the only vLEI credential type that can be issued directly by a Legal Entity without QVI intermediation, using the Legal Entity Direct Issuance pathway
- When issued by a QVI, the issuance chain requires: Legal Entity vLEI Credential -> QVI ECR AUTH vLEI Credential (issued by LAR) -> ECR vLEI Credential (issued by QVI)
- When issued directly by the Legal Entity, the chain is shorter: Legal Entity vLEI Credential -> ECR vLEI Credential (issued by LAR)
- Graduated Disclosure allows ECR holders to reveal only selected fields (such as role title and organization) while withholding personal details like contact information
- Contractually Protected Disclosure enables ECR presentation under terms that restrict how the verifier may use the disclosed information
- The dual-QAR workflow applies when the QVI issues the credential; direct Legal Entity issuance follows the LAR's own multi-sig group procedures

## Rules & Constraints

- The ECR Person's identity must be assured and authenticated before credential issuance, regardless of whether the QVI or Legal Entity is the issuer
- When issued by a QVI, a valid QVI ECR AUTH credential from a LAR is required before the QVI may proceed
- Roles are defined by the Legal Entity and do not require validation against public registries, but must accurately describe the person's engagement context
- The Legal Entity must hold a valid Legal Entity vLEI Credential to issue ECR credentials directly; revocation of the entity credential invalidates all downstream ECR credentials
- The credential does not assert the trustworthiness of the Legal Entity itself; it only attests to the person's role at that entity
- QVIs must report ECR credential issuance and revocation to GLEIF through the vLEI Reporting API

## Examples

- **QVI-Issued ECR**: A QVI issues an ECR vLEI Credential to an external legal counsel retained by a corporation for a specific litigation matter, authorized by a QVI ECR AUTH from the corporation's LAR
- **Direct Legal Entity Issuance**: A multinational company directly issues ECR credentials to its project managers through its own LARs, without involving its QVI
- **Graduated Disclosure**: An ECR holder presents their credential to a partner organization, revealing their role as "Sustainability Compliance Auditor" and their employer, but withholding their email and phone number
- **Contractually Protected ECR Presentation**: An ECR credential is presented to a regulator under terms specifying the disclosed information may only be used for the specific compliance review

## Disambiguation

> **ECR vLEI Credential** vs **OOR vLEI Credential**: ECR credentials cover engagement-specific roles defined by the Legal Entity (e.g., project manager, auditor), do not require external validation, and support direct Legal Entity issuance. OOR credentials cover official organizational roles (e.g., CEO, CFO) that must be validated against external sources, and can only be issued by QVIs.

> **Legal Entity Direct Issuance** vs **QVI Issuance**: In direct issuance, the Legal Entity itself issues the ECR credential through its LARs without QVI involvement. In QVI issuance, the LAR first issues a QVI ECR AUTH credential, and the QVI then issues the ECR credential.

## Navigation

- **Up**: [vLEI Credential Types](./vlei-credential-types.md)
- **Down**: *(none)*
- **Related**: [ECR Person](./ecr-person.md)
