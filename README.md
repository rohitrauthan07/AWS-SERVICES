# AWS-SERVICES

# Amazon S3 Interaction with Boto3

This Python script demonstrates how to interact with an Amazon S3 bucket using the `boto3` library. It provides functionality to list objects in the bucket, upload files to the bucket, and download files from the bucket.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system (version 3.x recommended)
- AWS account with access keys generated for programmatic access
- `boto3` library installed. You can install it using the following command:
    ```
    pip install boto3
    ```

## Configuration

1. AWS Credentials:
   - You need to have AWS credentials configured either using environment variables, IAM roles, or AWS CLI credentials file (`~/.aws/credentials`).

2. Bucket Name:
   - Replace the placeholder `'your_bucket_name'` in the code with the name of your S3 bucket.

3. Input Values:
   - When using the provided functions (`upload_file_to_bucket` and `download_file_from_bucket`), you need to provide input values such as local file paths, object names, and local destination paths.

## Usage

1. List Objects in the Bucket:
   - Run the `list_objects_in_bucket` function to list all objects in the specified S3 bucket.

2. Upload a File to the Bucket:
   - Use the `upload_file_to_bucket` function to upload a file to the specified S3 bucket. Provide the local file path and desired object name.

3. Download a File from the Bucket:
   - Use the `download_file_from_bucket` function to download a file from the specified S3 bucket. Provide the object name in the bucket and the local destination path.

## Example

```python
python s3_interaction.py
Replace 'your_bucket_name', 'local_file_path', 'object_name_in_bucket', and 'local_destination_path' with the actual input values.
