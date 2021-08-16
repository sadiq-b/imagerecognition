PyImageRekognition
Image Rekognition using AWS S3, AWS Lambda, AWS Rekognition
what you need: AWS account - basic free
Navigate to aws IAM (identity and management access)

Create a IAM > Access Management > Roles > Create role with 2 permissions (AWSLambdaExecute & AmazonRekognitionFullAccess)

Create AWS S3 Bucket - change Default encryption to enable and leave Encryption key type as Amazon S3 key (SSE-S3)

Upload an image to S3 Bucket

Create Lambda function > Runtime Python 3.6 > Chnage default execution role to the role you created in step 2

Write Lambda function to in Rekognition on your image in S3 Bucket

About
lambda function that uses aws S3 and aws rekognition algorithm


© 2021 GitHub, Inc.
