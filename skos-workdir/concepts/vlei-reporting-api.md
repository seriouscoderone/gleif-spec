---
id: vlei-reporting-api
prefLabel: "vLEI Reporting API"
altLabels: ["LEI Page"]
depth: 2
broader: ["gleif"]
narrower: []
related: ["credential-lifecycle"]
---

# vLEI Reporting API

## Definition

The vLEI Reporting API is an interface provided by GLEIF through which Qualified vLEI Issuers must report each issuance and revocation event of vLEI Credentials. This reporting enables GLEIF to maintain accurate public records on LEI pages hosted on gleif.org, where entity LEI information is displayed alongside associated vLEI Credential details. The API serves as the bridge between the decentralized credential operations performed by QVIs and GLEIF's centralized public information repository.

## Key Facts

- QVIs are contractually obligated to report every credential issuance and revocation event through the API, making it a mandatory operational integration point
- The LEI page on gleif.org is the publicly accessible display for each Legal Entity, showing its LEI information and associated vLEI Credential details updated through reported events
- The LEI page is an informational display that reflects reported credential status; it does not serve as the authoritative source for credential verification, which relies on cryptographic verification through KERI
- OOR Person consent for public disclosure on the GLEIF LEI page is required before an OOR vLEI Credential's details can be displayed
- The API enables GLEIF to maintain ecosystem-wide visibility into credential activity without directly participating in each issuance or revocation event
- Reporting through the API supports the vLEI Data Challenge mechanism, as publicly displayed credential information can be challenged by the public or GLEIF

## Rules & Constraints

- QVIs must report all issuance events through the API before the credential is considered fully processed within the ecosystem's public records
- QVIs must report all revocation events (both voluntary and involuntary) through the API to ensure public records remain current
- The API does not replace cryptographic verification; verifiers must still use KERI infrastructure and Transaction Event Logs for authoritative credential validation
- OOR credential details require explicit person consent before they can be displayed on the LEI page
- Failure to report through the API constitutes a breach of Core Duties under the vLEI Issuer Qualification Agreement

## Examples

- **Issuance Reporting**: A QVI issues a Legal Entity vLEI Credential to a corporation and reports the event through the vLEI Reporting API; GLEIF updates the entity's LEI page to reflect the new credential
- **Revocation Reporting**: A Legal Entity requests voluntary revocation of its vLEI Credential; the QVI processes the revocation in KERI and reports the event through the API, causing the LEI page to reflect the revoked status
- **OOR Credential Display**: After obtaining consent from an OOR Person, the QVI reports the OOR vLEI Credential issuance; the person's official organizational role appears on the Legal Entity's LEI page on gleif.org

## Disambiguation

> **vLEI Reporting API** vs **KERI Transaction Event Log (TEL)**: The Reporting API is GLEIF's centralized endpoint for QVI event reporting that feeds public LEI pages, while the TEL is the decentralized cryptographic log within KERI that serves as the authoritative record for credential status verification. The API provides human-readable public information; the TEL provides machine-verifiable cryptographic proof.

## Navigation

- **Up**: [GLEIF](./gleif.md)
- **Down**: *(none)*
- **Related**: [Credential Lifecycle](./credential-lifecycle.md)
