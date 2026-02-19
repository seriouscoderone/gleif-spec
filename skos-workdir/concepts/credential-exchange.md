---
id: credential-exchange
prefLabel: "Credential Exchange"
altLabels: ["Admit Message", "Contractually Protected Disclosure", "Credential Issuance and Revocation Registry", "Credential Wallet", "Graduated Disclosure", "IPEX", "IPEX Protocol", "Issuance and Presentation Exchange", "Issuance and Presentation Exchange Protocol", "PTEL", "Proof Request", "Public Transaction Event Log", "Revocation Log", "TEL", "Transaction Event Log", "Validator", "Verifier", "vLEI Credentials Wallet"]
depth: 1
broader: ["vlei-credentials"]
narrower: []
related: ["oobi-protocol"]
---

# Credential Exchange

## Definition

Credential Exchange encompasses the protocols and infrastructure for presenting and verifying vLEI Credentials between parties. The central protocol is the Issuance and Presentation Exchange Protocol (IPEX), defined within the ACDC specification, which governs how credential elements are exchanged between issuers and holders (issuance) and between holders and verifiers (presentation). The exchange infrastructure also includes credential registries, transaction event logs for tracking issuance and revocation state, credential wallets for secure storage, and disclosure mechanisms that enable privacy-preserving credential presentation.

## Key Facts

- IPEX supports two distinct disclosure modes: Graduated Disclosure allows selective revelation of credential attributes, while Contractually Protected Disclosure requires the verifier to agree to usage terms before data is revealed
- Each vLEI Credential Issuer must maintain a highly-available Credential Issuance and Revocation Registry compliant with the Public Transaction Event Log (PTEL) section of the ACDC specification
- Verifiers initiate exchange by sending a Proof Request specifying the credential criteria they need satisfied; presentation can occur in any context -- in-person, online, or over the phone
- A Verifier cryptographically checks signatures on event messages, while a Validator determines that a signed statement was valid at the time of issuance; these are distinct roles
- Credential Wallets store vLEI Credentials and their associated private keys, requiring trusted execution environments for protection
- Transaction Event Logs (TELs) provide a verifiable record of credential state changes, anchored to KERI key events for tamper-evident auditability

## Rules & Constraints

- Credential presentation via IPEX does not address credential lifecycle management (creation, revocation); it specifically handles the exchange mechanics
- Graduated Disclosure allows selective field-level revelation; holders may disclose different portions of a credential in response to different Proof Requests
- Contractually Protected Disclosure requires explicit contractual agreements between presenter and verifier before credential data is revealed
- Revocation Logs must be maintained by QVIs and transferred to GLEIF upon QVI termination to ensure continuity of revocation status
- QVIs must report each issuance and revocation event to GLEIF through the vLEI Reporting API for public record maintenance

## Examples

- **Standard Proof Request**: A financial regulator sends a Proof Request to a bank officer asking for their OOR vLEI Credential proving their CFO role; the officer's wallet presents the credential via IPEX
- **Graduated Disclosure**: An ECR vLEI Credential holder reveals only their role title and organization to a business partner, withholding personal contact details
- **Contractually Protected Disclosure**: A credential holder presents their vLEI to a third-party auditor under terms that restrict the auditor from sharing the disclosed data with other parties
- **Registry Verification**: A verifier checks the Credential Issuance and Revocation Registry to confirm a presented credential has not been revoked before accepting it

## Disambiguation

> **Credential Exchange** vs **Credential Lifecycle**: Exchange covers the presentation and verification mechanics (how credentials move between parties). Lifecycle covers the creation, maintenance, and revocation processes (how credentials come into existence and are terminated).

> **Verifier** vs **Validator**: A Verifier cryptographically checks that the signature on an event or credential is valid. A Validator determines whether a signed statement associated with an identifier was valid at the time of issuance, which is a broader determination.

## Navigation

- **Up**: [vLEI Credentials](./vlei-credentials.md)
- **Down**: *(none)*
- **Related**: [Out-of-Band Introduction](./oobi-protocol.md)
