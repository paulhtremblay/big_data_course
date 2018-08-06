from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from parse_noaa import parse_line

from  pyspark.sql import SQLContext

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()
rdd = sc.textFile('us_stations_90s_sample_big.txt')\
    .map(parse_line)
noaa_df = rdd.toDF()\
        .drop('air_temperature_observation_air_temperature_quality_code')\
        .drop('air_temperature_observation_dew_point_quality_code')\
        .drop('air_temperature_observation_dew_point_temperature')\
        .drop('atmospheric_pressure_observation_sea_level_pressure')\
        .drop('atmospheric_pressure_observation_sea_level_pressure_quality_code')\
        .drop('fixed_weather_station_call_letter_identifier')\
        .drop('fixed_weather_station_ncei_wban_identifier')\
        .drop('fixed_weather_station_ncei_wban_identifier')\
        .drop('geophysical_point_observation_additional_data_identifier')\
        .drop('geophysical_point_observation_data_source_flag')\
        .drop('geophysical_point_observation_elevation_dimension')\
        .drop('geophysical_point_observation_latitude_coordinate')\
        .drop('geophysical_point_observation_longitude_coordinate')\
        .drop('geophysical_report_type_code')\
        .drop('liquid_precipitation_depth_dimension')\
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
        .withColumnRenamed('fixed_weather_station_usaf_master_station_catalog_identifier',
                'id')\
        .withColumnRenamed('point_observation_date_time', 'time')\
        .withColumnRenamed('air_temperature_observation_air_temperature', 'temperature')
noaa_df.registerTempTable('noaa')

states_df = spark.read.csv('us_stations_states.csv', header=True)
states_df.registerTempTable("states")

results_df = sqlContext.sql("""select *
    from noaa
    inner join states
    on states.id = noaa.id
    limit 10
    """)
results_df.show()

avg_df = sqlContext.sql("""select state,
        avg(temperature) as avg_temp
    from noaa
    inner join states
    on states.id = noaa.id
    group by state
    """)
avg_df.show()


