# ETL Pipeline Project

## Project Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using Python, pandas, and MySQL.

The pipeline extracts holiday data from an external REST API, performs data cleaning and transformation, and loads the cleaned data into a MySQL database with logging and duplicate handling.



# Project Workflow

API → Data Cleaning → Data Transformation → MySQL Database → Logging



# Technologies Used

- Python
- pandas
- requests
- MySQL
- mysql-connector-python
- logging



# Deep Dive into the Project

## 1. REST APIs

A REST API (Representational State Transfer API) enables communication between a client and a server over HTTP protocols.

The API usually returns data in JSON format, which can then be processed and analyzed using Python.

In this project, holiday data is fetched from an external API and used for further processing and storage.



## 2. Data Cleaning

Although API data is generally structured and reliable, it is still important to perform data cleaning to ensure consistency and reliability.

The cleaning stage includes:
- Removing duplicate rows
- Standardizing text values
- Handling date formatting
- Preparing the data for transformation and storage

This helps maintain data quality throughout the pipeline.



## 3. Data Transformation

The fetched JSON data is converted into a pandas DataFrame for easier manipulation and analysis.

Using pandas, transformations such as:
- date conversion
- formatting
- duplicate removal
- additional column creation

can be performed efficiently.

After transformation, the data is converted back into dictionary format for insertion into the MySQL database.



## 4. Loading Data into MySQL

After cleaning and transformation, the processed data is loaded into a MySQL database using Python.

The database stores the cleaned holiday records, which can later be used for:
- SQL analysis
- reporting
- aggregation
- querying

A UNIQUE constraint is added to prevent duplicate records from being inserted into the database.


# Logging and Error Handling

The project uses Python logging to track:
- successful API requests
- database connections
- inserted rows
- duplicate rows
- failed insertions
- pipeline execution status

Error handling is implemented using try-except blocks to ensure the pipeline runs reliably without crashing unexpectedly.



# Features

- API data extraction
- Data cleaning using pandas
- JSON to DataFrame transformation
- MySQL database integration
- Duplicate protection
- Logging and monitoring
- Exception handling
- Modular function-based code structure



# Project Structure

```text
ETL-pipeline-Project/
│
├── app.py
├── requirements.txt
├── README.md
├── app.log
└── .gitignore
```


# Learning Outcomes

This project helped me learn:
- ETL pipeline development
- REST API integration
- Data transformation using pandas
- MySQL integration with Python
- Logging and monitoring
- Duplicate handling strategies
- Exception handling
- Modular code design
- Basic data engineering concepts
