---
id: trust-and-qualification
prefLabel: "Trust and Qualification"
altLabels: ["TAF", "ToIP", "ToIP Foundation", "ToIP Governance Stack", "Trust Assurance Framework", "Trust over IP", "Trust over IP Foundation", "Trust over IP Governance Stack"]
depth: 0
broader: []
narrower: ["annual-qualification", "identity-verification", "oobi-protocol", "qualification-program", "risk-assessment", "service-level-management", "trustmark"]
related: []
---

# Trust and Qualification

## Definition

Trust and Qualification is the top-level domain within the vLEI Ecosystem covering trust establishment, assurance mechanisms, and the qualification of organizations seeking to participate as credential issuers. It encompasses the Trust over IP (ToIP) governance architecture upon which the vLEI Ecosystem Governance Framework is built as a Layer Four framework, the Trust Assurance Framework (TAF) that maps governance requirements to specification, conformance, and performance assurance dimensions, the vLEI Issuer Qualification Program for initial and ongoing evaluation, identity verification processes, risk assessment, and service level management. This domain defines how trust is created, maintained, and verified throughout the ecosystem.

## Key Facts

- The vLEI EGF is built as a Layer Four Ecosystem Governance Framework within the Trust over IP Foundation's layered governance stack, which also includes Ecosystem, Credential, Provider, and Utility layers
- The Trust Assurance Framework maps every governance and technical requirement to three assurance dimensions: Specification Assurance (documented requirements), Conformance Assurance (evaluation processes), and Performance Assurance (technical enforcement)
- The ToIP Governance Stack categorizes risks across four layers (Ecosystem, Credential, Provider, Utility) and six trust areas (Governance, Availability, Security, Privacy, Confidentiality, Processing Integrity)
- Trust establishment in the ecosystem begins with GLEIF as the organizational and cryptographic root of trust, combining LEI governance with KERI-based verification
- The qualification pipeline moves organizations from Candidate vLEI Issuer through initial qualification, Annual vLEI Issuer Qualification, and potentially Extraordinary Qualification
- Identity verification spans two complementary processes: Identity Assurance (verifying real-world identity) and Identity Authentication (cryptographic proof of AID control)

## Rules & Constraints

- All Qualified vLEI Issuers must complete the vLEI Issuer Qualification Program before they can issue any vLEI Credentials
- Annual qualification must be conducted on or after the anniversary date of initial qualification
- Extraordinary qualification may be triggered at any time if GLEIF has reason to believe documentation is no longer current
- Identity verification must be performed before every vLEI Credential issuance, following the specific steps defined in each credential framework
- Only digital identity schemes at High or Substantial Level of Assurance are accepted for identity assurance
- Service level targets, breach handling, and escalation management are formally defined through the QVI Service Level Agreement

## Examples

- **Trust Assurance Framework mapping**: A governance requirement for QVI key management is mapped across all three dimensions -- documented in the Technical Requirements (Specification), evaluated during annual qualification (Conformance), and enforced through KERI multi-sig requirements (Performance)
- **ToIP Layer Four framework**: The vLEI EGF sits at Layer Four (Ecosystem Governance) of the ToIP stack, with KERI at the Utility layer, ACDC at the Credential layer, and QVIs at the Provider layer
- **Initial qualification pipeline**: An organization applies as a Candidate vLEI Issuer, completes the self-assessment checklist, undergoes GLEIF evaluation, and upon passing receives its QVI vLEI Credential

## Navigation

- **Up**: *(top-level concept)*
- **Down**: [Annual vLEI Issuer Qualification](./annual-qualification.md), [Identity Verification](./identity-verification.md), [Out-of-Band Introduction](./oobi-protocol.md), [vLEI Issuer Qualification Program](./qualification-program.md), [Risk Assessment](./risk-assessment.md), [Service Level Management](./service-level-management.md), [TrustMark](./trustmark.md)
- **Related**: *(none)*
