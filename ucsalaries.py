import requests
import csv
  
data = {
  '_search': 'false',
  'nd': '',
  'rows': '315668',
  'page': '1',
  'sidx': 'EAW_LST_NAM',
  'sord': 'asc',
  'year': '2020',
  'location': 'ALL',
  'firstname': '',
  'lastname': '',
  'title': '',
  'startSal': '0',
  'endSal': '9999999'
}

response = requests.post('https://ucannualwage.ucop.edu/wage/search.action', data=data)

content = response.content.decode('UTF-8')
content_obj = eval(content)
rows = content_obj['rows']

fieldnames = ['id', 'year', 'location', 'firstname', 'lastname', 'title', 'gross-pay', 'regular-pay', 'overtime-pay', 'other-pay' ] 

csv_file = "uc-salaries.csv"

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames) 
    for data in rows:
        writer.writerow(data['cell'])
