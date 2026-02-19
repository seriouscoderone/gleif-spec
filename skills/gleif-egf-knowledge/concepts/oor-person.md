---
id: oor-person
prefLabel: "OOR Person"
altLabels: ["ISO 5009", "ISO 5009 Official Organization Role Lists", "OOR", "OOR Person Consent", "Official Organizational Role", "Official Organizational Role Person"]
depth: 1
broader: ["roles-and-representatives"]
narrower: []
related: ["oor-vlei-credential"]
---

# OOR Person

## Definition

An OOR Person (Official Organizational Role Person) is a natural person who holds a formally recognized official organizational role at a Legal Entity, such as a position defined in the ISO 5009 standard for official organization role lists (for example, Chief Executive Officer, Chief Financial Officer, or Board Director). Before an OOR vLEI Credential can be issued, the person's identity and their role at the Legal Entity must be verified against official public sources, business registry documents, or certified entity documentation. The OOR Person must also provide explicit consent for public disclosure of their role on the GLEIF LEI page.

## Key Facts

- OOR Persons hold roles that must be validated against external official sources, not merely asserted by the Legal Entity -- this is the key distinction from ECR Persons
- ISO 5009 provides the standardized list of official organizational roles recognized in the vLEI Ecosystem, covering positions such as CEO, CFO, Board Chair, and similar formal titles
- The OOR Person must give explicit consent before their name and role information are published on the GLEIF LEI page for the Legal Entity
- Identity assurance for OOR Persons requires at least IAL2 (NIST 800-63A) verification or an approved digital identity scheme at High or Substantial Level of Assurance
- The credential chain for an OOR vLEI Credential involves both a QVI OOR Authorization credential (from the LAR) and an OOR Authorization credential (from the QVI), ensuring dual authorization
- Revocation of an OOR vLEI Credential may be voluntary (the person leaves the role) or involuntary (the entity's LEI status changes or governance violations occur)

## Rules & Constraints

- The role must be verifiable through official public sources, business registry documents, or certified entity documentation -- informal or self-declared roles do not qualify
- A QVI must verify the OOR Person's identity through a real-time OOBI session with audio and video, including a challenge-response cryptographic authentication
- The OOR Person's explicit consent for public disclosure must be obtained before credential issuance and recorded
- If the OOR Person leaves the official role, the Legal Entity must initiate voluntary revocation through a LAR
- OOR vLEI Credentials are reported by the QVI to GLEIF through the vLEI Reporting API and appear on the LEI page of the Legal Entity

## Examples

- **Chief Executive Officer**: The CEO of a multinational bank is verified as an OOR Person and issued an OOR vLEI Credential referencing the ISO 5009 role, enabling verifiable digital signing on behalf of the entity
- **Board Director**: A newly appointed board member undergoes identity assurance and OOBI authentication, then receives an OOR vLEI Credential linked to the Legal Entity vLEI Credential
- **Chief Compliance Officer**: A regulated financial institution's compliance head is issued an OOR vLEI Credential to enable counterparties to cryptographically verify their authority

## Disambiguation

> **OOR Person** vs **ECR Person**: An OOR Person holds an official organizational role validated against external public sources and ISO 5009 role lists. An ECR Person holds an engagement context role defined by the Legal Entity itself, which does not require validation against public registries. OOR roles are formal and externally verifiable; ECR roles are flexible and entity-defined.

## Navigation

- **Up**: [Roles and Representatives](./roles-and-representatives.md)
- **Down**: *(none)*
- **Related**: [OOR vLEI Credential](./oor-vlei-credential.md)
