# Troubleshooting Notes

This document summarises some of the technical issues encountered while building the Spotify ETL pipeline and how they were resolved.

## Spotify API 403 Error

### Issue
Spotify API requests returned a 403 error.

### Resolution
Reviewed the Spotify application configuration, API permissions and authentication setup to identify the access issue.

### Learning
API errors should be investigated using the response status code, authentication method and endpoint permissions.

---

## Spotify API 404 Error

### Issue
A playlist request returned a resource not found error.

### Resolution
Checked the playlist URL and playlist ID being passed to the Spotify API.

### Learning
Resource identifiers should be validated before making API requests.

---

## AWS Lambda Timeout

### Issue
The Lambda function timed out while making API requests and processing data.

### Resolution
Increased the Lambda timeout configuration to allow sufficient execution time.

### Learning
Serverless functions need execution limits that match the workload being performed.

---

## Python Package Compatibility Issue

### Issue
A NumPy import error occurred in AWS Lambda because the package was not compatible with the Lambda runtime environment.

### Resolution
Reviewed the package/runtime compatibility and adjusted the deployment approach.

### Learning
Python dependencies used in Lambda must be compatible with the target runtime and operating environment.

---

## S3 put_object Parameter Error

### Issue
The S3 upload failed because an incorrect parameter was supplied to `put_object()`.

### Resolution
Used the correct `Body` parameter when uploading data to S3.

Example:

```python
s3.put_object(
    Bucket=bucket_name,
    Key=object_key,
    Body=data
)
