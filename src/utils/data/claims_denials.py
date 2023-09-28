import typing as t

import pandas as pd


def get_overturn_rate(
    df: pd.DataFrame,
    outcome_col_name: str = "Outcome",
    overturn_val: str = "Insurer Denial Overturned",
):
    """
    Given a pandas dataframe and outcome column, calculate overturn rate across the dataframe.
    """
    total_count = len(df)
    overturn_count = len(df[df[outcome_col_name] == overturn_val])
    fraction = overturn_count / total_count if total_count > 0 else -1
    return fraction


def get_overturn_rates_by_categorical_col(
    df: pd.DataFrame,
    categorical_col_name: str,
    outcome_col_name: str = "Outcome",
    overturn_val: str = "Insurer Denial Overturned",
    exclude_cat_vals: list[t.Union[int, str]] = [],
    include_cat_vals: list[t.Union[int, str]] = [],
):
    """
    Given a pandas dataframe, categorial column, and outcome column, calculate overturn rates broken
    down by category, returned as a list of (category, overturn rate) tuples.
    """

    # Get unique values of "categorical_col_name" and sort the results
    if len(include_cat_vals) > 0:
        unique_cat_values = sorted(include_cat_vals)
    else:
        unique_cat_values = sorted(df[categorical_col_name].unique())
        [unique_cat_values.remove(val) for val in exclude_cat_vals]

    # Calculate the fractions
    fractions = []
    for val in unique_cat_values:
        total_count = len(df[df[categorical_col_name] == val])
        overturn_count = len(
            df[
                (df[categorical_col_name] == val)
                & (df[outcome_col_name] == overturn_val)
            ]
        )
        fraction = overturn_count / total_count if total_count > 0 else -1
        fractions.append(fraction)

    # Combine the two lists
    result = list(zip(unique_cat_values, fractions))
    return result
