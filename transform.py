filepath = 'source.json'
data = []
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    
    while line:
        row = line.strip()
        data.append(row)
        line = fp.readline()
        cnt += 1

f = open('target.json', 'w')
for (idx, i) in enumerate(data):
    if idx == 0:
        f.write("[{},".format(i))
    elif idx < len(data)-1:
        f.write("{},".format(i))
    else:
        f.write("{}]".format(i))
f.close()
