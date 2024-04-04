import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define your bucket name
bucket_name = 'your_bucket_name'

# Example: List all objects in the bucket
def list_objects_in_bucket(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Objects in bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error listing objects: {e}")

# Example: Upload a file to the bucket
def upload_file_to_bucket(bucket_name, file_path, object_name):
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded as '{object_name}' to bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Example: Download a file from the bucket
def download_file_from_bucket(bucket_name, object_name, local_file_path):
    try:
        s3.download_file(bucket_name, object_name, local_file_path)
        print(f"File '{object_name}' downloaded to '{local_file_path}' from bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error downloading file: {e}")

# Example usage
if __name__ == "__main__":
    # List objects in the bucket
    list_objects_in_bucket(bucket_name)

    # Upload a file to the bucket
    upload_file_to_bucket(bucket_name, 'local_file_path', 'object_name_in_bucket')

    # Download a file from the bucket
    download_file_from_bucket(bucket_name, 'object_name_in_bucket', 'local_destination_path')
