#![allow(clippy::unused_unit)]
use std::fmt::Write;

use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use sha2::{Digest, Sha256}; // Add this for hashing

#[polars_expr(output_type=String)]
fn hash_transform(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        // Hash the input string using SHA-256
        let mut hasher = Sha256::new();
        hasher.update(value.as_bytes());
        let hash_result = hasher.finalize();

        // Write the hex-encoded hash to the output
        for byte in hash_result {
            output.push_str(&format!("{:02x}", byte));
        }
    });
    Ok(out.into_series())
}
