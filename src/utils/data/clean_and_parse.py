import pandas as pd


def cast_to_int(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Cast list of specified columns in df to int.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe on which to cast types.
    cols : list[str]
        Columns in dataframe.

    Returns
    -------
    pd.DataFrame
        Dataframe with updated types.
    """
    conversion_dict = {name: int for name in cols}
    df = df.astype(conversion_dict)
    return df


def cast_to_float(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Cast list of specified columns in df to float.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe on which to cast types.
    cols : list[str]
        Columns in dataframe.

    Returns
    -------
    pd.DataFrame
        Dataframe with updated types.
    """
    conversion_dict = {name: float for name in cols}
    df = df.astype(conversion_dict)
    return df
