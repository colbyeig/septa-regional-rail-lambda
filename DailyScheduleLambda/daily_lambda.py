from daily_extract import hit_septa_rail_endpoint, create_dataframe
from daily_transform import create_estimated_time, seperate_times
from daily_load import upload_to_s3

def lambda_handler():
    # Make a request to the SEPTA API and retrieve the response
    response = hit_septa_rail_endpoint()
    
    # Create a DataFrame from the response data
    train_df = create_dataframe(response)

    # Transform the DataFrame by calling the 'create_estimated_time' function
    transformed_df = create_estimated_time(train_df)

    # Transform the DataFrame by calling the 'seperate_time' function
    transformed_df = seperate_times(transformed_df)

    # Upload file to S3 in Parquet format
    upload_to_s3(transformed_df)
