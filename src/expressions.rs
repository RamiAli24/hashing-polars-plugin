#![allow(clippy::unused_unit)]
use hex;
use hmac::{Hmac, Mac};
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use sha2::Sha256;

type HmacSha256 = Hmac<Sha256>;

// TODO:
const SECRET_KEY: &[u8] = b"your_super_secret_key_here";

#[polars_expr(output_type=String)]
fn hash_transform(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;

    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let mut mac =
            HmacSha256::new_from_slice(SECRET_KEY).expect("HMAC can take key of any size");
        mac.update(value.as_bytes());

        let result = mac.finalize().into_bytes();
        let hex_string = hex::encode(result);
        output.push_str(&hex_string);
    });

    Ok(out.into_series())
}
