# SEPTA Data Pipeline from REST to Tableau

This Git repository contains the code for a data pipeline that extracts Regional Rail data from the SEPTA API for the Temple University station and loads it into an S3 Bucket connected to Tableau using two AWS Lambda functions. 

## Project Overview

In the field of Intelligent Transportation Systems, efficient and real-time data processing is crucial. The SEPTA Data Pipeline to Tableau project provides a solution to collect and transform Regional Rail data from the Southeastern Pennsylvania Transportation Authority (SEPTA) API and load it into Tableau for further analysis and visualization.

The project is organized into two AWS Lambda functions, each designed to perform specific tasks:

### 1. Daily Function

The Daily Lambda Function retrieves the train schedule from the SEPTA API each morning at 5 AM. The code for this function is located in the `DailyScheduleLambda` directory. This ETL workflow is seperated into `daily_extract.py`, `daily_transform.py`, `daily_load.py` scripts, and the entry point for the Lambda function is `daily-lambda.py`.

### 2. Batch Function

The Batch Lambda Function retrieves the Train Statuses from a different SEPTA API endpoint. It triggers every 10 minutes and to aggregate Train status over the original Train schedule. The code for this function is located in the `UpdateScheduleLambda` directory. This ETL workflow is seperated into `update_extract.py`, `update_transform.py`, `update_load.py` scripts, and the entry point for the Lambda function is `update-lambda.py`.

### 3. Tech Stack

The SEPTA Data Pipeline from REST to Tableau project leverages a range of technologies to ensure efficient data extraction, transformation, and loading into an S3 Bucket, ultimately connecting to Tableau for data visualization and analysis:

#### Extract:
- **Python Requests Library**: The data extraction process is facilitated using the Python Requests library. This library allows us to make HTTP requests to the SEPTA API and retrieve the necessary Regional Rail data.

#### Transform:
- **Pandas DataFrame Operations**: Pandas is used extensively for data transformation. It provides powerful tools for cleaning, reshaping, and aggregating the extracted data, ensuring that it's prepared for analysis and visualization.
- ** Python DateTime Library**: The Python DateTime library is used for many of the time-centric transformations. This is vital for future aggregation and analytics in Tableau.

#### Load:
- **Boto3**: Boto3, the Amazon Web Services (AWS) SDK for Python, is employed for interacting with AWS services, including S3. It is used to store the transformed data into an S3 bucket, making it available for further processing and integration with Tableau.

- **pyarrow.parquet**: The PyArrow library is utilized to convert the Pandas DataFrame into the Parquet format. Parquet is an efficient columnar storage format, which is well-suited for large datasets. This format is ideal for storing data in S3 and makes it easy to work with in downstream processes.

By combining these technologies, the SEPTA Data Pipeline ensures a robust and scalable data processing workflow, enabling data-driven insights and visualizations in Tableau.
