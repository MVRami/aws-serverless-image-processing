![AWS](https://img.shields.io/badge/AWS-Lambda-orange)
![Cloud](https://img.shields.io/badge/Cloud-Serverless-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
# aws-serverless-image-processing
# Serverless Image Processing System using AWS Lambda

A serverless cloud-based image processing system built using AWS services. The application automatically resizes images when they are uploaded to an Amazon S3 bucket.

## Academic Context

This project was developed as part of coursework at **Blekinge Institute of Technology (BTH)**.

## System Overview

The system follows an event-driven architecture:

1. A user uploads an image to an **Amazon S3 bucket**.
2. The upload triggers an **AWS Lambda function**.
3. The Lambda function resizes the image.
4. The processed image is stored in another **S3 bucket**.

## Architecture

Upload → S3 Bucket → Lambda Function → Resized Image → Output S3 Bucket

## Technologies Used

* AWS Lambda
* Amazon S3
* Amazon CloudWatch
* Python
* Serverless Architecture

## Performance Analysis

The system uses **CloudWatch metrics** to analyze:

* Lambda invocation count
* Concurrent executions
* Performance under multiple image uploads

Experiments were conducted with different workloads to observe **automatic scaling behavior** of AWS Lambda.

## Skills Demonstrated

* Serverless Cloud Architecture
* Event-driven Systems
* AWS Lambda Development
* Cloud Monitoring with CloudWatch
* Python-based Image Processing

## Author

**Rami M V**
Student — Blekinge Institute of Technology
