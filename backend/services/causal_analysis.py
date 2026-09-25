from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from econml.dml import LinearDML
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier


FEATURE_COLUMNS = [
    "recency",
    "history",
    "mens",
    "womens",
    "newbie",
]

TREATMENT_COLUMN = "discount_offered"
OUTCOME_COLUMN = "purchased"


def run_dml(frame: pd.DataFrame) -> dict:
    """
    Run Double Machine Learning on the uploaded campaign dataset.
    """

    required = [
        *FEATURE_COLUMNS,
        TREATMENT_COLUMN,
        OUTCOME_COLUMN,
        "customer_id",
    ]

    missing = [column for column in required if column not in frame.columns]

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}"
        )

    data = frame[required].copy()

    # Convert numeric columns
    for column in FEATURE_COLUMNS + [
        TREATMENT_COLUMN,
        OUTCOME_COLUMN,
    ]:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )

    data = data.dropna().reset_index(drop=True)

    if len(data) < 30:
        raise ValueError(
            "At least 30 valid customers are required for causal analysis."
        )

    treatment = data[TREATMENT_COLUMN].astype(int).to_numpy()
    outcome = data[OUTCOME_COLUMN].astype(float).to_numpy()
    features = data[FEATURE_COLUMNS].astype(float).to_numpy()

    if len(np.unique(treatment)) < 2:
        raise ValueError(
            "Both treatment and control groups are required."
        )

    # DML nuisance models
    model_y = RandomForestRegressor(
        n_estimators=100,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1,
    )

    model_t = RandomForestClassifier(
        n_estimators=100,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1,
    )

    # Linear DML estimates heterogeneous treatment effects
    dml = LinearDML(
        model_y=model_y,
        model_t=model_t,
        discrete_treatment=True,
        random_state=42,
        cv=3,
    )

    dml.fit(
        outcome,
        treatment,
        X=features,
    )

    # Individual Treatment Effect
    ite = dml.effect(features)

    ite = np.asarray(ite, dtype=float)

    # Average Treatment Effect
    ate = float(np.mean(ite))

    positive_pct = float(np.mean(ite > 0) * 100)
    negative_pct = float(np.mean(ite < 0) * 100)

    # Save ITE results
    result = pd.DataFrame({
        "customer_id": data["customer_id"],
        "ITE": ite,
    })

    return {
        "data": result,
        "ate": ate,
        "avg_ite": ate,
        "positive_pct": positive_pct,
        "negative_pct": negative_pct,
        "sample_size": len(data),
    }