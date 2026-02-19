---
id: service-level-management
prefLabel: "Service Level Management"
altLabels: ["Appendix 4", "Appendix 5", "Challenge Legal Entity Data", "Communications Portal", "Customer Portal", "Disaster", "Escalation Management", "Incident Management", "Incident Report", "Major Incident", "QVI SLA", "Qualified vLEI Issuer Service Level Agreement", "RTO", "Recovery Time Objective", "SLA", "SLT", "Service Continuity Process", "Service Level Agreement", "Service Level Breach", "Service Level Target", "Service Target", "vLEI Data Challenge", "vLEI Issuer Contact Details"]
depth: 1
broader: ["trust-and-qualification"]
narrower: []
related: ["annual-qualification", "qualified-vlei-issuer"]
---

# Service Level Management

## Definition

Service Level Management is the operational governance framework for the vLEI Ecosystem that defines the service level agreements between GLEIF and Qualified vLEI Issuers (Appendix 5), measurable service level targets, breach handling and escalation procedures, incident management processes, disaster recovery with recovery time objectives, the GLEIF Communications Portal for operational coordination, and the vLEI Data Challenge mechanism for public data quality assurance. It encompasses both GLEIF-provided services and QVI-provided services.

## Key Facts

- The QVI Service Level Agreement (Appendix 5) governs services, service levels, escalation management, incident management, and monitoring obligations for both GLEIF and QVI
- Service Level Targets (SLTs) are specific measurable characteristics such as availability percentages and processing time limits that GLEIF and QVIs commit to achieve
- A Service Level Breach occurs when measured results exceed the respective SLT, automatically triggering the escalation management process
- The vLEI Data Challenge mechanism enables the public or GLEIF to challenge Legal Entity-related data; QVIs must review, research, validate, and respond to challenges within 15 calendar days
- The Communications Portal is a centralized web-based platform provided by GLEIF for information exchange, qualification documentation sharing, contact management, and operational communications with QVIs
- Recovery Time Objectives (RTOs) define the maximum time allowed to resume activities and recover services after a disaster, with disasters defined as situations exceeding GLEIF's ability to respond using its own resources
- Changes to QVI contact details (Appendix 4) do not require prior GLEIF approval, unlike most other operational changes

## Rules & Constraints

- Major incidents require immediate escalation and structured response, typically involving significant service disruption or unauthorized access to vLEI data
- QVIs must maintain documented incident response procedures following ITIL Incident Management guidelines
- Incident Reports must document all details of security incidents and privacy breaches for review by GLEIF
- The Service Continuity Process must recover GLEIF's vital business functions according to the GLEIF Code of Conduct for disaster situations
- Service Level Breaches trigger escalation management with defined severity levels and response timelines
- QVIs must monitor and report on their service level performance as specified in the SLA

## Examples

- **Service Level Target**: A QVI commits to 99.5% availability for its vLEI credential issuance service, measured monthly; falling below this threshold constitutes a Service Level Breach
- **vLEI Data Challenge**: A member of the public submits a challenge disputing that a person holds a claimed Official Organizational Role at a Legal Entity; the QVI must investigate and respond within 15 calendar days
- **Major Incident Response**: A QVI detects unauthorized access to its credential signing infrastructure, immediately escalates to GLEIF, begins forensic investigation, and produces a formal Incident Report
- **Disaster Recovery**: Following a catastrophic infrastructure failure, GLEIF activates its Service Continuity Process to restore vLEI services within the defined Recovery Time Objective

## Navigation

- **Up**: [Trust and Qualification](./trust-and-qualification.md)
- **Down**: *(none)*
- **Related**: [Annual vLEI Issuer Qualification](./annual-qualification.md), [Qualified vLEI Issuer](./qualified-vlei-issuer.md)
