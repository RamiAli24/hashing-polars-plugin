import polars as pl
from polars.testing import assert_frame_equal
from polars_utils import hash_transform  # Adjust if needed

def test_hashing():
    df = pl.DataFrame(
        {
            "Patient": ["john", "sam", "edmond", "sara", "hammond"],
            "MRN": [
                "MRN-2024-001234",
                "MRN-2024-005678",
                "MRN-2023-009876",
                "MRN-2024-003456",
                "MRN-2023-007890",
            ],
        }
    )

    result = df.with_columns(
        hashed_mrn=hash_transform("MRN")
    )

    expected_df = pl.DataFrame(
        {
            "Patient": ["john", "sam", "edmond", "sara", "hammond"],
            "MRN": [
                "MRN-2024-001234",
                "MRN-2024-005678",
                "MRN-2023-009876",
                "MRN-2024-003456",
                "MRN-2023-007890",
            ],
            "hashed_mrn": [
                "31190444c8cb2bc0a1b48c82dbd165bf8544b11c5088066a1c79868cc45e6f13",
                "29f1ca863776956e3cc3b35ae2fd362988463c9b017cdc2fc647c45e0b819a33",
                "173f522721e228f2af97da70e8b31f8da65a05f1405f5ef038ee045bb77fab9c",
                "e3f8cc8b95f96e84a9bb32a964fe26b19c4b9bd3a0e5dbe093dfd79b6a4e3027",
                "1cef2f644a9a7cf8f3c9ffcbfcc61f8bcaa3777b801ab8332f0a19a253c9c8f0",
            ],
        }
    )

    assert_frame_equal(result, expected_df)
