import polars as pl
from polars_utils import hash_transform


df = pl.DataFrame(
    {
        "Patient": ["john", "sam", "edmond", "sara", "hammond"],
        "MRN": ["MRN-2024-001234", "MRN-2024-005678", "MRN-2023-009876", "MRN-2024-003456", "MRN-2023-007890"],
    }
)
result = df.with_columns(hashed_name=hash_transform("MRN"))

print(result)
print(result.to_dict(as_series=False))

