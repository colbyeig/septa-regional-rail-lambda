# SEPTA Data Pipeline to Tableau

This Git repository contains the code for a data pipeline that extracts data from the SEPTA API and loads it into Tableau using two AWS Lambda functions. This project is a part of the author's Honors Data Science Degree coursework in the Intelligent Transportation Systems class CEE 4221.

## Project Overview

In the field of Intelligent Transportation Systems, efficient and real-time data processing is crucial. The SEPTA Data Pipeline to Tableau project provides a solution to collect and transform data from the Southeastern Pennsylvania Transportation Authority (SEPTA) API and load it into Tableau for further analysis and visualization.

The project is organized into two AWS Lambda functions, each designed to perform specific tasks:

### 1. Extract Function

The extract function retrieves data from the SEPTA API. The code for this function is located in the `extract` directory. The primary script responsible for this task is `extract.py`, and the entry point for the Lambda function is `extract_handler.py`.

### 2. Transform and Load Function

The transform and load function processes the extracted data and loads it into Tableau. This function is located in the `transform_load` directory. The primary script for transformation and loading is `transform_load.py`, and the entry point for the Lambda function is `transform_load_handler.py`.
