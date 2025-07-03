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
              '45f447ca7d79acab6fd97db9409ccfcbb21c80c97ff46890ac6bd5b6e94788c5',
              'e2821f7c9df02d22ec059486352902784675c257410214666d9a9595dd130322',
              'a6c487458e640fec3a30d1531404f4d6f9d6af5d7ed7d8afcd15375951ac0f99',
              '32db4af0559ece55aa2f82d6b4535d435cffcbb51715e5f6607bca4e0f47847b',
              '1c1ad43764a60a822a1f57b53e3496447f5a03056e01da8e1d604287ff7c14b8'
            ],
        }
    )

    assert_frame_equal(result, expected_df)
