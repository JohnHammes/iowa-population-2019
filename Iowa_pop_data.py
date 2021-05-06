# Print out most all counties in 2019 from most to least populace

import csv
with open('County_Population_in_Iowa_by_Year.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

counties = []
for line in rows:
    if '2019' in line['Year']:
        counties.append((int(line['Population']), line['County']))

sorted_counties = list(reversed(sorted(counties)))
for i, county in enumerate(sorted_counties, 1):
    print(f"#{str(i).ljust(2)} {county[1].ljust(20)} {county[0]}")
