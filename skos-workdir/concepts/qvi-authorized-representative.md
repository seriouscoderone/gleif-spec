---
id: qvi-authorized-representative
prefLabel: "QVI Authorized Representative"
altLabels: ["Delegated AID QVI Authorized Representative Lead", "Dual QAR Issuance Workflow", "QAR", "QAR Lead", "Qualified vLEI Issuer Authorized Representative", "Two-QAR Workflow"]
depth: 1
broader: ["roles-and-representatives"]
narrower: []
related: ["identity-verification"]
---

# QVI Authorized Representative

## Definition

A QVI Authorized Representative (QAR) is an individual authorized by a Qualified vLEI Issuer to perform identity verification, credential issuance, and revocation operations on behalf of that QVI. Every QVI must designate at least two QARs who operate within a multi-signature group, with a QAR Lead responsible for coordinating delegated AID creation. A mandatory dual-QAR workflow requires that separate QARs verify identity and co-sign credential issuance, ensuring no single individual can unilaterally issue a vLEI Credential.

## Key Facts

- A minimum of two QARs is required per QVI, operating in a multi-sig group to prevent single points of failure in credential issuance
- The dual-QAR (Two-QAR) workflow mandates that one QAR performs identity verification while a different QAR co-signs the resulting credential issuance, enforcing separation of duties
- The QAR Lead is responsible for initiating the creation of the QVI's delegated AID and coordinating the multi-sig group setup
- QARs must contact GLEIF External GARs for approval before executing rotation events that occur less than six months after the previous rotation
- QARs hold cryptographic signing keys and are responsible for safeguarding them within a Trusted Execution Environment or equivalent secure infrastructure
- QARs perform identity assurance at a minimum of IAL2 (NIST 800-63A) or via an approved digital identity scheme rated at High or Substantial Level of Assurance

## Rules & Constraints

- If a QAR's private key is compromised, the QVI must report to GLEIF within 24 hours and execute a recovery rotation event
- QARs must verify the identity of all persons (DARs, LARs, OOR Persons) through real-time OOBI sessions with audio and video, signing and returning unique challenge messages
- The same QAR who performs the identity verification step must not be the sole signer on the resulting credential -- a second QAR must co-sign
- QARs perform spot checks to periodically re-verify that previously authenticated contacts still control their private keys
- QAR key rotation requires prophylactic rotation on unpredictable schedules, not just in response to compromise

## Examples

- **QAR Lead setting up a QVI**: The QAR Lead initiates the multi-sig group inception event with GLEIF External GARs, establishing the QVI's delegated AID
- **Dual-QAR credential issuance**: QAR-A conducts an OOBI session with a Legal Entity Authorized Representative to verify identity; QAR-B then reviews the verification evidence and co-signs the Legal Entity vLEI Credential
- **Spot check verification**: A QAR initiates an unscheduled OOBI session with a LAR to perform a challenge-response exchange, confirming the LAR still controls their AID's private keys

## Disambiguation

> **QVI Authorized Representative (QAR)** vs **Legal Entity Authorized Representative (LAR)**: QARs represent the Qualified vLEI Issuer and perform identity verification and credential issuance. LARs represent the Legal Entity and request issuance and revocation of credentials on the entity's behalf. They operate on opposite sides of the issuer-holder relationship.

## Navigation

- **Up**: [Roles and Representatives](./roles-and-representatives.md)
- **Down**: *(none)*
- **Related**: [Identity Verification](./identity-verification.md)
