---
id: qvi-auth-vlei-credential
prefLabel: "QVI Authorization vLEI Credential"
altLabels: ["QVI AUTH Credential", "QVI AUTH vLEI Credential", "QVI Auth vLEI Credential", "QVI Authorization Credential", "Qualified vLEI Issuer Authorization vLEI Credential"]
depth: 2
broader: ["vlei-credential-types"]
narrower: []
related: ["legal-entity-representatives"]
---

# QVI Authorization vLEI Credential

## Definition

The QVI Authorization vLEI Credential is a family of authorization credentials issued by Legal Entity Authorized Representatives (LARs) to Qualified vLEI Issuers, comprising two variants: QVI OOR AUTH and QVI ECR AUTH. These credentials provide secure, explicit instruction and authorization for the issuance and revocation of specific vLEI Role Credentials on behalf of a Legal Entity. Unlike externally presentable credentials, the QVI AUTH family is part of the internal credential chain and is not presented to third-party verifiers -- it serves purely as an authorization artifact between the Legal Entity and the QVI.

## Key Facts

- The QVI AUTH family has two distinct variants: QVI OOR AUTH (schema SAID Edqjl80uP0r_SNSpyImpLGglTEbOwgO77wsOPjyRVKy, v1.0.0) authorizes OOR credential operations, and QVI ECR AUTH (schema SAID ED_PcIn1wFDe0GB0W7Bk9I4Q_c9bQJZCM2w7Ex9Plsta, v1.0.0) authorizes ECR credential operations
- These credentials are issued by LARs, not by GLEIF or the QVI itself, ensuring that the Legal Entity retains explicit control over which role credentials are issued in its name
- The QVI AUTH credential names the specific person, role, and parameters for the credential to be issued or revoked, preventing unauthorized or overbroad credential operations
- Each QVI AUTH credential is chained via its Sources section to the Legal Entity vLEI Credential, establishing that the authorization originates from a valid entity in the ecosystem
- The credential forms a critical link in the trust chain: Legal Entity vLEI Credential -> QVI AUTH vLEI Credential -> OOR/ECR vLEI Credential

## Rules & Constraints

- A QVI must not issue or revoke an OOR or ECR vLEI Credential without holding a valid, non-revoked QVI AUTH credential authorizing that specific operation
- QVI AUTH credentials are not publicly presentable; they serve only as internal authorization between the LAR and the QVI
- Revocation of a QVI AUTH credential does not automatically revoke the downstream OOR or ECR credential that was already issued, but it prevents further operations under that authorization
- The LAR issuing a QVI AUTH must be a duly designated representative authorized by the Legal Entity's Designated Authorized Representative (DAR)
- Both QVI OOR AUTH and QVI ECR AUTH credentials must chain to a valid Legal Entity vLEI Credential; if the entity credential is revoked, the authorization credentials lose their foundation

## Examples

- **QVI OOR AUTH Issuance**: A LAR at a pharmaceutical company issues a QVI OOR AUTH credential to their QVI, authorizing the QVI to issue an OOR vLEI Credential for the company's newly appointed Chief Medical Officer
- **QVI ECR AUTH Issuance**: A LAR issues a QVI ECR AUTH credential instructing the QVI to issue an ECR vLEI Credential for a consultant engaged in a specific regulatory filing project
- **Revocation Authorization**: A LAR issues a QVI OOR AUTH credential authorizing the QVI to revoke the OOR credential of a former board director who has resigned
- **Chain Verification**: A verifier examining an OOR credential traces the chain back through the QVI OOR AUTH to the Legal Entity vLEI Credential to the QVI vLEI Credential, confirming end-to-end authorization

## Disambiguation

> **QVI Authorization vLEI Credential** vs **QVI vLEI Credential**: The QVI vLEI Credential authorizes an organization to act as a Qualified vLEI Issuer in the ecosystem. The QVI AUTH credential authorizes a QVI to perform a specific credential operation (issuance or revocation) for a particular Legal Entity.

> **QVI AUTH** vs **Legal Entity Direct Issuance**: When a Legal Entity directly issues ECR credentials (Legal Entity Direct Issuance), no QVI AUTH credential is needed because the entity is acting as its own issuer. QVI AUTH is only required when a QVI is issuing on behalf of the entity.

## Navigation

- **Up**: [vLEI Credential Types](./vlei-credential-types.md)
- **Down**: *(none)*
- **Related**: [Legal Entity Representatives](./legal-entity-representatives.md)
