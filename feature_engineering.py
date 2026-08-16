import numpy as np
import pandas as pd

BOOLEAN_COLUMNS = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
]

FURNISHING_MAP = {
    "unfurnished": 0,
    "semi-furnished": 1,
    "furnished": 2,
}


def engineer_features(data):
    """Apply the same Week 6 feature engineering used by the trained model."""
    df = pd.DataFrame(data).copy()

    # Keep categorical yes/no columns as categories for the model's OneHotEncoder.
    # Numeric versions are used only to construct derived features.
    binary_numeric = df[BOOLEAN_COLUMNS].apply(lambda col: col.map({"yes": 1, "no": 0}))

    df["LogArea"] = np.log1p(df["area"])
    df["TotalRoomsProxy"] = df["bedrooms"] + df["bathrooms"] + df["stories"]
    df["AreaPerRoom"] = df["area"] / df["TotalRoomsProxy"].replace(0, np.nan)
    df["BathroomBedroomRatio"] = df["bathrooms"] / df["bedrooms"].replace(0, np.nan)
    df["AmenityCount"] = binary_numeric.sum(axis=1)
    df["HasExtraSpace"] = ((binary_numeric["basement"] == 1) | (binary_numeric["guestroom"] == 1)).astype(int)
    df["FurnishingScore"] = df["furnishingstatus"].map(FURNISHING_MAP)
    df["AreaCategory"] = pd.cut(
        df["area"],
        bins=[-np.inf, 3000, 6000, np.inf],
        labels=["Small", "Medium", "Large"],
    )

    return df
