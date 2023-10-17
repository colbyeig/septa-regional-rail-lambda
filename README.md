# SEPTA Data Pipeline from REST to Tableau

This Git repository contains the code for a data pipeline that extracts Regional Rail data from the SEPTA API for the Temple University station and loads it into Tableau using two AWS Lambda functions. This project is a part of the author's Honors Data Science Degree coursework in the Intelligent Transportation Systems class CEE 4221.

## Project Overview

In the field of Intelligent Transportation Systems, efficient and real-time data processing is crucial. The SEPTA Data Pipeline to Tableau project provides a solution to collect and transform Regional Rail data from the Southeastern Pennsylvania Transportation Authority (SEPTA) API and load it into Tableau for further analysis and visualization.

The project is organized into two AWS Lambda functions, each designed to perform specific tasks:

### 1. Daily Function

The Daily Lambda Function retrieves the train schedule from the SEPTA API each morning at 5 AM. The code for this function is located in the `DailyScheduleLambda` directory. This ETL workflow is seperated into `daily_extract.py`, `daily_transform.py`, `daily_load.py` scripts, and the entry point for the Lambda function is `daily_lambda.py`.

### 2. Batch Function
