import boto3
import pyarrow.parquet as pq
import pandas as pd
import io
from io import BytesIO
import pyarrow as pa

s3 = boto3.client('s3')
bucket_name = 'septa-regional-rails'
file_name='train-file-lambda.parquet'

def fetch_schedule_from_s3():
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    parquet_data = response['Body'].read()
    df = pd.read_parquet(io.BytesIO(parquet_data))
    return df

def reupload_to_s3(df):
    table = pa.Table.from_pandas(df)
    
    # Create an in-memory buffer to write the Parquet file
    buf = pa.BufferOutputStream()

    # Create a Parquet writer
    writer = pq.ParquetWriter(buf, table.schema)

    # Write the table to the in-memory Parquet file
    writer.write_table(table)

    # Close the writer to finalize the file
    writer.close()

    # Get the bytes from the in-memory buffer
    parquet_data = buf.getvalue()

    s3.upload_fileobj(BytesIO(parquet_data), bucket_name, file_name)