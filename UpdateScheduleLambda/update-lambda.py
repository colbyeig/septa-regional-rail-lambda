from update_extract import hit_train_view_endpoint
from update_transform import process_dataframe
from update_load import fetch_schedule_from_s3, reupload_to_s3 

def lambda_handler():
    status_df = hit_train_view_endpoint()

    current_df = fetch_schedule_from_s3()

    final_df = process_dataframe(current_df, status_df)

    reupload_to_s3(final_df)
