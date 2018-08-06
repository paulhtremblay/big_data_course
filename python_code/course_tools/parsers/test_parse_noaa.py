import parse_noaa

with open('../temp_data/us_stations_90_sample_small.txt', 'r') as read_obj:
    line = 'init'
    counter = 0
    while line:
        counter += 1
        line = read_obj.readline()
        d = parse_noaa.parse_line(line)
        x = d['liquid_precipitation_depth_dimension']
        if x:
            print(d['liquid_precipitation_depth_dimension'])
            break
