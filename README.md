# hashing-polars-plugin

A Polars plugin that provides hashing utilities for de-identifying sensitive PII data such as Medical Record Numbers (MRNs).

## Why Hashing Instead of Partial Masking?

Hashing offers several key advantages over simple masking:

-   **HIPAA Compliance**  
    Healthcare regulations require _irreversible_ de-identification of personal data. Hashing ensures that PII cannot be reconstructed from the transformed value.

-   **Research Analytics**  
    Enables tracking the same patient across multiple studies or datasets without revealing their identity. This is crucial for longitudinal studies and cohort analysis.

## Features

-   Hash string columns using HMAC-SHA256
-   Fast, native Rust performance via Polars plugin
-   Seamlessly integrates with Python via `pyo3-polars`
