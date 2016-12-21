# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
with open('/home/osboxes/ds/metis/metisgh/prework/dsp/python/football.csv', newline='') as f:
    reader = csv.reader(f)
    first = next(reader, None)
    ga = first.index('Goals Allowed')
    gf = first.index('Goals')
    minv = 100
    for row in reader:
        if abs(int(row[ga])-int(row[gf])) < minv:
            minv = abs(int(row[ga])-int(row[gf]))
            teamn = row[0]
    print(teamn)
