from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

page_count = 1
entries = []
while page_count<10:
    randomPage = random.randint(1,2222)
    new_url = url+str(randomPage)
    browser.get(new_url)

    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    page_count += 1


with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(entry+"\n")
        file.write(30*"*"+"\n")
        

browser.close()
