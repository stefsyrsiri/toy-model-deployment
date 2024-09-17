"""
This module provides functionality for preparing a dataset for ML model.

It consists of functions to load data from a database,
encode categorical columns, and parse specific columns for further processing.
"""

import re

import pandas as pd
from loguru import logger

from model.pipeline.collection import load_data


def prepare_data() -> pd.DataFrame:
    """
    Prepare the dataset for analysis and modelling.

    This involves loading the data, encoding categorical columns,
    and parsing the 'garden' column.

    Returns:
        pd.DataFrame: The processed dataset.
    """
    logger.info('starting up preprocessing pipeline')
    # 1. load the dataset
    dataframe = load_data()
    # 2. encode columns like balcony, parking etc
    data_encoded = _encode_cat_cols(dataframe)
    # 3. parse the garden column
    return _parse_garden_col(data_encoded)


def _encode_cat_cols(dataframe) -> pd.DataFrame:
    """
    Encode categorical columns into dummy variables.

    Args:
        dataframe (pd.DataFrame): The original dataset.

    Returns:
        pd.DataFrame: Dataset with categorical columns encoded.
    """
    cols = [
        'balcony',
        'parking',
        'furnished',
        'garage',
        'storage',
        ]
    logger.info(f'encoding categorical columns {cols}')
    return pd.get_dummies(dataframe, columns=cols, drop_first=True)


def _parse_garden_col(dataframe) -> pd.DataFrame:
    """
    Parse the 'garden' column in the dataset.

    Args:
        dataframe (pd.DataFrame): The dataset with a 'garden' column.

    Returns:
        pd.DataFrame: The dataset with the 'garden' column parsed.
    """
    dataframe['garden'] = dataframe['garden'].apply(
        lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0]),
    )
    return dataframe
