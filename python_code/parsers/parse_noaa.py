import csv
import datetime

class InvalidDoc(Exception):
    pass

def len_var(line):
    return int(line[0:4])

def line_is_valid_len(line):
    if len(line.strip()) != len_var(line) + 105:
        raise InvalidDoc("not right length")

def create_date_time(line):
    try:
        return datetime.datetime.strptime(line[15:27], '%Y%m%d%H%M')
    except ValueError:
        raise InvalidDoc("String not in right format for datetime")

def _check_valid_length(line, start, stop, required):
    if stop >= len(line) and not required:
        return
    if stop >= len(line) and  required:
        raise InvalidDoc("line not right length for field")
    return True

def get_str_field(line, start, stop, required=True):
    if _check_valid_length(line, start, stop, required):
        return line[start - 1: stop]

def _field_with_divide_factor(line, start, stop, scale, required = True):
    assert isinstance(scale, int), "scale must be int"
    x = get_signed_int_field(line, start, stop, required)
    if x:
        return x/float(scale)

def get_temp(line, start, stop, required = True):
    t =  _field_with_divide_factor(line, start, stop, 10, required)
    if t == 999.9:
        return None
    return t

def get_air_pressure(line, start, stop, required = True):
    return _field_with_divide_factor(line, start, stop, 10, required)

def get_geo_coord(line, start, stop, required = True):
    return _field_with_divide_factor(line, start, stop, 1000, required)

def get_signed_int_field(line, start, stop, required = True):
    if _check_valid_length(line, start, stop, required):
        if line[start -1: start] == '+':
            return get_int_field(line, start + 1, stop, required)
        return get_int_field(line, start, stop, required)

def get_int_field(line, start, stop, required=True):
    if _check_valid_length(line, start, stop, required):
        try:
            return int(line[start - 1: stop])
        except ValueError:
            raise InvalidDoc("Can't convert to int")

def parse_line_(line):
    return (line, len(line))

def parse_line(line):
    return {
        'total_variable_characters':get_int_field(line, 1, 4),
        'fixed_weather_station_usaf_master_station_catalog_identifier':get_str_field(line, 5, 10),
        'fixed_weather_station_ncei_wban_identifier':get_int_field(line, 10, 15),
        'point_observation_date_time':create_date_time(line),
        'geophysical_point_observation_data_source_flag': get_str_field(line,
            28, 28),
        'geophysical_point_observation_latitude_coordinate':get_geo_coord(line,29,
            34),
        'geophysical_point_observation_longitude_coordinate':get_geo_coord(line,35,
            41),
        'geophysical_report_type_code':get_str_field(line,42, 46),
        'geophysical_point_observation_elevation_dimension':
             get_int_field(line, 47, 51),
        'fixed_weather_station_call_letter_identifier':get_str_field(line, 52,
             56),
        'meteorological_point_observation_quality_control_process_name':
            get_str_field(line, 57, 60),
        'wind_observation_direction_angle':get_int_field(line, 61, 63),
        'wind_observation_direction_quality_code':get_int_field(line, 64, 64),
        'wind_observation_type_code':get_str_field(line, 65, 65),
        'wind_observation_speed_rate': get_int_field(line, 66, 69),
        'wind_observation_speed_quality_code': get_int_field(line, 70, 70),
        'sky_condition_observation_ceiling_height_dimension':get_int_field(line,
            71, 75),
        'sky_condtion_observation_ceiling_quality_code':get_int_field(line, 76,
            76),
        'sky_condition_observation_ceiling_determination_code':get_str_field(line,
            77, 77),
        'sky_condition_observation_cavok_code':get_str_field(line, 78, 78),
        'visibility_observation_distance_dimension':get_int_field(line, 79,
            84),
        'visibility_observation_distance_quality_code':get_int_field(line,
            85,85),
        'visibility_observation_variability_code':get_str_field(line, 86, 86),
        'visibility_observation_quality_variability_code':get_int_field(line,
            87, 87),
        'air_temperature_observation_air_temperature':get_temp(line, 88,
            92),
        'air_temperature_observation_air_temperature_quality_code':
        get_str_field(line, 93, 93),
        'air_temperature_observation_dew_point_temperature':get_temp(line, 94,
            98),
        'air_temperature_observation_dew_point_quality_code':get_str_field(line,
            99, 99),
        "atmospheric_pressure_observation_sea_level_pressure":get_air_pressure(line,
            100, 104),
        "atmospheric_pressure_observation_sea_level_pressure_quality_code":get_str_field(line,
            105, 105, False),
        "geophysical_point_observation_additional_data_identifier":get_str_field(line, 106,
            108, False),
        "liquid_precipitation_occurrence_identifier":get_str_field(line, 109,
            111, False),
        }
