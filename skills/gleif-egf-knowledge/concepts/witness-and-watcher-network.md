---
id: witness-and-watcher-network
prefLabel: "Witness and Watcher Networks"
altLabels: ["Backer", "Endorser", "GLEIF Watcher Network", "GLEIF Witness Network", "KAWA", "KERI Algorithm for Witness Agreement", "KERI Watcher", "KERI Witness", "Ledger Registrar", "Registrar", "Watcher", "Witness", "Witness Pool"]
depth: 1
broader: ["keri-infrastructure"]
narrower: []
related: []
---

# Witness and Watcher Networks

## Definition

Witness and Watcher Networks are the decentralized verification infrastructure in KERI that provides secondary roots of trust for key event integrity. Witness pools are groups of nodes designated by a Controller to endorse key events using the KERI Algorithm for Witness Agreement (KAWA), creating receipts that establish consensus on the authoritative key state. Watcher networks independently verify signature status of key events to protect validators from attacks, forming a threshold structure where an attacker must compromise a sufficient number of watchers for a successful attack. The infrastructure also includes Registrar backers that provide ledger-based secondary roots of trust. GLEIF operates its own dedicated Witness and Watcher networks for the vLEI Ecosystem.

## Key Facts

- Witness pools require a minimum of five witness nodes, each identified by a non-transferable AID, to provide adequate redundancy and fault tolerance
- KAWA (KERI Algorithm for Witness Agreement) requires a sufficient majority threshold of witnesses to agree before a key event is considered endorsed, preventing any single witness from unilaterally validating events
- Witnesses are designated by the Controller of an identifier and are authorized to verify, sign, and keep events associated with that identifier, effectively acting as endorsers
- Watchers are not designated by the Controller; they independently keep copies of Key Event Receipt Logs and verify signatures, providing a detection layer against duplicitous key events
- Endorsers serve as secondary roots of trust for Key Event Logs, with two types supported: Witnesses (non-ledger based) and Registrars (ledger-based using a GLEIF-approved DID method)
- GLEIF operates dedicated Witness and Watcher networks as part of the vLEI infrastructure, providing ecosystem-wide verification services
- Hardware Security Modules (HSMs) are recommended for encryption key storage in Witness and Watcher services

## Rules & Constraints

- Witnesses do not have signing authority over credentials; they only attest to the receipt of key events and endorse the event sequence
- A sufficient majority of witnesses must agree through KAWA before an event is accepted as authoritative
- Witness pools must maintain a minimum of five nodes to meet the vLEI technical requirements
- Watchers only verify; they do not perform issuance or endorsement of events
- Registrar backers must use a GLEIF-approved DID method for their ledger-based secondary root of trust
- An event is only accepted as verified by the signature verification infrastructure if a sufficient majority of watchers agree on the verification status

## Examples

- **GLEIF Root AID Witness Pool**: The GLEIF Root AID inception event requires at least three witnesses from GLEIF's dedicated witness network to endorse the creation of the root identifier
- **QVI Key Event Endorsement**: When a Qualified vLEI Issuer performs a key rotation, the rotation event is sent to its designated witness pool, which endorses the event through KAWA consensus before the rotation is considered authoritative
- **Watcher-Based Attack Detection**: If an attacker attempts to present a forged key event to a verifier, the verifier's watcher network independently checks the event against its copies of the Key Event Receipt Log, detecting the inconsistency
- **Ledger Registrar**: A registrar backer records key event anchors on a distributed ledger using a GLEIF-approved DID method, providing an additional independent root of trust alongside the witness pool

## Disambiguation

> **Witness** vs **Watcher**: A Witness is designated by the Controller to endorse key events and forms part of the authoritative consensus mechanism (KAWA). A Watcher is not designated by the Controller but independently monitors and verifies key events to protect validators. Witnesses produce receipts; Watchers detect inconsistencies.

## Navigation

- **Up**: [KERI Infrastructure](./keri-infrastructure.md)
- **Down**: *(none)*
- **Related**: *(none)*
