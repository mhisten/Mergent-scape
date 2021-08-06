import os, codecs, csv


path1 = '/Users/mhisten/OneDrive/research/lda/mergent/waves/files/stockcsv/'
path2 = '/Users/mhisten/OneDrive/research/lda/mergent/'
#path1 = '/Users/mhisten/OneDrive - The College of Wooster/research/lda/Note/http/'
#path1 = '/Users/mhisten/OneDrive - The College of Wooster/research/lda/Note/processed/'
os.chdir(path1)


def search(term):
    reader = csv.reader(open(path2 + 'stockdate.csv', 'r'))
    for row in reader:
        if str(row[0]) == term:
            return row[2]


print(search('Facebook Inc'))



'''
for filename in os.listdir(path1):
    if filename != '.DS_Store':
        print(filename)

        f = codecs.open(filename, 'r', 'utf-8-sig')
        reader = csv.reader(f, delimiter=',')
        row_count0 = sum(1 for row in reader)

        ticker1 = 0
        price1 = 0
        shares1 = 0
        data0 = []
        data1 = []
        row1 = 'blank'
        row2 = 'blank'
        row3 = 'blank'
        cash1 = 0

        f = codecs.open(filename, 'r', 'utf-8-sig')
        reader = csv.reader(f, delimiter=',')
        row_count1 = 0

        for row in reader:
            row3 = row2
            row2 = row1
            row1 = row[0]
            row_count1 = row_count1 + 1

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
                #outfile = open(path2 + 'stockname.csv','a')
                #outfile.write(str(name).strip() + '\n')
            
            if 'closing price' in row[0].lower():
                if 'not available' in row[0].lower():
                    pass
                
'''