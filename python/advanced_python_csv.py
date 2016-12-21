import csv
with open('/home/osboxes/ds/metis/metisgh/prework/dsp/python/faculty.csv', newline='') as f:
    reader = csv.reader(f)
    first = next(reader, None)
    en = first.index(' email')
    
    emails = []
    for row in reader:
        e = row[en]
        emails.append(e)

print(emails)

with open('/home/osboxes/ds/metis/metisgh/prework/dsp/python/emails.csv', 'w+') as f:
    csvwrite = csv.writer(f)
    for line in emails:
        csvwrite.writerow([line])

