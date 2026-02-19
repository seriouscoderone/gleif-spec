---
id: gleif
prefLabel: "GLEIF"
altLabels: ["Global Legal Entity Identifier Foundation"]
depth: 1
broader: ["vlei-ecosystem-governance"]
narrower: ["vlei-reporting-api", "vlei-software"]
related: ["delegation-hierarchy"]
---

# GLEIF

## Definition

The Global Legal Entity Identifier Foundation (GLEIF) is a not-for-profit foundation incorporated under Swiss law that operates the Global LEI System and serves as both the Governing Authority and Administering Authority of the vLEI Ecosystem Governance Framework. As Governing Authority, GLEIF sets the policies, rules, and controlled documents that govern the entire vLEI Ecosystem. As Administering Authority, GLEIF directly manages the GLEIF Root AID at the apex of the delegation hierarchy, oversees the qualification and ongoing compliance of Qualified vLEI Issuers, and operates dedicated Witness and Watcher networks for the ecosystem infrastructure.

## Key Facts

- GLEIF holds a dual role unique in the vLEI Ecosystem: it is simultaneously the policy-setting Governing Authority and the operationally active Administering Authority
- GLEIF manages the Root Autonomic Identifier (Root AID) that serves as the single cryptographic root of trust for the entire vLEI delegation tree
- The GLEIF Root AID delegates to two subordinate identifiers: the GIDA for internal operations and the GEDA for issuing QVI credentials and delegating QVI AIDs
- GLEIF operates under the oversight of the Regulatory Oversight Committee (ROC), a committee of global regulators that provides regulatory oversight of the Global LEI System
- GLEIF maintains the vLEI Credential Schema Registry as the authoritative source for all vLEI credential schema definitions
- GLEIF sponsors the open-source vLEI Software that QVIs must install, test, and implement for their ecosystem operations
- The vLEI Reporting API enables QVIs to report credential issuance and revocation events, which GLEIF publishes on LEI pages on gleif.org

## Rules & Constraints

- GLEIF must maintain a Continuity Policy ensuring the survival of control authority for the GLEIF Root AID and all its Delegated AIDs, including escrow agent provisions
- Revisions to the vLEI Issuer Qualification Agreement are reviewed and approved by GLEIF only, without public review
- GLEIF may require QVIs to contract with third-party QVIs for their own credentials after a specified future deadline, limiting QVI self-issuance
- GLEIF retains the right to conduct verification and audits of QVI internal controls and operations at any time
- GLEIF can trigger Extraordinary vLEI Issuer Qualification when it has reason to believe a QVI's documentation is no longer current
- QVIs must report key compromise to GLEIF within 24 hours

## Examples

- **QVI Qualification**: GLEIF evaluates a Candidate vLEI Issuer through the Qualification Program, assessing financial, operational, and IT capabilities before granting QVI status and issuing a QVI vLEI Credential
- **Root AID Management**: GLEIF's Internal GARs manage the Root AID through a weighted multi-signature group with an escrow agent, performing prophylactic key rotations on unpredictable schedules
- **TrustMark Issuance**: Upon successful qualification, GLEIF provides a TrustMark to the QVI for display on its website, subject to specific terms of use and removal upon termination
- **Annual Qualification Review**: On each anniversary date, GLEIF conducts Annual vLEI Issuer Qualification to verify that each QVI continues to meet the EGF requirements

## Disambiguation

> **GLEIF** vs **Qualified vLEI Issuer (QVI)**: GLEIF is the governing and administering authority of the entire ecosystem; it does not directly issue credentials to Legal Entities. QVIs are the operational entities qualified by GLEIF to issue, maintain, and revoke Legal Entity, OOR, and ECR vLEI Credentials.

## Navigation

- **Up**: [vLEI Ecosystem Governance](./vlei-ecosystem-governance.md)
- **Down**: [vLEI Reporting API](./vlei-reporting-api.md), [vLEI Software](./vlei-software.md)
- **Related**: [Delegation Hierarchy](./delegation-hierarchy.md)
