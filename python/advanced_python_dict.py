import re, csv
with open('/home/osboxes/ds/metis/metisgh/prework/dsp/python/faculty.csv', newline='') as f:
    reader = csv.reader(f)
    first = next(reader, None)
    dn = first.index(' degree')
    tn = first.index(' title')
    en = first.index(' email')
    nn = first.index('name')
    
    faculty_dict = {}
    professor_dict = {}

    for row in reader:
        lastn = row[nn].split()[-1]
        if lastn not in faculty_dict:
            faculty_dict[lastn] = []
        t = re.match(r'(.*?) (of|is)',row[tn])
        faculty_dict[lastn].append([row[dn],t.group(1),row[en]])
        
        firstn = row[nn][:-len(lastn)-1]
        if (firstn,lastn) not in professor_dict:
            professor_dict[(firstn,lastn)] = []
        professor_dict[(firstn,lastn)].append([row[dn],t.group(1),row[en]])
        
    print(faculty_dict)
    print(professor_dict)
    
    keys = sorted(professor_dict.keys(), key=lambda x:x[1])
    for k in keys:
        print(str(k) + ' ' + str(professor_dict[k]))
