---
id: risk-assessment
prefLabel: "Risk Assessment"
altLabels: ["Credential Registry Risk", "GLEIF Credential Registry Risk", "GLEIF Risk", "Governing Authority Risk", "QVI Risk", "Qualified vLEI Issuer Risk", "Risk Treatment", "Trust Area", "Utility Risk", "Verifier Risk"]
depth: 1
broader: ["trust-and-qualification"]
narrower: []
related: ["security-infrastructure", "vlei-ecosystem-information-trust-policies"]
---

# Risk Assessment

## Definition

The vLEI Risk Assessment is a structured framework for identifying, categorizing, and treating risks across the vLEI Ecosystem. It organizes risks along two dimensions: the Trust over IP governance stack layers (Ecosystem, Credential, Provider, Utility) and six trust areas (Governance, Availability, Security, Privacy, Confidentiality, Processing Integrity). The assessment covers five principal risk categories -- Governing Authority (GLEIF), Qualified vLEI Issuer, Verifier, GLEIF Credential Registry, and Utility -- with treatment recommendations of Mitigation, Avoidance, Transference, Acceptance, or Other for each identified risk.

## Key Facts

- Governing Authority risks address GLEIF's competence, policy consistency, accountability, legal enforceability of ACDCs, and ecosystem acceptance -- risks that could undermine the entire trust foundation
- QVI risks focus on credential issuance without appropriate verification, credential invalidity, operational unavailability, and use of obsolete software
- Verifier risks cover inconsistent verification practices, incomplete proof request formats, acceptance of revoked vLEIs, man-in-the-middle attacks, and network unavailability
- GLEIF Credential Registry risks address competence, availability, access control, unauthorized writes, data breaches, and exploited use of stolen vLEIs
- Utility risks target the KERI infrastructure and vLEI software layer, including undetected bugs, inadequate key protection, and failure to follow code delivery best practices; these can cascade to affect all higher governance layers
- The six trust areas map directly to standard information trust principles, providing a systematic classification that aligns with established security and governance frameworks

## Rules & Constraints

- Each identified risk must be classified by both its governance layer and its affected trust area
- Risk treatments must specify one of five actions: Mitigation, Avoidance, Transference, Acceptance, or Other
- Utility layer risks can propagate upward to affect the Credential, Provider, and Ecosystem layers, requiring special attention to cascading effects
- The risk assessment must be maintained as a living controlled document, updated as the ecosystem evolves and new risks emerge
- Risk treatments inform the requirements specified in the Information Trust Policies and technical requirements documents

## Examples

- **Governing Authority Risk -- Legal Enforceability**: The risk that ACDCs issued within the vLEI Ecosystem may not be recognized as legally enforceable in certain jurisdictions, treated through governance advocacy and jurisdictional analysis
- **QVI Risk -- Issuance Without Verification**: The risk that a QVI issues credentials without completing proper identity assurance, treated through the multi-QAR workflow requirement and annual qualification audits
- **Utility Risk -- Undetected Software Bugs**: The risk that KERI or vLEI software contains exploitable vulnerabilities, treated through open-source development, the Developer Security Policy, and GLEIF-provided software upgrades
- **Verifier Risk -- Revoked Credential Acceptance**: The risk that a verifier accepts a credential that has already been revoked, treated through real-time Transaction Event Log checking and watcher network verification

## Navigation

- **Up**: [Trust and Qualification](./trust-and-qualification.md)
- **Down**: *(none)*
- **Related**: [Security Infrastructure](./security-infrastructure.md), [Information Trust Policies](./vlei-ecosystem-information-trust-policies.md)
