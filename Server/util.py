# define a function to get location names
import json
import pickle
import numpy as np

__locations = None # global variables
__data_columns = None
__model = None

# estimate the price based on the number of bathroom and bedroom and location
# the input is x, the output is estimate price
def get_estimated_price(location,sqft,size_num,bath):
    try:
        loc_index = __data_columns.index(location.lower())  # get the location index
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = size_num
    if loc_index >= 0:
        x[loc_index] = 1  # make the location index to 1

    return round(__model.predict([x])[0],2)

# read the columns in json file from the 4th columns because the first 3 columns are features (not locations).
def get_location_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:] # from the 3rd columns becasue the first two columns are features

    global __model
    with open("./artifacts/Bengaluru-house-data-prediction-model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))

