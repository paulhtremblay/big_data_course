import boto3
s3 = boto3.resource('s3')
bucket = 'paulhtremblay'
my_bucket = s3.Bucket(bucket)
from io import BytesIO
from gzip import GzipFile
from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict
import pprint
pp = pprint.PrettyPrinter(indent = 4)

us_paths = []
for i in my_bucket.objects.filter(Prefix='noaa/data/1990'):
    obj = s3.Object(bucket, i.key)
    content = s3.Object(bucket, i.key).get()
    bytestream = BytesIO(content['Body'].read())
    lines = GzipFile(None, 'rb', fileobj=bytestream).read().decode('utf-8').split('\n')
    the_dict = parse_line(lines[0])
    station_id = the_dict.get('fixed_weather_station_usaf_master_station_catalog_identifier')
    if us_stations_dict.get(station_id, {}).get('ctry') == "US":
        us_paths.append(i.key)
with open('../data/us_stations_keys.txt', 'w') as write_obj:
    for i in us_paths:
        write_obj.write('{p}\n'.format(p = i))

