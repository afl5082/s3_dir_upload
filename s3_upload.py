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
    ignore_files_dir = [
        '__pycache__',
        's3_upload.py',
        '.prefectignore',
        '.git',
        's3_upload',
        '.github',
        '.gitignore',
        ]

    for root,dirs,files in os.walk('.'):
       
        for file in files:
            if file in ignore_files_dir:
                continue

            path = os.path.join(root,file)
            root_dir = path.split('/')[1]
            if root_dir in ignore_files_dir:
                continue
                
            file_path_to_upload = path.replace('./','')
            file_path_to_upload = '{}{}{}'.format(repo_name,'/',file_path_to_upload)
            print(path,bucketname,file_path_to_upload)
            s3.upload_file(path,bucketname,file_path_to_upload)
            
def main():
    repo_name = os.environ.get("REPO_NAME")
    repo_name = '{}{}'.format('prefect-server-repo/',repo_name)
    bucket = os.environ.get("BUCKET_NAME")

    uploadDirectory(repo_name,bucket)
    
main()
