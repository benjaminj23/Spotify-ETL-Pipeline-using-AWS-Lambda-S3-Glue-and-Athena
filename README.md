# Spotify-ETL-Pipeline-using-AWS-Lambda-S3-Glue-and-Athena
# Spotify ETL Pipeline on AWS

## Overview
Built an end-to-end ETL pipeline using the Spotify Web API and AWS services to extract, transform, store and query music data.

## Architecture
Spotify API → AWS Lambda → Amazon S3 → AWS Glue Crawler → Glue Data Catalog → Amazon Athena

## Technologies
- Python
- Spotify Web API
- AWS Lambda
- Amazon S3
- AWS Glue
- Amazon Athena
- CloudWatch
- IAM
- Boto3

## Pipeline
1. Extract playlist data from Spotify API
2. Store raw JSON data in S3
3. Transform raw data into structured artist, album and song datasets
4. Store processed files back in S3
5. Use Glue Crawler to infer schema
6. Register tables in Glue Data Catalog
7. Query transformed data using Athena

## Key Learnings
- API authentication and JSON parsing
- Serverless ETL with AWS Lambda
- S3 object storage
- IAM roles and trust policies
- Schema discovery with Glue
- SQL querying using Athena
- Debugging with CloudWatch

## Challenges Solved
- Spotify API 403/404 errors
- Lambda timeout issues
- S3 put_object parameter errors
- IAM trust policy issues
- Glue crawler configuration
- CSV header handling in Athena
