import json
# import json communicate with api
import boto3
# boto3 is the aws module for python

def lambda_handler(event, context):
    # get the rekognition client/make connection - go to rekoginition service and save it to the variable
    rekognition = boto3.client("rekognition")
    # make connection to s3 service
    s3 = boto3.client("s3")
    # invoke get_bucket function on s3 service and pass in bucket name as first argument and key as name of image file
    fileObj = s3.get_object(Bucket = "nameofyourbucket", Key ="nameofyourimageinyourbucket.jpg" )
    file_content = fileObj["Body"].read()
    # invoke detect_labels is the deep learning function on rekognition service
    response = rekognition.detect_labels(Image = { "S3Object" : {"Bucket" : "nameofyourbucket", "Name" : "nameofyourimageinyourbucket.jpg" }}, MaxLabels=3, MinConfidence=70 )
    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    } 
