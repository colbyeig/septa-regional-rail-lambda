import requests 
import pandas as pd

# Define a function to make a request to the SEPTA rail endpoint
def hit_septa_rail_endpoint():
    # Define the URL for the SEPTA API
    url = "https://www3.septa.org/api/Arrivals/index.php?station=Temple%20U&results=100"

    # Define request headers
    headers = {'content-type': 'application/json'}

    # Send a GET request to the SEPTA API and parse the JSON response
    response = requests.get(url, params=headers).json()

    # Extract the relevant data from the response
    without_request_timestamp = response[list(response.keys())[0]]

    return without_request_timestamp

# Define a function to create a DataFrame from the SEPTA API response
def create_dataframe(response_list):
    # Extract northbound and southbound data dictionaries from the response list
    north_dict = response_list[0]
    south_dict = response_list[1]

    # Normalize and create DataFrames for northbound and southbound trains, dropping unnecessary columns
    north_df = pd.json_normalize(north_dict, 'Northbound').drop(labels=['track', 'track_change', 'platform', 'platform_change', 'next_station'], axis=1)
    south_df = pd.json_normalize(south_dict, 'Southbound').drop(labels=['track', 'track_change', 'platform', 'platform_change', 'next_station'], axis=1)

    # Merge the northbound and southbound DataFrames into a single DataFrame
    train_df = north_df.merge(south_df, how='outer')

    return train_df
