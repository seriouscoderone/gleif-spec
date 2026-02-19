---
id: cryptographic-primitives
prefLabel: "Cryptographic Primitives"
altLabels: ["CESR", "Composable Event Streaming Representation", "DHT", "Distributed Hash Table", "SAID", "Seal", "Self-Addressing Identifier"]
depth: 1
broader: ["keri-infrastructure"]
narrower: []
related: ["acdc"]
---

# Cryptographic Primitives

## Definition

Cryptographic Primitives are the foundational cryptographic data structures and encoding formats that underpin the vLEI Ecosystem's trust infrastructure. They include Composable Event Streaming Representation (CESR) for universal text-binary encoding, Self-Addressing Identifiers (SAIDs) for content-based tamper-evident identification, cryptographic seals for anchoring arbitrary data to key events, and distributed hash tables (DHTs) for AID discovery. These primitives collectively enable the immutability, verifiability, and composability guarantees that KERI and ACDC credentials depend on.

## Key Facts

- CESR provides a unique property of text-binary concatenation composability, meaning CESR-encoded data can be freely concatenated in either text or binary form and converted between the two without loss of information
- SAIDs are deterministically generated from and embedded within the content they identify, making both the identifier and its data mutually tamper-evident through cryptographic binding
- Cryptographic seals anchor arbitrary data to a specific event in a key event sequence using either a cryptographic digest or a Merkle root (hash tree root), enabling verifiable timestamping of external data
- All vLEI credentials must use CESR as their proof format, and every credential schema must include a SAID for immutability verification
- DHTs implement an associative array mapping keys to values, used within the ecosystem specifically for the discovery of Autonomic Identifiers and their service endpoints
- Key pairs in the ecosystem must provide approximately 128 bits of cryptographic strength, with Ed25519 as the specified signature algorithm

## Rules & Constraints

- Every ACDC credential must include a SAID in its schema definition to ensure that any modification to the credential content is detectable
- CESR encoding must be used for all digital signatures, SAIDs, and proof format representations within vLEI protocol messages
- Seals must reference a specific event in the key event log, creating an immutable temporal anchor point
- Schema SAIDs follow semantic versioning conventions, ensuring that schema updates are tracked and verifiable through the vLEI Credential Schema Registry maintained by GLEIF
- SAIDs do not function as network addresses or locators; they are strictly content-based identifiers used for verification purposes

## Examples

- **SAID in a Credential Schema**: Each vLEI credential schema (e.g., the QVI vLEI Credential schema) contains a SAID that uniquely identifies that exact version of the schema; any alteration to the schema fields would produce a different SAID, immediately revealing tampering
- **CESR-Encoded Signature**: An Ed25519 digital signature on a key event is encoded in CESR format, allowing it to be transmitted in either text (Base64-like) or binary form while remaining composable with other protocol elements
- **Seal Anchoring**: When a QVI issues a credential, a cryptographic seal containing the credential's SAID is anchored in an interaction event in the issuer's key event log, binding the issuance to a verifiable point in the log
- **DHT for AID Discovery**: A verifier looking up a Legal Entity's AID can query a distributed hash table to locate the service endpoints and witness information needed to resolve that identifier

## Disambiguation

> **Cryptographic Primitives** vs **Security Infrastructure**: Cryptographic Primitives are the data structures and encoding formats (CESR, SAIDs, seals) used to represent and verify data. Security Infrastructure covers the operational security components (multi-sig groups, HSMs, TEEs, key compromise recovery) that protect and manage the use of those primitives.

## Navigation

- **Up**: [KERI Infrastructure](./keri-infrastructure.md)
- **Down**: *(none)*
- **Related**: [Authentic Chained Data Container](./acdc.md)
