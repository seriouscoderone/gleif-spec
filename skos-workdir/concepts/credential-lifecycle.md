---
id: credential-lifecycle
prefLabel: "Credential Lifecycle"
altLabels: ["Active Status", "Grace Period", "Involuntary Revocation", "Issuance Compliance", "LEI Entity Status", "LEI Registration Status", "Voluntary Revocation", "vLEI Issuance", "vLEI Maintenance", "vLEI Revocation"]
depth: 1
broader: ["vlei-credentials"]
narrower: []
related: ["identity-verification", "vlei-reporting-api"]
---

# Credential Lifecycle

## Definition

The Credential Lifecycle covers the full span of a vLEI Credential from issuance through maintenance to revocation. Issuance requires successful Identity Assurance and Identity Authentication of the relevant parties, plus verification that the underlying LEI has Active entity status and a valid registration status in the Global LEI System. Maintenance ensures these conditions remain true on an ongoing basis. Revocation may be voluntary (initiated by the holder or their authorized representative) or involuntary (initiated by the issuer or GLEIF due to non-compliance, LEI status changes, or governance violations).

## Key Facts

- The LEI Entity Status must be Active and the LEI Registration Status must be Issued, Pending Transfer, or Pending Archival for a vLEI Credential to be issued or maintained; any other status triggers revocation
- Revocation of a QVI vLEI Credential initiates a grace period of up to 90 days, during which GLEIF manages the transition of affected Legal Entities to new Qualified vLEI Issuers
- During the grace period following QVI credential revocation, no further issuance, verification, or revocation of vLEIs by that QVI is permitted
- Voluntary revocation is typically initiated when a person leaves an official organizational role or an engagement context ends
- Involuntary revocation is triggered when a Legal Entity's LEI lapses, when a QVI fails annual qualification, or when governance framework violations are detected
- QVIs must report every issuance and revocation event to GLEIF through the vLEI Reporting API, enabling GLEIF to update public LEI pages on gleif.org

## Rules & Constraints

- If the LEI Entity Status changes from Active to any other value, the Qualified vLEI Issuer must initiate involuntary revocation of the affected credentials
- If the LEI Registration Status changes to Lapsed or Retired, credential maintenance fails and revocation is required
- Identity verification must be completed before any credential issuance; the specific requirements vary by credential type and are defined in the applicable vLEI Credential Governance Framework
- Revocation of a Legal Entity vLEI Credential cascades to all OOR and ECR credentials chained from it
- QVIs must maintain Revocation Logs that are transferred to GLEIF upon QVI termination to ensure continuity of status information
- Credential wallets and private keys must be kept secure throughout the maintenance phase

## Examples

- **Standard Issuance**: A QVI completes identity verification of a Legal Entity's DAR and LARs, confirms the entity's LEI is Active with Issued registration status, and issues a Legal Entity vLEI Credential
- **Voluntary Revocation**: A company's CFO resigns; the LAR requests the QVI to revoke the former CFO's OOR vLEI Credential
- **Involuntary Revocation (LEI Lapse)**: A Legal Entity fails to renew its LEI registration; the status changes to Lapsed, triggering the QVI to revoke all associated vLEI Credentials
- **QVI Termination Grace Period**: GLEIF revokes a QVI's credential due to failed annual qualification; a 90-day grace period begins during which GLEIF coordinates transition of affected entities

## Disambiguation

> **Credential Lifecycle** vs **Credential Exchange**: Lifecycle governs when and how credentials come into existence, remain valid, and are terminated. Exchange governs how existing valid credentials are presented to and verified by third parties.

> **Voluntary Revocation** vs **Involuntary Revocation**: Voluntary revocation is requested by the credential holder or their LAR (e.g., role change). Involuntary revocation is imposed by the QVI or GLEIF without the holder's request (e.g., compliance failure).

## Navigation

- **Up**: [vLEI Credentials](./vlei-credentials.md)
- **Down**: *(none)*
- **Related**: [Identity Verification](./identity-verification.md), [vLEI Reporting API](./vlei-reporting-api.md)
