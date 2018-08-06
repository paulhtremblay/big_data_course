import datetime
import boto3
session = boto3.Session(profile_name='default')
client = session.client('emr')

def make_instances():
    return {
       'InstanceGroups': [
           {
           'InstanceRole': 'MASTER',
           'Market': 'SPOT',
           'BidPrice': '.6',
           'InstanceType': 'm1.medium',
           'InstanceCount': 1,
           'Configurations': [
               {"Classification":"emrfs-site",
               "Properties":{"fs.s3.consistent.retryPeriodSeconds":"10",
                   "consistent":"true",
                   "Consistent":"true",
                   "fs.s3.consistent.retryCount":"5",
                   "fs.s3.consistent.metadata.tableName":"EmrFSMetadata"},
               "Configurations":[]
               },
               ],
       },
           {
           'InstanceRole': 'CORE',
           'Market': 'SPOT',
           'BidPrice': '.6',
           'InstanceType': 'm3.xlarge',
           'InstanceCount': 2,
           'Configurations': [
               {"Classification":"emrfs-site",
               "Properties":{"fs.s3.consistent.retryPeriodSeconds":"10",
                   "consistent":"true",
                   "Consistent":"true",
                   "fs.s3.consistent.retryCount":"5",
                   "fs.s3.consistent.metadata.tableName":"EmrFSMetadata"},
               "Configurations":[]
               },
               ],

       }
           ],
       'Ec2KeyName': 'ubuntu-home',
       'KeepJobFlowAliveWhenNoSteps': False,
       'Ec2SubnetId': "subnet-0f159079",
   }

def make_bootstrap():
    return[
            {
                'Name': 'Wordcount bootstrap',
                'ScriptBootstrapAction': {
                    'Path': 's3://paulhtremblay/emr_bootstraps/emr_bootstrap_big_data_class.sh',
                }
            },
        ]



response = client.run_job_flow(
   Name = "big data example {0}".format(datetime.datetime.now()),
   LogUri =  "s3n://paulhtremblay/emr-logs/",
   ReleaseLabel = 'emr-5.3.0',
   Instances = make_instances(),
   JobFlowRole = 'EMR_EC2_DefaultRole',
   ServiceRole = 'EMR_DefaultRole',
   BootstrapActions= make_bootstrap(),


   Steps=[
       {'Name': 'first_step',
        'ActionOnFailure': 'TERMINATE_JOB_FLOW',
        'HadoopJarStep': {
           'Args': ['spark-submit', '/usr/local/bin/noaa_temp_to_parquet.py' ],
           'Jar': 'command-runner.jar'}

        }],
   Applications =  [
        {
            "Name": "Hadoop",
        },
        {
            "Name": "Spark",
        }
    ],

    Configurations = [{
        'Classification': 'spark-log4j',
        'Properties': {
            'log4j.rootCategory': 'ERROR, console'
        }
    },

    {
        'Classification': 'spark-defaults',
        'Properties': {
            'spark.ui.showConsoleProgress': 'false',
            'spark.executorEnv': 'PYTHONHASHSEED=321',
            #'spark.eventLog.dir':'hdfs:///var/log/spark/apps'
            # could set above line to s3:
        }


    }, {
        'Classification': 'spark-env',
        'Properties': {},
        'Configurations': [{
            'Classification': 'export',
            'Properties': {
                'PYSPARK_PYTHON': 'python34',
                'PYSPARK_DRIVER_PYTHON': 'python34'
                #can export pytonpath here
            }
        }]
    },
        {
            "Classification": "hadoop-env",
            "Properties": {},
            "Configurations": [
                {
                    "Classification": "export",
                    "Properties": {
                        "PYTHONHASHSEED": "0"
                    },
                    "Configurations": []
                }
            ]
        }
    ],
   )
print(response)

