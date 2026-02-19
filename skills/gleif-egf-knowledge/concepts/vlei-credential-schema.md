---
id: vlei-credential-schema
prefLabel: "vLEI Credential Schema"
altLabels: ["SemVer", "Semantic Versioning", "vLEI Credential Schema Registry"]
depth: 1
broader: ["vlei-credentials"]
narrower: []
related: ["acdc"]
---

# vLEI Credential Schema

## Definition

A vLEI Credential Schema is a JSON Schema 2020-12 compliant definition that specifies the structure, required fields, and data types for a particular vLEI Credential type. Each schema includes a Self-Addressing Identifier (SAID) that makes the schema immutably bound to its content, ensuring that any modification would produce a different identifier. All schemas are published in the vLEI Credential Schema Registry maintained by GLEIF as the sole authoritative source, with versioning governed by Semantic Versioning (SemVer 2.0.0) conventions.

## Key Facts

- Each vLEI Credential schema must be fully compliant with JSON Schema 2020-12, the version of JSON Schema that supports advanced features such as vocabulary-based extensibility
- The SAID embedded in each schema provides approximately 128 bits of cryptographic strength, encoded using CESR, making any schema tampering immediately detectable
- Schema versioning follows SemVer 2.0.0: backward incompatible changes require a higher MAJOR version number, which produces a new SAID even if only the version number changes
- GLEIF maintains the vLEI Credential Schema Registry as the single authoritative registry where all official schema definitions and their normative SAIDs are published
- The registry publishes distinct schemas for QVI vLEI Credentials, Legal Entity vLEI Credentials, OOR vLEI Credentials, ECR vLEI Credentials, and both OOR and ECR Authorization credentials
- Verifiers must resolve a credential's schema SAID against the registry to confirm the credential conforms to a recognized schema

## Rules & Constraints

- A backward incompatible schema change must increment the MAJOR version number and will produce a new SAID, effectively creating a new schema identity
- All credential instances must include the SAID of their governing schema, enabling verifiers to retrieve and validate the schema from the registry
- Only GLEIF may publish or update schemas in the vLEI Credential Schema Registry; no other party has publishing authority
- Schema SAIDs are computed over the full schema content, so even whitespace-level changes produce a different SAID, enforcing strict immutability

## Examples

- **QVI vLEI Credential Schema**: SAID ELqriXX1-lbV9zgXP4BXxqJlpZTgFchll3cyjaCyVKiz at version 1.0.0, defining the fields required for authorizing a Qualified vLEI Issuer
- **Legal Entity vLEI Credential Schema**: SAID EK0jwjJbtYLIynGtmXXLO5MGJ7BduX2vr2_MhM9QjAxZ at version 1.0.0, specifying the LEI and AID binding structure
- **OOR vLEI Credential Schema**: SAID EILRwno8cEnkGTi9cr7-PFg_IXTPx9fZ0r9snFFZ0nm at version 1.0.0, defining person-to-role binding with official organizational role fields
- **ECR vLEI Credential Schema**: SAID EohcE9MV90LrygJuYN1N0c5XXNFkzwFxUBfQ24v7qeEY at version 1.0.0, including personally identifying fields that support graduated disclosure

## Disambiguation

> **vLEI Credential Schema** vs **vLEI Credential Schema Registry**: A schema is the JSON Schema definition for a single credential type. The registry is the GLEIF-maintained repository that publishes all official schemas and their normative SAIDs.

> **vLEI Credential Schema** vs **ACDC Schema Section**: The schema section within an ACDC credential references the schema SAID. In fully-compressed form, only the SAID appears; in fully-expanded form, the complete schema is embedded.

## Navigation

- **Up**: [vLEI Credentials](./vlei-credentials.md)
- **Down**: *(none)*
- **Related**: [Authentic Chained Data Container](./acdc.md)
