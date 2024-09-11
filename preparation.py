import pandas as pd
import re
from collection import load_data

def prepare_data():
    #1. load the dataset
    data = load_data()
    #2. encode columns like balcony, parking etc
    data_encoded = encode_cat_cols(data)
    #3. parse the garden column
    df = parse_garden_col(data_encoded)
    return df

def encode_cat_cols(data):
    return pd.get_dummies(data, 
                                  columns = ['balcony', 
                                             'parking', 
                                             'furnished', 
                                             'garage', 
                                             'storage'], 
                                             drop_first=True)

def parse_garden_col(data):
    for i in range(len(data)):
        if data.loc[i, 'garden'] == 'Not present':
            data.loc[i, 'garden'] = 0
        else:
            data.loc[i, 'garden'] = int(re.findall(r'\d+', data.loc[i, 'garden'])[0])
    return data