#!/bin/bash
set -e
sudo aws s3 cp s3://paulhtremblay/word_count.py /usr/local/bin
sudo aws s3 cp s3://paulhtremblay/parse_noaa2.py /usr/local/bin
sudo aws s3 cp s3://paulhtremblay/noaa_temp_to_parquet.py /usr/local/bin
#sudo pip-3.4 install boto3
pip-3.4 install boto3 --user
