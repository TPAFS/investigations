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


def introduce_label_newlines(
    labels: list[str], char_limit: int = 20, strict: bool = False
):
    """Introduce and return newlines into list of labels.

    If strict, allow chopping words to attain max char_limit per line. Otherwise, split
    on whitespace, and allow a line to exceed the char limit just by the amount necessary
    to complete a word.
    """
    if strict:
        return [
            "\n".join(
                [label[i : i + char_limit] for i in range(0, len(label), char_limit)]
            )
            for label in labels
        ]
    else:
        result = []
        for label in labels:
            lines = []
            current_line = ""
            words = label.split()
            for word in words:
                if len(current_line) + len(word) + 1 <= char_limit:
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            result.append("\n".join(lines))
        return result
