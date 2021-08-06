import os, codecs, csv, numpy, re, statistics, datetime
from numpy import cov


path = '/Users/mhisten/OneDrive/research/levi/companydata/stockprice/'

input1 = 'finaldata1.csv'
output1 = 'prices2.csv'
output2 = 'pricesexcept1.csv'


def index_function(stonks1,stonks2,merger):

    location = stonks1.index(merger)
    range1 = stonks2[(location-1):location]
    range2 = stonks2[(location):(location+1)]

    range1 = [float(i) for i in range1]
    range2 = [float(i) for i in range2]

    average1 = sum(range1)/len(range1)
    average2 = sum(range2)/len(range2)
    var1 = statistics.variance(range1) 
    var2 = statistics.variance(range2) 

    return [average1, average2, var1, var2]
def add_date(merger):
    merger1 = merger.split('/')
    month = merger1[0]
    day = merger1[1]
    year = merger1[2]
    d1 = datetime.datetime(int(year),int(month),int(day))
    d1 = d1 + datetime.timedelta(days=1)
    d2 = str(d1)
    d2 = d2.split(' ')
    d2 = d2[0]
    d2 = d2.split('-')
    year2 = d2[0]
    month2 = d2[1]
    day2 = d2[2]
    d2 = str(month2) + '/' + str(day2) + '/' + str(year2)
    return d2

match = []
reader2 = csv.reader(open(path + input1, 'r'))
for row in reader2:
    match.append(row)

f = codecs.open(path + 'stockdata.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')

cp1 = 0
merger = 'blank'
row1 = 'blank'
row2 = 'blank'
row3 = 'blank'

for row in reader:
    row3 = row2
    row2 = row1
    row1 = row[0]

    if cp1 == 1:
        if row[0] in (None, ""):
            cp1 = 0
            for dates in merger:
                merger1 = dates
                try:
                    values = index_function(stonks1,stonks2,dates)
                except:
                    dates = add_date(dates)
                    try:
                        values = index_function(stonks1,stonks2,dates)
                    except:
                        dates = add_date(dates)
                        try:
                            values = index_function(stonks1,stonks2,dates)
                        except:
                            dates = add_date(dates)
                            try: 
                                values = index_function(stonks1,stonks2,dates)
                            except: 
                                dates = add_date(dates)
                                try:
                                    values = index_function(stonks1,stonks2,dates)
                                except:
                                    values = 'nnnn'
                outfile = open(path + output1,'a')
                outfile.write(str(name) + ',' + str(merger1) + ',' + str(values[0]) + ',' + str(values[1]) + ',' + str(values[2]) + ',' + str(values[3]) + ',' + '\n')
    
        else:
            try:
                count = count + 1
                price = (row[0])
                str(price)
                price = price.split(':')
                date = str(price[0]).strip()
                price = str(price[1]).strip()
                stonks1.append(date)
                stonks2.append(price)
            except:
                pass

    if 'general company information' in (row[0]).lower():
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
        print(name)

        #Grab dates and make quarterly
        merger = []
        for rows in match:
            company = rows[2]
            company = str(company)
            company = company.replace(',','')
            company = company.replace('.','')
            company = company.strip()

            if name == company:
                merger.append(rows[3])

    if 'closing price' in row[0].lower():
        if 'not available' in row[0].lower():
            pass
        else:
            cp1 = 1
            count = 0
            stonks1 = []
            stonks2 = []

    