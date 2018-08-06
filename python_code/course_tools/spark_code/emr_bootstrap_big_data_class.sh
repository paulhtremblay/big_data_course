#!/bin/bash
set -e
sudo aws s3 cp s3://paulhtremblay/word_count.py /usr/local/bin
sudo aws s3 cp s3://paulhtremblay/noaa_temp_to_parquet.py /usr/local/bin
aws s3 cp s3://paulhtremblay/course_tools-.2.tar.gz .
tar -xvzf course_tools-.2.tar.gz
cd course_tools-.2/
python3 setup.py install --user
sudo python34 setup.py install 
#sudo pip-3.4 install boto3
pip-3.4 install boto3 --user
