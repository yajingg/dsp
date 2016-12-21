import re, csv
with open('/home/osboxes/ds/metis/metisgh/prework/dsp/python/faculty.csv', newline='') as f:
    reader = csv.reader(f)
    first = next(reader, None)
    dn = first.index(' degree')
    tn = first.index(' title')
    en = first.index(' email')
    
    degrees = {}
    titles = {}
    emails = []
    domains = {}
    for row in reader:
        deg = row[dn].split()
        for d in deg:
            m = d.replace('.','').upper()
            if m not in degrees:
                degrees[m] = 1
            else:
                degrees[m] += 1
        
        t = re.match(r'(.*?) (of|is)',row[tn])
        if t.group(1) not in titles:
            titles[t.group(1)] = 1
        else:
            titles[t.group(1)] += 1
        
        e = row[en]
        emails.append(e)
        
        ed = re.match(r'.+?@(.+)',e)
        if ed.group(1) not in domains:
            domains[ed.group(1)] = 1
        else:
            domains[ed.group(1)] += 1
        
    print(degrees)
    print(titles)
    print(emails)
    print(domains)
    
    
