import os, codecs, csv, numpy, re, statistics, datetime
from numpy import cov


path = '/Users/mhisten/OneDrive/research/levi/companydata/stockprice/'
data1 = '/Users/mhisten/OneDrive/research/levi/companydata/ratio/ratiodata2.csv'
data2 = '/Users/mhisten/OneDrive/research/levi/companydata/ratio/data1.csv'
input1 = 'prices.csv'
output1 = 'pricesexcept1.csv'


def quarter_date(merger, YE):
    ye = YE[::-1]
    date1 = str(merger)
    date1 = date1.split('/')
    year = (date1[2])
    if len(year) < 4:
        year = '20' + year
    year = int(year)
    month = int(date1[0])
    day = int(date1[1])
    d1 = datetime.datetime(year,month,day)

    for item in ye:
        date1 = str(item)
        date1 = date1.split('/')
        year1 = (date1[2])
        month1 = int(date1[0])
        day1 = int(date1[1])
        if len(year1) < 4:
            year1 = '20' + year1
        year1 = int(year1)
        d2 = datetime.datetime(year1,month1,day1)
        
        if d1 > d2:
            pass
        else:
            yearend = d2
            break
            
    yearend = str(yearend)
    yearend = yearend.split(' ')
    yearend = yearend[0]
    yearend = yearend.split('-')
    year2 = yearend[0]
    year2 = str(year2)
    year2 = year2[2:]
    month2 = yearend[1]
    month2 = int(month2)
    day2 = yearend[2]
    day2 = int(day2)
    yearend = str(month2) + '/' + str(day2) + '/' + str(year2)
    return yearend


match = []
reader1 = csv.reader(open(data2, 'r'))
for rows in reader1:
    match.append(rows)

f = codecs.open(data1, 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

row_count1 = 0
row1 = []
row2 = 'blank'
row3 = 'blank'
check1 = 0
check2 = 0

for row in reader:
    row3 = row2
    row2 = row1
    row1 = row[0]
    row_count1 = row_count1 + 1

    if 'general company information' in (row[0]).lower():
        #ratio data
        if check1 == 1 and check2 == 1:

            #Grab dates and make quarterly
            for rows in match:
                company = rows[2]
                company = str(company)
                company = company.replace(',','')
                company = company.replace('.','')
                company = company.strip()
                if name == company:
                    merger.append(rows[3])
                    
            #Check for match
            for dates in merger:
                try:
                    quarter = quarter_date(dates,date1)
                    merger_quarters.append(quarter)
                except:
                    print(name + ': ' + dates)

            '''
            fin_data = []
            for obs in merger_quarters:
                try:
                    locate = date1.index(obs)
                    values = roa1[locate]
                    fin_data.append(values)
                except:
                    print(name)
                    print(obs)
            '''
            check1 = 0 
            check2 = 0
            
            
        merger = []
        merger_quarters = []
        item = str(row3).split(':')
        ticker = str(item[1]).split(')')
        ticker = str(ticker[0]).strip()
        exchange = str(item[0]).split('(')
        exchange = exchange[-1]
        name = str(item[0])
        name = name[:-(len(exchange) + 1)]
        name = name.replace(',','')
        name = name.replace('.','')
        name = name.strip()

    if 'roa %' in row[0].lower():
        roa1 = (row[1:])
        while '' in roa1:
            roa1.remove('')
        check2 = 1       

    if 'profitability ratios' in row[0].lower():
        date1 = (row[1:])
        while '' in date1:
            date1.remove('')
        check1 = 1

    