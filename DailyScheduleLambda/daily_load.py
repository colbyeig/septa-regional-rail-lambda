import pandas as pd
import boto3
import pyarrow as pa
import pyarrow.parquet as pq
from io import BytesIO

def upload_to_s3(df):

    s3=boto3.client('s3')

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

    s3.upload_fileobj(BytesIO(parquet_data), 'septa-regional-rails', 'train-file-tues.parquet')
