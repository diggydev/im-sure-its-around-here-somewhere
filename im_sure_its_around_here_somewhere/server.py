from flask import Flask
from flask import render_template
import boto3
import os

s3 = boto3.client(service_name='s3',
aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = s3.list_objects(Bucket=os.environ['BUCKET'])
    contents = response['Contents']
    list = ''
    for obj in contents:
        list += obj['Key']
    return render_template('index.html', list=list)

if __name__ == "__main__":
    app.run()
