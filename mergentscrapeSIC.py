import requests, re, codecs, csv
from bs4 import BeautifulSoup

input1 = '/Users/mhisten/OneDrive/research/levi/companydata/data1.csv'
output1 = '/Users/mhisten/OneDrive/research/levi/companydata/industry.csv'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

f = codecs.open(input1, 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    name = row[0]
    company = row[1]
    url = row[2]
    
    doc_resp = requests.get(url, headers=headers)
    doc_str = doc_resp.text

    soup = BeautifulSoup(doc_str, 'html.parser')
    tag = soup.find(id = 'summarycol2')

    for rows in tag:
        text = str(rows)
        m = re.search('SIC(.+?)</p>', text)
        if m:
            SIC = m.group(1)
            SIC = SIC.replace(')','')
            SIC = SIC.replace(' ','')

    print(name + ', ' + company + ', ' + SIC)
    outfile = open(output1,'a')
    outfile.write(str(name) + ',' + str(company) + ',' + str(SIC) + '\n')
 
    
