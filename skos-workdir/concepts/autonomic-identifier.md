---
id: autonomic-identifier
prefLabel: "Autonomic Identifier"
altLabels: ["AID", "DID Method", "Delegated AID", "Ephemeral AID", "Non-Transferable AID", "Transferable AID", "did:keri"]
depth: 1
broader: ["keri-infrastructure"]
narrower: []
related: ["credential-chain"]
---

# Autonomic Identifier

## Definition

An Autonomic Identifier (AID) is a self-certifying identifier managed via the KERI protocol that is imbued with self-management capabilities, meaning the identifier itself cryptographically proves control without reliance on any external authority. AIDs exist in two main classes: transferable AIDs that support key rotation through pre-rotation for long-term persistent use, and non-transferable (ephemeral) AIDs whose key pairs cannot be rotated and must be abandoned upon compromise. The vLEI Ecosystem also supports delegated AIDs authorized through cooperative cryptographic commitment between a delegator and delegatee, and DID method resolution via did:keri.

## Key Facts

- Transferable AIDs maintain two sets of key pairs at all times: the current signing keys and a pre-committed set of one-time rotation keys that become the next signing keys after rotation
- Non-transferable AIDs are used for infrastructure components like witnesses, which are identified by their non-transferable AIDs rather than network addresses
- Delegated AIDs are anchored in the Key Event Log of the delegator, requiring cooperative verified signatures from both parties for creation and any subsequent key operations
- The GLEIF Root AID sits at the apex of the vLEI delegation tree; it delegates to the GIDA (internal operations) and GEDA (external credential issuance), which in turn delegate to QVI AIDs
- AIDs can be resolved through the did:keri DID method, bridging KERI identifiers into the broader W3C Decentralized Identifier ecosystem
- Every AID must be generated from a random number seed large enough to provide approximately 128 bits of cryptographic security for its branch of the trust tree

## Rules & Constraints

- A transferable AID must have pre-committed rotation keys established at inception; without them, the identifier cannot be rotated and is effectively non-transferable
- Delegated AID creation requires both the delegator's approval (via an anchoring seal) and the delegatee's inception event, ensuring neither party can act unilaterally
- Non-transferable AIDs cannot recover from key compromise; they must be replaced with a new AID if compromise is suspected
- All AIDs used by GLEIF, QVIs, and Legal Entities in the vLEI credential chain must be transferable AIDs to support ongoing key management
- If a QVI's delegated AID requires rotation less than six months after the previous rotation, the QVI must contact GLEIF External GARs for approval

## Examples

- **GLEIF Root AID**: A transferable, multi-signature AID at the top of the delegation hierarchy, created through a threshold multisig inception event with weighted participant signatures
- **QVI Delegated AID**: A transferable AID delegated from the GLEIF External Delegated AID, enabling a Qualified vLEI Issuer to issue credentials under GLEIF's authority
- **Witness AID**: A non-transferable AID identifying a specific witness node in a witness pool; if the witness key is compromised, the AID is abandoned and a new witness is established
- **Legal Entity AID**: A transferable AID controlled by a Legal Entity's authorized representatives (LARs) operating in a multi-signature group, used to hold and manage the entity's vLEI credentials

## Disambiguation

> **Autonomic Identifier (AID)** vs **Legal Entity Identifier (LEI)**: An AID is a cryptographic self-certifying identifier managed through KERI key events. An LEI is a standardized registration identifier (ISO 17442) in the Global LEI System. In the vLEI Ecosystem, a Legal Entity vLEI Credential binds an entity's LEI to its AID, linking organizational identity to cryptographic control.

## Navigation

- **Up**: [KERI Infrastructure](./keri-infrastructure.md)
- **Down**: *(none)*
- **Related**: [Credential Chain](./credential-chain.md)
