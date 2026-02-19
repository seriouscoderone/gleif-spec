---
id: key-management
prefLabel: "Key Management"
altLabels: ["Controller", "Ed25519", "Ed25519 Signature", "Inception Event", "Interaction Event", "KEL", "Key Event Log", "Key Pre-Rotation", "Key Rotation", "Key Rotation Event", "Key-Pair Creation and Storage Infrastructure", "Pre-Rotation", "Rotation Event", "Signature Creation Infrastructure"]
depth: 1
broader: ["keri-infrastructure"]
narrower: []
related: ["security-infrastructure"]
---

# Key Management

## Definition

Key Management encompasses the policies and infrastructure for managing asymmetric key pairs within the vLEI Ecosystem, organized into three infrastructure areas: key-pair creation and storage, signature creation, and signature verification. It covers the full lifecycle of cryptographic keys from generation through Ed25519 key pairs, to operational use in signing key events and credentials, to rotation via KERI's pre-rotation mechanism. The key event types -- inception events, rotation events, and interaction events -- are recorded in verifiable Key Event Logs (KELs) that constitute the authoritative record of identifier key state.

## Key Facts

- KERI's pre-rotation mechanism maintains two sets of key pairs simultaneously: current signing keys and pre-committed one-time rotation keys, so that even if current keys are compromised, the attacker cannot predict or control the next key state
- Ed25519 is the specified signature algorithm for the vLEI Ecosystem, providing approximately 128 bits of cryptographic strength with compact 64-byte signatures
- Key Event Logs are append-only verifiable data structures recording every key state change for an AID, endorsed by witnesses and independently verifiable by watchers
- Inception events establish the initial key pairs, configuration parameters, witness pool, and signing thresholds for a new AID
- Interaction events record non-establishment operations such as delegation approvals, credential signings, and seal anchoring without changing the key state
- Rotation events replace the current signing keys with the pre-committed rotation keys and simultaneously establish new pre-committed keys for the next rotation
- A Controller is the entity responsible for authorizing all key events for an AID, managing the private keys and determining when rotation occurs

## Rules & Constraints

- Key pairs must be generated with approximately 128 bits of cryptographic strength using approved algorithms
- All key-pair creation and storage must occur within protected infrastructure, preferably within a Trusted Execution Environment (TEE) or Hardware Security Module (HSM)
- Prophylactic key rotation must be performed on unpredictable schedules to limit the window of exposure from any undetected compromise
- Mandatory rotation is required immediately upon any indication of possible key compromise
- QVI rotation events occurring less than six months after the previous rotation require approval from GLEIF External GARs
- Key compromise must be reported to GLEIF within 24 hours, followed by a recovery rotation event that forks the KEL and a published key recovery explanation
- Pre-rotation applies only to transferable AIDs; non-transferable AIDs use replacement rather than rotation

## Examples

- **Inception Event**: When GLEIF creates the Root AID, it generates an inception event specifying the initial signing keys, pre-committed rotation keys, weighted multi-sig thresholds, and the designated witness pool
- **Scheduled Key Rotation**: A QVI performs a prophylactic rotation event, replacing current signing keys with pre-committed keys, establishing new pre-committed keys, and having the event endorsed by its witness pool
- **Interaction Event**: A QVI anchors a credential issuance seal in an interaction event in its KEL, recording the issuance without changing the AID's key state
- **Key Compromise Recovery**: Upon detecting a compromised private key, a QVI immediately performs a recovery rotation, forks the KEL at the point of compromise, reports to GLEIF, and publishes an explanation of the recovery event

## Disambiguation

> **Key Management** vs **Security Infrastructure**: Key Management covers the policies, events, and logs governing key lifecycle (creation, rotation, inception, interaction). Security Infrastructure covers the protective components (multi-sig groups, HSMs, TEEs, escrow agents) and recovery mechanisms that safeguard those keys and ensure operational continuity.

## Navigation

- **Up**: [KERI Infrastructure](./keri-infrastructure.md)
- **Down**: *(none)*
- **Related**: [Security Infrastructure](./security-infrastructure.md)
