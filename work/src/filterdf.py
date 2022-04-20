# -*- coding: utf-8 -*-

import pandas as pd

def filter_by_regex(df: pd.DataFrame, column_name: str, regex: str) -> pd.DataFrame:
    return df.loc[df[column_name].str.contains(regex, regex=True)]
