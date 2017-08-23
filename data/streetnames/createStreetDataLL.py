# import csv
# with open('streettypes.csv', 'rb') as typefile:
#     typereader = csv.reader(typefile, delimiter=',', quotechar='|')
#     for row in typereader:
#         print ', '.join(row)

import csv, pandas as pd

types = pd.read_csv('streettypes.csv')
streets = pd.read_csv('9zvu-p8uz.csv')
# streets = pd.read_csv('https://data.calgary.ca/resource/9zvu-p8uz.csv?$query=SELECT%20street_name,street_type,street_quad%20GROUP%20BY%20street_name,street_type,street_quad LIMIT 100000')
merged = streets.merge(types, on='street_type')
merged = merged[['street_name','street_type_full','street_quad']]
merged['street_name'] = map(lambda x: x.title(), merged['street_name'])
merged.to_csv('output.csv', sep=",", quoting=csv.QUOTE_NONE, header=False, index=False)

s = open('output.csv')
f = open('input.txt', "w")
for street in s.readlines():
    # print(street.replace(",", " "))
    f.write(street.replace(",", " "))

s.close()
f.close()
