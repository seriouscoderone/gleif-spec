---
id: keri-infrastructure
prefLabel: "KERI Infrastructure"
altLabels: ["KERI", "Key Event Receipt Infrastructure"]
depth: 0
broader: []
narrower: ["autonomic-identifier", "cryptographic-primitives", "delegation-hierarchy", "key-management", "security-infrastructure", "witness-and-watcher-network"]
related: ["vlei-software"]
---

# KERI Infrastructure

## Definition

Key Event Receipt Infrastructure (KERI) is the decentralized protocol and key management architecture that serves as the technical foundation for the entire vLEI Ecosystem. It provides self-certifying Autonomic Identifiers (AIDs) with pre-rotation key management, witness-based verification of key events, and delegation capabilities that enable the hierarchical trust model linking GLEIF to Qualified vLEI Issuers to Legal Entities. KERI operates independently of any ledger or blockchain, instead relying on key event logs endorsed by witness pools and verified by watcher networks to establish and maintain authoritative key state.

## Key Facts

- KERI is a Layer 1 (utility) protocol in the Trust over IP governance stack, providing the cryptographic foundation upon which all vLEI credentials are built
- The protocol manages authoritative key state through verifiable Key Event Logs (KELs) that record inception, rotation, interaction, and delegation events in an append-only sequence
- KERI uses Composable Event Streaming Representation (CESR) as its encoding format, enabling text-binary concatenation composability across all protocol messages
- Witness pools require a minimum of five witnesses using the KERI Algorithm for Witness Agreement (KAWA) to endorse key events through a sufficient majority threshold
- The infrastructure supports two classes of identifiers: transferable AIDs with pre-rotation for long-term use, and non-transferable (ephemeral) AIDs that are abandoned upon compromise
- KERI does not handle credential issuance or schema definitions directly; those responsibilities belong to the ACDC specification and related credential frameworks

## Rules & Constraints

- All AIDs in the vLEI Ecosystem must be generated from a random number seed providing approximately 128 bits of cryptographic strength
- Key event logs must be endorsed by a sufficient majority of witnesses before events are considered authoritative
- Delegation requires cooperative verified signatures from both the delegator and the delegatee, preventing unilateral delegation
- Qualified vLEI Issuers must report key compromise to GLEIF within 24 hours and perform a recovery rotation event that forks the KEL
- Prophylactic key rotation must occur on unpredictable schedules, with mandatory rotation upon any likelihood of key compromise
- QVI rotation events occurring less than six months from the last rotation require approval from GLEIF External GARs

## Examples

- **GLEIF Root AID**: The top-level identifier in the vLEI delegation hierarchy, created through a threshold multisig inception event with at least three witnesses, from which all authority in the ecosystem flows
- **QVI Delegated AID**: An identifier delegated from the GLEIF External Delegated AID to a Qualified vLEI Issuer, requiring cooperative signatures from both GLEIF and the QVI
- **Key Rotation Event**: When a QVI performs a scheduled key rotation, the pre-committed rotation keys become the new signing keys and new pre-committed keys are established, all recorded in the KEL
- **Witness Endorsement**: A key event submitted by a controller is sent to a witness pool of at least five nodes, which endorse the event using KAWA once a sufficient majority agrees

## Disambiguation

> **KERI Infrastructure** vs **ACDC (Authentic Chained Data Container)**: KERI manages identifiers, keys, and key events at the protocol layer; ACDC defines the credential format, chaining, and disclosure mechanisms that operate on top of KERI. KERI provides the "who" (identifier control), while ACDC provides the "what" (credential content).

## Navigation

- **Up**: *(top-level concept)*
- **Down**: [Autonomic Identifier](./autonomic-identifier.md), [Cryptographic Primitives](./cryptographic-primitives.md), [Delegation Hierarchy](./delegation-hierarchy.md), [Key Management](./key-management.md), [Security Infrastructure](./security-infrastructure.md), [Witness and Watcher Networks](./witness-and-watcher-network.md)
- **Related**: [vLEI Software](./vlei-software.md)
