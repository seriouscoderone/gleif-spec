---
id: security-infrastructure
prefLabel: "Security Infrastructure"
altLabels: ["Continuity Policy", "Cryptographic Root of Trust", "Escrow Agent", "HSM", "Hardware Security Module", "Key Compromise Recovery", "MFA", "Multi-Sig Group", "Multi-Signature Group", "Multi-Signature Scheme", "Multi-factor Authentication", "Multi-sig", "Multi-sig Group", "Multi-signature Group", "Multisig", "Private Key Compromise", "Private Key Store", "Signature Verification Infrastructure", "Signing Threshold", "TEE", "Threshold Multisig", "Thresholded Multi-Signature", "Trusted Execution Environment", "Weighted Multi-Sig"]
depth: 1
broader: ["keri-infrastructure"]
narrower: []
related: ["key-management", "oobi-protocol", "risk-assessment"]
---

# Security Infrastructure

## Definition

Security Infrastructure encompasses the protective components and operational security mechanisms within the KERI infrastructure that safeguard cryptographic keys, ensure operational continuity, and enable recovery from compromise. This includes multi-signature schemes with weighted thresholds for group-controlled identifiers, Trusted Execution Environments (TEEs) and Hardware Security Modules (HSMs) for isolating private key operations, private key stores, escrow agents for key recovery scenarios, continuity policies for maintaining control authority, and comprehensive mechanisms for detecting and recovering from private key compromise.

## Key Facts

- Multi-signature groups use weighted threshold schemes where each participant AID receives a fractional weight, and the combined weights of signers must meet or exceed the threshold for both current and next (pre-committed) key sets
- The GLEIF Root AID uses a weighted multi-sig scheme with an escrow agent as a secondary signer who can act if the required threshold of primary GLEIF signers is unavailable for rotation or recovery
- Trusted Execution Environments protect key-pair creation, storage, signature creation, and signature verification from observation or capture of private keys
- HSMs are dedicated physical devices recommended specifically for encryption key storage in Witness and Watcher services
- Private key compromise of one wallet in a multi-sig group does not result in loss of identifier control, because the attacker would still need to compromise enough additional wallets to meet the signing threshold
- The Cryptographic Root of Trust principle requires that all AIDs be generated from random seeds large enough to provide adequate cryptographic security for their branch of the trust tree
- A single-signer threshold (non-multi-sig) applies only to sole-employee entities within the vLEI Ecosystem

## Rules & Constraints

- GLEIF must maintain a Continuity Policy for the survival of control authority of all Controllers for the GLEIF Root AID and its Delegated AIDs, including provisions for escrow agents
- QVIs and Legal Entities should maintain Continuity Policies for their own Controllers
- Key compromise must be reported to GLEIF within 24 hours, followed by a recovery rotation event that forks the Key Event Log
- After key compromise recovery, the QVI must investigate the source of compromise and publish a key recovery event explanation
- Signature verification infrastructure must be protected by watcher pool mechanisms where events are only accepted as verified if a sufficient majority of watchers agree
- Multi-factor authentication is required during OOBI sessions and key management ceremonies
- All signature creation infrastructure should operate within a TEE to prevent observation of private keys during signing operations

## Examples

- **GLEIF Root AID Multi-Sig**: The GLEIF Root AID is controlled by a weighted multi-signature group of GLEIF Authorized Representatives, with an escrow agent as a fallback signer in case primary signers become unavailable
- **TEE-Protected Key Operations**: A QVI's signature creation infrastructure runs inside a TEE, ensuring that private keys are never exposed to the host operating system during credential signing operations
- **HSM for Witness Keys**: A GLEIF witness node stores its encryption keys in a dedicated HSM, providing hardware-level isolation against software-based key extraction attacks
- **Key Compromise Recovery**: Upon detecting a compromised signing key, a QVI performs a recovery rotation event within 24 hours, forks the KEL to invalidate the compromised branch, and publishes an explanation of the recovery

## Disambiguation

> **Security Infrastructure** vs **Key Management**: Security Infrastructure provides the protective mechanisms (multi-sig, TEEs, HSMs, escrow, continuity policies) that safeguard cryptographic operations. Key Management covers the policies and event lifecycle (inception, rotation, interaction) that govern how keys are created, used, and retired.

## Navigation

- **Up**: [KERI Infrastructure](./keri-infrastructure.md)
- **Down**: *(none)*
- **Related**: [Key Management](./key-management.md), [Out-of-Band Introduction](./oobi-protocol.md), [Risk Assessment](./risk-assessment.md)
