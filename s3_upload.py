import boto3
import os


def aws_conn():
    session = boto3.Session(
    aws_access_key_id= os.environ.get("AWS_PUBLIC_KEY"),
    aws_secret_access_key= os.environ.get("AWS_SECRET_KEY"),
)
    return session.client('s3') 


def uploadDirectory(repo_name,bucketname):

    s3 = aws_conn()
    ignore_files_dir = ['__pycache__','upload_s3.py','.prefectignore']

    for root,dirs,files in os.walk('.'):
        for file in files:
            if file in ignore_files_dir or 'main.cpython' in file:
                continue

            path = os.path.join(root,file)
            file_path_to_upload = path.replace('./','')
            file_path_to_upload = '{}{}{}'.format(repo_name,'/',file_path_to_upload)
            print(path,bucketname,file_path_to_upload)
            s3.upload_file(os.path.join(root,file),bucketname,file_path_to_upload)

def main():
    repo_name = os.environ.get("REPO_NAME")
    repo_name = '{}{}'.format('prefect-server-repo/',repo_name)
    bucket = os.environ.get("BUCKET_NAME")

    uploadDirectory(repo_name,bucket)
    
main()
