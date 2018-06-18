import boto3
s3 = boto3.resource('s3')
bucket = 'paulhtremblay'
my_bucket = s3.Bucket(bucket)
from io import BytesIO
from gzip import GzipFile

for i in my_bucket.objects.filter(Prefix='noaa/data/1990'):
    obj = s3.Object(bucket, i.key)
    content = s3.Object(bucket, i.key).get()
    bytestream = BytesIO(content['Body'].read())
    lines = GzipFile(None, 'rb', fileobj=bytestream).read().decode('utf-8').split('\n')
    print(lines[0])

    break
