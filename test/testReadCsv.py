import csv
csv_file = csv.reader(open('test.csv','r'))
status = 0
for l in csv_file:
    line = []
    for elem in l:
        if elem != '':
            line.append(elem)
    for i in range(len(line)):
        line[i] = line[i].strip()
    if len(line) ==0 or line[0].startswith('#'): # 井号为注释
        if status == 1:
            print(dict)
        elif status == 3:
            print(dict)
        status = 0
        continue
    if status == 0:
        if line[0].startswith(':'):
            if line[0].startswith(':VAR'):
                var_name = line[1]
                tags = line[2:]
                dict = {}
                status = 1
            elif line[0]==':TABLE':
                var_name = line[1]
                tags = line[2:3]
                dict = {}
                status = 2
            else:
                raise Exception('Unidentified Tag')
        else:
            var_name = line[0]
            value = float(line[1])
            dict = {var_name:value}
            print(dict)
    elif status == 2:
        tag2 = line
        status = 3
        for j in range(len(tag2)):
            if tag2[j].isdigit():
                tag2[j] = int(tag2[j])
    elif status ==1:
        if len(tags) == 0:
            raise Exception('The index must be greater than 0')
        elif len(tags) == 1:
            key=line[0]
            if key.isdigit():
                key=int(key)
            dict[key] = float(line[1])
        else:
            key = line[:(len(line)-1)]
            for j in range(len(key)):
                if key[j].isdigit():
                    key[j] = int(key[j])
            key = tuple(key)
            dict[key] = float(line[-1])
    elif status == 3:
        tag1 = line[0]
        if tag1.isdigit():
            tag1 = int(tag1)
        for j in range(len(tag2)):
            key = (tag1,tag2[j])
            dict[key] = float(line[j+1])
if status == 1:
    print(dict)
elif status == 3:
    print(dict)