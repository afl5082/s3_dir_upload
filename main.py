import boto3
import os


def aws_conn():
    session = boto3.Session(
    aws_access_key_id= os.environ.get("AWS_PUBLIC_KEY"),
    aws_secret_access_key= os.environ.get("AWS_SECRET_KEY"),
)
    return session.resource('s3')


def uploadDirectory(path,bucketname):

    #s3 = aws_conn()

    for root,dirs,files in os.walk(path):
            for file in files:
                path = os.path.join(root,file)
                print(path,bucketname,path)
                #s3.upload_file(os.path.join(root,file),bucketname,file)

def main():
    path = os.environ.get("SOURCE_DIR")
    bucket = os.environ.get("BUCKET_NAME")

    uploadDirectory(path,bucket)
    
main()
