lines = """
MA 5
MA 7
NH 1
NH 2
MA 3

"""
data = lines.split('\n')
print(data)

#non functional way
ma = 0
nh = 0
for i in data:
    if i == '':
        continue
    st, temp = i.split()
    if st == 'MA':
        ma += float(temp)
    else:
        nh += float(temp)
print(ma, nh)

#functional way
#lets do this one step at a time
ma_list = [x for x in data if x[0:2] == 'MA']
print(ma_list)
ma_list = [x.split() for x in data if x[0:2] == 'MA']
print(ma_list)
ma_list = [x.split()[1] for x in data if x[0:2] == 'MA']
print(ma_list)
ma_list = [float(x.split()[1]) for x in data if x[0:2] == 'MA']
print(ma_list)

#now lets sum!
s = sum([float(x.split()[1]) for x in data if x[0:2] == 'MA'])
print(s)
#OR
print(sum([float(x.split()[1]) for x in data if x[0:2] == 'MA']))

#finally, this is it in one line

print(sum([float(x.split()[1]) for x in data if x[0:2] == 'MA']),
sum([float(x.split()[1]) for x in data if x[0:2] == 'NH']
        ))

