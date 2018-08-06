import datetime
import sys
print(sys.path)
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
from course_tools.parsers.parse_noaa2 import parse_line
import pprint
pp = pprint.PrettyPrinter(indent = 4)

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()

rdd = sc.textFile('s3a://paulhtremblay/noaa/data/1990/010010-99999-1990.gz')\
        .union(sc.textFile('s3a://paulhtremblay/noaa/data/1990/010014-99999-1990.gz'))\
    .map(parse_line)
schema = StructType([StructField("air_temperature_observation_air_temperature", FloatType()),
                    StructField("air_temperature_observation_air_temperature_quality_code", StringType()),
                    StructField('air_temperature_observation_dew_point_quality_code', StringType()),
                    StructField('air_temperature_observation_dew_point_temperature', FloatType()),
                    StructField('atmospheric_pressure_observation_sea_level_pressure', FloatType()),
                    StructField('atmospheric_pressure_observation_sea_level_pressure_quality_code', StringType()),
                    StructField('county', StringType()),
                    StructField('fixed_weather_station_call_letter_identifier', StringType()),
                    StructField('fixed_weather_station_ncei_wban_identifier', StringType()),
                    StructField('fixed_weather_station_usaf_master_station_catalog_identifier', StringType()),
                    StructField('geophysical_point_observation_additional_data_identifier', StringType()),
                    StructField('geophysical_point_observation_data_source_flag', StringType()),
                    StructField('geophysical_point_observation_elevation_dimension', IntegerType()),
                    StructField('geophysical_point_observation_latitude_coordinate', FloatType()),
                    StructField('geophysical_point_observation_longitude_coordinate', FloatType()),
                    StructField('geophysical_report_type_code', StringType()),
                    StructField('liquid_precipitation_depth_dimension', FloatType()),
                    StructField('liquid_precipitation_occurrence_identifier', StringType()),
                    StructField('liquid_precipitation_period_quantity_in_hours', IntegerType()),
                    StructField('meteorological_point_observation_quality_control_process_name', StringType()),
                    StructField('point_observation_date_time', TimestampType()),
                    StructField('sky_condition_observation_cavok_code', StringType()),
                    StructField('sky_condition_observation_ceiling_determination_code', StringType()) ,
                    StructField('sky_condition_observation_ceiling_height_dimension', StringType()),
                    StructField('sky_condtion_observation_ceiling_quality_code', StringType()),
                    StructField('state', StringType()),
                    StructField('total_variable_characters', StringType()),
                    StructField('visibility_observation_distance_dimension', IntegerType()),
                    StructField('visibility_observation_distance_quality_code', StringType()),
                    StructField('visibility_observation_quality_variability_code', StringType()),
                    StructField('visibility_observation_variability_code', StringType()),
                    StructField('wind_observation_direction_angle', IntegerType()),
                    StructField('wind_observation_direction_quality_code', StringType()),
                    StructField('wind_observation_speed_quality_code', StringType()),
                    StructField('wind_observation_speed_rate', IntegerType()),
                    StructField('wind_observation_type_code', StringType())
                    ])



df = rdd.toDF(schema = schema)\
        .write.mode('Overwrite').parquet('s3a://paulhtremblay/parquet_noaa_data')

#df.printSchema()

