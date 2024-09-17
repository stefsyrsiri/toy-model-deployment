"""
This module provides functionalities to load data from a database.

It includes a function to extract data from the RentApartments table
in the database and load it into a pandas DataFrame. This module is useful
for scenarios where data needs to be retrieved from a database for further
analysis or processing. It uses SQLAlchemy for executing database queries
and pandas for handling the data in a DataFrame format.
"""

import pandas as pd
from loguru import logger

from config import model_settings


def load_data(path=model_settings.data_file_name) -> pd.DataFrame:
    """
    Extract the entire RentApartments DataFrame.

    Args:
        path: Path of the csv file

    Returns:
        pd.DataFrame: DataFrame containing the RentApartments data.
    """
    logger.info(f'loading csv file at path {path}')
    return pd.read_csv(path)
