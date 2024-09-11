import pandas as pd
from config import settings

CSV_PATH = 'rent_apartments.csv'

def load_data(path=settings.data_file_name):
    return pd.read_csv(path)
