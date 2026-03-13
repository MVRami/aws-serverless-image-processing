import boto3
from PIL import Image
import os
import tempfile

s3 = boto3.client('s3')

OUTPUT_BUCKET = "image-output-bucket-team18"

TARGET_SIZE = (300, 300)

def lambda_handler(event, context):
    record = event['Records'][0]
    input_bucket = record['s3']['bucket']['name']
    input_key = record['s3']['object']['key']

    print(f"Triggered by upload: s3://{input_bucket}/{input_key}")

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, os.path.basename(input_key))
        output_path = os.path.join(tmpdir, "resized.jpg")

        s3.download_file(input_bucket, input_key, input_path)

        img = Image.open(input_path)
        img.thumbnail(TARGET_SIZE)

        img.save(output_path, format="JPEG")

        output_key = f"resized_{os.path.basename(input_key)}"
        s3.upload_file(output_path, OUTPUT_BUCKET, output_key)

        print(f"Resized image saved to s3://{OUTPUT_BUCKET}/{output_key}")

    return {
        "statusCode": 200,
        "body": "Image resized successfully"
    }
