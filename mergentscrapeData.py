import os, requests, re, codecs, csv
from bs4 import BeautifulSoup

path = '/Users/mhisten/OneDrive/research/lda/mergent/waves/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

os.chdir(path)

f = codecs.open('all1.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

for row in reader:
    print(row[3])
    url = row[3]
    doc_resp = requests.get(url, headers=headers)
    doc_str = doc_resp.text

    soup = BeautifulSoup(doc_str, 'html.parser')
    tag = soup.find('title')
    tag = str(tag).split(':')
    tag = tag[1].split('</title>')
    tag = tag[0].strip()
    outfile = open(path + 'name.csv','a')
    outfile.write(str(url) + ',' + str(tag) + '\n')


    '''
    tag = soup.find('div', {'id' : 'summarycol1'})
    for item in tag:
        print(item)
        if 'incorporated' in str(item).lower():
            try:
                item1 = str(item).split(',')
                item1 = (str(item1[0]).split("</strong>",1)[1]).strip()
                item1 = re.findall(r'\b\d+\b', item1)
                date = (item1[0])
        
                outfile = open(path + 'date2.csv','a')
                outfile.write(str(url) + ',' + str(date) + '\n')
            except:
                pass
        '''
