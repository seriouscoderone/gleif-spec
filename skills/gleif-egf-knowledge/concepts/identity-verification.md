---
id: identity-verification
prefLabel: "Identity Verification"
altLabels: ["Digital Identity Scheme", "IA", "IAL2", "Identity Assurance", "Identity Assurance Level 2", "Identity Authentication", "Signing Authority Verification", "Spot Check"]
depth: 1
broader: ["trust-and-qualification"]
narrower: []
related: ["credential-lifecycle", "qvi-authorized-representative"]
---

# Identity Verification

## Definition

Identity Verification in the vLEI Ecosystem is the combined process of Identity Assurance and Identity Authentication that must be completed before any vLEI Credential can be issued. Identity Assurance verifies a person's real-world identity to at least Identity Assurance Level 2 (IAL2) as defined by NIST SP 800-63A, or through an approved digital identity scheme at High or Substantial Level of Assurance. Identity Authentication cryptographically verifies that the person controls the Autonomic Identifier they claim, through challenge-response protocols conducted during real-time Out-of-Band Introduction (OOBI) sessions. Together, these processes bind a verified real-world identity to a cryptographic identifier.

## Key Facts

- IAL2 requires identity proofing that resolves to a unique real-world identity with evidence that is verified by the credential service provider -- mere self-assertion is insufficient
- Only digital identity schemes rated at High or Substantial Level of Assurance are accepted; commercial or private identity verification services at lower assurance levels are excluded
- Identity Authentication requires a real-time OOBI session with both audio and video, during which participants exchange AIDs and sign unique challenge messages that must be returned as fully signed responses
- Spot checks are periodic re-verification operations where a QAR initiates an unscheduled OOBI session with a previously authenticated person to confirm they still control their AID's private keys
- Signing authority verification confirms that the person has the legal authority to sign on behalf of the Legal Entity, verified through official documentation
- Each vLEI Credential Framework defines the specific identity verification steps required for that credential type, allowing for variation across credential categories

## Rules & Constraints

- Identity verification must be completed before every vLEI Credential issuance -- there are no exemptions for repeat issuances to the same person
- The OOBI session for identity authentication must be continuous (no breaks) and attended by all parties on both audio and video
- Challenge messages used during identity authentication must be unique to each OOBI session and contain a cryptographic nonce
- A third-party service may assist in performing identity assurance (e.g., for LARs), but the QAR must be able to view and confirm the third party's verification results
- Spot checks may be performed at any time and are mandatory when there is reason to suspect that a previously authenticated contact may no longer control their keys
- The identity verification process applies to all representative types: GARs, QARs, DARs, LARs, OOR Persons, and ECR Persons

## Examples

- **IAL2 identity assurance for a LAR**: A QAR verifies a Legal Entity Authorized Representative's real-world identity using government-issued documents and biometric comparison, meeting IAL2 requirements before the LAR can participate in credential operations
- **OOBI challenge-response authentication**: During a live video session, a QAR sends a unique challenge message to a DAR; the DAR's KERI agent signs the challenge and returns it, proving control of the DAR's AID private keys
- **Spot check on an OOR Person**: A QAR conducts an unscheduled OOBI session with a previously credentialed CEO to verify continued control of their AID, as part of ongoing trust maintenance
- **Digital identity scheme**: A European QVI accepts an eIDAS High-level digital identity for identity assurance of a LAR, bypassing manual IAL2 document verification

## Disambiguation

> **Identity Assurance** vs **Identity Authentication**: Identity Assurance verifies who a person is in the real world (real-world identity proofing). Identity Authentication verifies that a person controls a specific cryptographic identifier (AID control proof). Both are required for Identity Verification, but they address different aspects of trust.

## Navigation

- **Up**: [Trust and Qualification](./trust-and-qualification.md)
- **Down**: *(none)*
- **Related**: [Credential Lifecycle](./credential-lifecycle.md), [QVI Authorized Representative](./qvi-authorized-representative.md)
