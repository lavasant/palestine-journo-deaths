import csv

infile = open('./csv/wikipedia_list_of_journalists_killed_in_the_gaza_war.csv', 'r')
outfile = open('./csv/monthly_totals_of_journalists_killed_in_the_gaza_war.csv', 'w')
monthcountdict = {}

# skips header row
iterinfile = iter(infile)
next(iterinfile)

for line in iterinfile:
    linecontentsarray = line.split(',')
    month = linecontentsarray[0].split(' ')[0]
    year = linecontentsarray[1]
    monthandyearstr = month + year

    if monthandyearstr in monthcountdict:
        monthcountdict[monthandyearstr] += 1
    else:
        monthcountdict[monthandyearstr] = 1

with open('./csv/monthly_totals_of_journalists_killed_in_the_gaza_war.csv','w') as f:
    w = csv.writer(f)
    w.writerows(monthcountdict.items())

infile.close()
outfile.close()
