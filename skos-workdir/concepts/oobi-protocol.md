---
id: oobi-protocol
prefLabel: "Out-of-Band Introduction"
altLabels: ["Challenge Message", "OOBI", "OOBI Session", "Out-of-Band Interaction", "Out-of-Band Introduction Session"]
depth: 1
broader: ["trust-and-qualification"]
narrower: []
related: ["credential-exchange", "security-infrastructure"]
---

# Out-of-Band Introduction

## Definition

Out-of-Band Introduction (OOBI) is the protocol in the KERI ecosystem for bootstrapping trust between parties through initial discovery and real-time cryptographic authentication sessions. OOBI operates in two phases: a discovery mechanism that publishes AID resolution information through well-known URIs, websites, DHTs, DID method resolvers, or ledgers; and a live interaction session conducted over audio and video where participants exchange Autonomic Identifiers and perform cryptographic authentication through unique Challenge Messages that must be signed and returned. OOBI itself does not authenticate an identifier -- it provides the initial introduction that must be followed by cryptographic verification.

## Key Facts

- OOBI sessions require continuous real-time audio and video participation from all parties, ensuring mutual live presence during identity and key management ceremonies
- Challenge Messages contain a cryptographic nonce unique to each OOBI session, preventing replay attacks across sessions
- The signed Challenge Message response proves that the responder controls the private keys associated with the presented AID, without revealing those keys
- OOBI discovery information can be published through multiple mechanisms: well-known URIs, websites, distributed hash tables, DID method resolvers, and ledgers
- Spot Checks are a specific OOBI operation performed with an unauthenticated contact to verify that the other person in the live session controls the claimed private keys
- OOBI sessions are mandatory for identity verification before issuance of vLEI Credentials, forming a critical link between real-world identity and cryptographic identity

## Rules & Constraints

- Every Challenge Message must be unique to its OOBI session; reuse of challenge nonces across sessions is prohibited
- The signed response to a Challenge Message must be returned during the same live session in which it was issued
- OOBI sessions must maintain continuous audio and video for the duration of the identity verification ceremony
- OOBI discovery does not constitute authentication; successful introduction must always be followed by cryptographic verification through challenge-response
- Multi-factor authentication is required during OOBI sessions as specified in the technical requirements for KERI infrastructure
- If an OOBI session is interrupted or cannot maintain live audio/video, the session must be restarted with new Challenge Messages

## Examples

- **GAR-to-QAR OOBI Session**: During QVI qualification, GLEIF Authorized Representatives conduct an OOBI session with QVI Authorized Representatives, exchanging AIDs and verifying control through signed Challenge Messages over a live video call
- **QAR-to-LAR Identity Verification**: A QVI Authorized Representative performs an OOBI session with a Legal Entity Authorized Representative to authenticate the LAR's AID before issuing Legal Entity vLEI Credentials
- **Spot Check**: A periodic verification where an existing authenticated contact is re-verified through a new OOBI exchange and challenge-response to confirm ongoing control of private keys
- **OOBI Discovery via Well-Known URI**: GLEIF publishes its Root AID discovery information at a well-known URI endpoint, enabling any party to resolve the GLEIF AID and initiate trust bootstrapping

## Disambiguation

> **Out-of-Band Introduction (OOBI)** vs **Credential Exchange (IPEX)**: OOBI handles the initial discovery and authentication of identifiers between parties through live sessions. IPEX (Issuance and Presentation Exchange Protocol) handles the subsequent exchange, presentation, and verification of credentials between already-authenticated parties.

## Navigation

- **Up**: [Trust and Qualification](./trust-and-qualification.md)
- **Down**: *(none)*
- **Related**: [Credential Exchange](./credential-exchange.md), [Security Infrastructure](./security-infrastructure.md)
