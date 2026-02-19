---
id: assurance-dimensions
prefLabel: "Assurance Dimensions"
altLabels: ["Conformance Assurance", "Performance Assurance", "Specification Assurance"]
depth: 2
broader: ["annual-qualification"]
narrower: []
related: []
---

# Assurance Dimensions

## Definition

The Assurance Dimensions are the three complementary mechanisms within the Trust Assurance Framework that collectively ensure vLEI Ecosystem requirements are properly established, verified, and enforced. Specification Assurance ensures that requirements are formally documented in credential frameworks and governance documents. Conformance Assurance confirms that participants comply with those requirements through evaluation processes such as the Annual vLEI Issuer Qualification. Performance Assurance enforces requirements through the technical architecture itself, particularly KERI key management and GLEIF-supplied vLEI software, making non-compliance technically difficult or impossible.

## Key Facts

- The Trust Assurance Framework maps every governance, operational, and technical requirement to at least one of the three assurance dimensions, creating a comprehensive assurance matrix
- Specification Assurance is achieved through the controlled document hierarchy of the EGF, where each credential framework and technical requirements document formally specifies the rules participants must follow
- Conformance Assurance relies primarily on the qualification program (initial and annual) and GLEIF's verification and audit rights, providing human-evaluated compliance checks
- Performance Assurance leverages the inherent properties of KERI (cryptographic self-certification, pre-rotation, delegation) and vLEI software to make certain violations technically impossible rather than merely prohibited
- The three dimensions form a defense-in-depth model: even if one dimension fails (e.g., a specification is ambiguous), the other two provide compensating controls
- Performance Assurance is the strongest form because it is enforced by the technology stack itself, not by policy or audit alone

## Rules & Constraints

- All EGF requirements must be mapped to at least one assurance dimension; unmapped requirements represent governance gaps
- Specification Assurance documents must be maintained as controlled documents subject to the EGF change management process
- Conformance Assurance evaluations must be conducted at least annually through the Annual vLEI Issuer Qualification process
- Performance Assurance mechanisms must be implemented in GLEIF-supplied vLEI software, which QVIs are required to install and operate
- If a requirement cannot be enforced through Performance Assurance, it must have compensating controls through both Specification and Conformance Assurance

## Examples

- **Specification Assurance**: The Legal Entity vLEI Credential Framework formally specifies that identity assurance must reach at least IAL2 (NIST 800-63A) before credential issuance, documenting the requirement in a controlled document
- **Conformance Assurance**: During annual qualification, GLEIF evaluates whether a QVI has been conducting IAL2 identity verification by reviewing the QVI's records, procedures, and audit reports
- **Performance Assurance**: KERI's multi-signature requirement for QVI credential issuance technically prevents a single QAR from issuing credentials alone, enforcing the dual-QAR workflow through cryptographic thresholds rather than policy alone

## Disambiguation

> **Assurance Dimensions** vs **Trust Areas (Risk Assessment)**: Assurance Dimensions describe how requirements are ensured (specification, conformance, performance), while Trust Areas classify what aspect of trust is at risk (Governance, Availability, Security, Privacy, Confidentiality, Processing Integrity). Dimensions are mechanisms of assurance; Trust Areas are categories of risk.

## Navigation

- **Up**: [Annual vLEI Issuer Qualification](./annual-qualification.md)
- **Down**: *(none)*
- **Related**: *(none)*
