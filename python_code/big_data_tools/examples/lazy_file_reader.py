#BAD uses too much memory
needed = []
with open('us_stations_90s_sample_big.txt', 'r') as read_obj:
    lines = read_obj.readlines()
    for line in lines:
        if line.strip() == '0092619760999991990062009004-15883+054517FM-12+001399999V0201601N01031220001CN0350001N9+02641+01761101671ADDAG10999GA1031+005709009GF104991041081008001041001MD1999999-0091REMSYN017333   59009 83019':
            needed.append(line)

def my_generator():
    with open('us_stations_90s_sample_big.txt', 'r') as read_obj:
        line = 'init'
        while line:
            line = read_obj.readline()
            yield line


#LAZY evaluation
needed = []
gen = my_generator()
for line in gen:
    if line.strip() == '0092619760999991990062009004-15883+054517FM-12+001399999V0201601N01031220001CN0350001N9+02641+01761101671ADDAG10999GA1031+005709009GF104991041081008001041001MD1999999-0091REMSYN017333   59009 83019':
        needed.append(line)

gen = my_generator()
needed = filter(lambda x: x.strip() == '0092619760999991990062009004-15883+054517FM-12+001399999V0201601N01031220001CN0350001N9+02641+01761101671ADDAG10999GA1031+005709009GF104991041081008001041001MD1999999-0091REMSYN017333   59009 83019', gen)

print(list(needed))
