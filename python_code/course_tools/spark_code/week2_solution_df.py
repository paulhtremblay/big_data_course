import datetime
import sys
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
from parse_noaa import parse_line
import pprint
pp = pprint.PrettyPrinter(indent = 4)


conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()



rdd = sc.textFile('file:///home/henry/projects/big_data_course/workspace/us_stations_90_sample_small.txt')\
        .map(parse_line)
#pp.pprint(rdd.take(1))
schema = StructType([StructField("air_temperature_observation_air_temperature", FloatType()),
                    StructField("air_temperature_observation_air_temperature_quality_code", StringType()),
                    StructField('air_temperature_observation_dew_point_quality_code', StringType()),
                    StructField('air_temperature_observation_dew_point_temperature', FloatType()),
                    StructField('atmospheric_pressure_observation_sea_level_pressure', FloatType()),
                    StructField('atmospheric_pressure_observation_sea_level_pressure_quality_code', StringType()),
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



df = rdd.toDF(schema = schema)
df = df.drop('air_temperature_observation_dew_point_quality_code')\
    .drop('air_temperature_observation_air_temperature_quality_code')\
    .drop('air_temperature_observation_dew_point_temperature')\
    .drop('atmospheric_pressure_observation_sea_level_pressure')\
    .drop('atmospheric_pressure_observation_sea_level_pressure_quality_code')\
    .drop('fixed_weather_station_call_letter_identifier')\
    .drop('fixed_weather_station_ncei_wban_identifier')\
    .drop('geophysical_point_observation_additional_data_identifier')\
    .drop('geophysical_point_observation_data_source_flag')\
    .drop('geophysical_point_observation_elevation_dimension')\
    .drop('geophysical_point_observation_latitude_coordinate')\
    .drop('geophysical_point_observation_longitude_coordinate')\
    .drop('geophysical_report_type_code')\
    .drop('liquid_precipitation_occurrence_identifier')\
    .drop('liquid_precipitation_period_quantity_in_hours')\
    .drop('meteorological_point_observation_quality_control_process_name')\
    .drop('sky_condition_observation_cavok_code')\
    .drop('sky_condition_observation_ceiling_determination_code')\
    .drop('sky_condition_observation_ceiling_height_dimension')\
    .drop('sky_condtion_observation_ceiling_quality_code')\
    .drop('total_variable_characters')\
    .drop('visibility_observation_distance_dimension')\
    .drop('visibility_observation_distance_quality_code')\
    .drop('visibility_observation_quality_variability_code')\
    .drop('visibility_observation_variability_code')\
    .drop('wind_observation_direction_angle')\
    .drop('wind_observation_direction_quality_code')\
    .drop('wind_observation_speed_quality_code')\
    .drop('wind_observation_speed_rate')\
    .drop('wind_observation_type_code')\
    .withColumnRenamed('air_temperature_observation_air_temperature', 'temperature')\
    .withColumnRenamed('point_observation_date_time', 'date_time')\
    .withColumnRenamed('liquid_precipitation_depth_dimension', 'precipitation')\
    .withColumnRenamed('fixed_weather_station_usaf_master_station_catalog_identifier', 'station_id')
df.printSchema()
df.createOrReplaceTempView("weather")
df_sql_test = spark.sql("select * from weather limit 10")
df_sql_test.show()
df_temp_moisture = spark.sql("""select 
    station_id,
    avg(temperature) as avg_temperature,
    sum(precipitation) as sum_preciptation
    from weather 
    where temperature is not null
    and precipitation is not null
    and station_id is not null
    group by station_id
    """)
df_temp_moisture.show()
df_temp_moisture.coalesce(1)\
     .write\
    .format("csv")\
    .mode("overwrite")\
    .save("file:///home/henry/projects/big_data_course/workspace/moisture_temps")
        




