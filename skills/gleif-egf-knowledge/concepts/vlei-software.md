---
id: vlei-software
prefLabel: "vLEI Software"
altLabels: ["GLEIF Supplied vLEI Software"]
depth: 2
broader: ["gleif"]
narrower: []
related: ["keri-infrastructure"]
---

# vLEI Software

## Definition

vLEI Software refers to the open-source software sponsored by GLEIF that provides the operational capabilities required for vLEI Ecosystem participation. It encompasses functionality for vLEI Credential issuance, presentation, identifier and key management, credential revocation, and supporting functions. Qualified vLEI Issuers are required to install, test, and implement this software as part of their vLEI Ecosystem operations, and GLEIF is responsible for providing technical upgrades to maintain security and functionality.

## Key Facts

- The software is open-source, reflecting a transparency-first approach that allows ecosystem participants and the security community to audit the codebase for vulnerabilities
- GLEIF sponsors the software development but distributes it for QVI deployment, creating a centralized development / decentralized deployment model
- The software serves as a key mechanism for Performance Assurance in the Trust Assurance Framework, technically enforcing requirements that might otherwise rely solely on policy compliance
- Utility Risk in the vLEI Risk Assessment specifically addresses threats to the software layer, including undetected bugs, inadequate key protection, and failure to follow code delivery best practices
- The Developer Security Policy requires QVI developers to follow security recommendations from both the W3C Verifiable Credentials specification and the Trust over IP ACDC specification when extending or integrating the software
- QVIs must implement GLEIF-provided software upgrades as part of their obligations under the Qualification Agreement, ensuring consistent software versions across the ecosystem

## Rules & Constraints

- QVIs must install, test, and implement the GLEIF-supplied vLEI Software before operational credential issuance can begin
- GLEIF must provide technical upgrades to maintain the software's security posture and functional capabilities
- QVI developers working with or extending the software must adhere to the Developer Security Policy, including W3C and ToIP ACDC security recommendations
- The software must support all KERI infrastructure operations including AID management, key rotation, witness interactions, and delegation
- The software must support credential operations including issuance, presentation via IPEX, graduated disclosure, and revocation through Transaction Event Logs
- Failure to implement required software upgrades may constitute a breach of the QVI's obligations under the Qualification Agreement

## Examples

- **QVI Deployment**: A Candidate vLEI Issuer completing the qualification process installs and tests the GLEIF-supplied vLEI Software, configuring it for their KERI infrastructure including witness pool connections, key stores, and credential issuance workflows
- **Security Upgrade**: GLEIF releases a software update addressing a discovered vulnerability in the CESR encoding library; all QVIs must implement the upgrade within the timeframe specified in their SLA
- **Credential Issuance**: A QVI uses the software to create a Legal Entity vLEI Credential, signing it with the QVI's delegated AID keys, anchoring it in the Transaction Event Log, and reporting the issuance through the vLEI Reporting API

## Disambiguation

> **vLEI Software** vs **KERI Infrastructure**: vLEI Software is the concrete software implementation that QVIs deploy and operate, while KERI Infrastructure is the protocol specification and architectural design that the software implements. The software is the artifact; KERI is the specification it follows.

## Navigation

- **Up**: [GLEIF](./gleif.md)
- **Down**: *(none)*
- **Related**: [KERI Infrastructure](./keri-infrastructure.md)
