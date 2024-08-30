import json
import pickle
import numpy as np

__suburbs = None
__data_columns = None
__model = None

def get_estimated_price(suburb, bedrooms, bathrooms, garage, land_area, floor_area):
    try:
        suburb_index = __data_columns.index(suburb.lower())
    except: 
        suburb_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = garage
    x[3] = land_area
    x[4] = floor_area

    if suburb_index >= 0:
        x[suburb_index] = 1

    price = __model.predict([x])[0]
    return f"${price / 1_000_000:.2f}M"

def get_suburb_names():
    return __suburbs

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __suburbs

    with open(r'server/artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __suburbs = __data_columns[5:]  

    global __model
    with open(r'server/artifacts/Perth_Housing_Prediction.pickle', 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price('alfred cove', 3, 2, 5, 600, 300))
    print(get_estimated_price('alfred cove', 4, 2, 5, 700, 400))
    print(get_estimated_price('wooroloo', 5, 6, 2, 700, 400))
    print(get_estimated_price('yokine', 5, 6, 2, 700, 400))
