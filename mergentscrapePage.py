import os, requests, re, codecs, csv
from bs4 import BeautifulSoup

path = '/Users/mhisten/OneDrive - The College of Wooster/research/lda/mergent/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

os.chdir(path)

f = codecs.open('ticker1.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')
link = 'https://www.mergentonline.com/advancedsearchresults.php?action=basic&page=1&sector=&u=on&ui=on&i=on&ii=on&searchtext='

for row in reader:
    print(row[1])
    name = (row[1])
    url = link + name

    doc_resp = requests.get(url, headers=headers)
    doc_str = doc_resp.text

    soup = BeautifulSoup(doc_str, 'html.parser')
    tag = soup.find('table', class_='tablesorter bodyline')
    rows = tag.find_all('tr')
    for row in rows:
        cells = row.find_all('td')

        try:

            href = cells[1]
            sic = cells[2]
            sic = str(sic)
            sic = sic.replace('<td>','')
            sic = sic.replace('</td>','')          
            exchange = cells[3]
            ticker = cells[4]
            ticker = str(ticker)
            ticker = ticker.replace('<td>','')
            ticker = ticker.replace('</td>','')
            ticker = ticker.lower()
            active = cells[5]
            active = str(active)
            active = active.replace('<td>','')
            active = active.replace('</td>','')
            active = active.lower()
            country = cells[6]
            country = str(country)
            country = re.search('">(.*)</a', country)
            country = country.group(1)
            country = country.lower()


            if active == 'active':
                link1 = 'https://www.mergentonline.com/'
                href = str(href)
                href1 = re.search('href="(.*)">', href)
                url1 = link1 + href1.group(1)
                outfile = open(path + 'mergent1.csv','a')
                outfile.write(str(name) + ',' + str(url1) + '\n')
       
        except:
            pass

        