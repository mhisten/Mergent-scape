from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time, os, codecs, csv

path = '/Users/mhisten/OneDrive/research/lda/mergent/leftover/'
chromedriver = '/Users/mhisten/OneDrive/Code/useful/chromedriver'


os.chdir(path)
f = codecs.open('revmergent2.csv', 'r', 'utf-8-sig')
reader = csv.reader(f, delimiter=',')
data = list(reader)


# convert to smaller sizes
x = 125 # number of companies added to bucket
length = int((len(data) / x))
data1 = []

for number in range(length):
    if number == 0:
        data2 = data[number:(number + 1) * (x)]
    else:
        if number == (length - 1):
            data2 = data[number * (x):]
        else: 
            data2 = data[number * (x):(number + 1) * (x)]
    data1.append([data2])
    

# run counter for each
y = 0
for number in range(length):
    
    data3 = (data1[number])
    driver = webdriver.Chrome(chromedriver)
    driver.set_window_size(1024,768)
    baseUrl = 'https://www.google.com/'
    driver.get(baseUrl)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    for i in data3[0]:
        y = y  + 1
        print(str(y) + ': ' + str(i[3]))
        link = i[3]
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[1]/div/a/span"))).click()  




