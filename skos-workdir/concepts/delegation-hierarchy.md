---
id: delegation-hierarchy
prefLabel: "Delegation Hierarchy"
altLabels: ["Delegation", "GEDA", "GIDA", "GLEIF External Delegated AID", "GLEIF Identifier Governance Framework", "GLEIF Internal Delegated AID", "GLEIF Root AID", "GLEIF Root Autonomic Identifier", "KERI Delegation", "QVI Delegated AID", "Root AID"]
depth: 1
broader: ["keri-infrastructure"]
narrower: []
related: ["credential-chain", "gleif", "gleif-authorized-representative"]
---

# Delegation Hierarchy

## Definition

The Delegation Hierarchy is the hierarchical AID structure in the vLEI Ecosystem through which GLEIF's root authority flows down to Qualified vLEI Issuers and ultimately to Legal Entities. At the apex sits the GLEIF Root AID, which delegates authority to two subordinate identifiers: the GLEIF Internal Delegated AID (GIDA) for internal ecosystem operations and the GLEIF External Delegated AID (GEDA) for issuing QVI credentials and delegating QVI AIDs. Each delegation in this hierarchy requires cooperative verified signatures from both the delegator and the delegatee, ensuring that no delegation can occur unilaterally. The hierarchy is governed by the GLEIF Identifier Governance Framework.

## Key Facts

- The GLEIF Root AID is created through a threshold multisig inception event requiring at least three witnesses, and it serves as the single root of trust for the entire vLEI delegation tree
- The GIDA (GLEIF Internal Delegated AID) is used for internal GLEIF operations within the vLEI Ecosystem and for participating as a vLEI Holder, with policies identical to the Root AID except with relaxed TEE requirements
- The GEDA (GLEIF External Delegated AID) is the identifier through which GLEIF issues QVI vLEI Credentials and delegates QVI Autonomic Identifiers to Qualified vLEI Issuers
- Delegation is implemented through anchoring seals in the delegator's Key Event Log, creating a cryptographic link between the delegator's key state and the delegatee's inception or rotation event
- A QVI Delegated AID does not exist independently; it requires the cooperative delegation with a cryptographic commitment from both GLEIF (as delegator) and the QVI (as delegatee)
- The hierarchy creates a verifiable chain of authority: GLEIF Root AID delegates to GEDA, which delegates to QVI AIDs, which in turn manage credentials for Legal Entities

## Rules & Constraints

- Every delegation event requires cooperative verified signatures from both the delegator and the delegatee before it is considered valid
- The GLEIF Root AID must use a weighted multi-signature scheme with specified minimum thresholds for both current and next key sets
- QVI Delegated AID rotation events occurring less than six months after the last rotation require prior approval from GLEIF External GARs
- The GLEIF Identifier Governance Framework specifies the purpose, principles, policies, and specifications for the use of the GLEIF Root AID and all Delegated AIDs
- GIDA and GEDA policies mirror the Root AID policies except where explicitly relaxed (e.g., TEE requirements for GIDA)
- Revocation of a QVI's delegated authority invalidates the QVI's ability to issue credentials, triggering downstream effects on all credentials the QVI has issued

## Examples

- **GLEIF Root AID Inception**: GLEIF creates the Root AID through a multi-signature inception event, establishing the weighted threshold group of Internal GARs and the escrow agent, with witness endorsement from the GLEIF witness network
- **GEDA Delegation**: The GLEIF Root AID delegates authority to the GEDA through a cooperative event, where Internal GARs approve the delegation and External GARs create the GEDA inception event, both anchored in the Root AID's KEL
- **QVI AID Delegation**: External GARs use the GEDA to delegate a new AID to an incoming Qualified vLEI Issuer, with the delegation requiring signed commitment from both the GLEIF External GARs and the QVI's Authorized Representatives
- **QVI Rotation with Approval**: A QVI needing to rotate keys within six months of its last rotation contacts GLEIF External GARs, who approve the rotation event before it can be endorsed by the witness pool

## Disambiguation

> **Delegation Hierarchy** vs **Credential Chain**: The Delegation Hierarchy is the AID-level structure where authority flows through KERI delegation events (Root AID to GEDA to QVI AIDs). The Credential Chain is the credential-level structure where trust flows through ACDC source links (QVI Credential to LE Credential to Role Credentials). Both hierarchies are parallel and complementary.

## Navigation

- **Up**: [KERI Infrastructure](./keri-infrastructure.md)
- **Down**: *(none)*
- **Related**: [Credential Chain](./credential-chain.md), [GLEIF](./gleif.md), [GLEIF Authorized Representative](./gleif-authorized-representative.md)
