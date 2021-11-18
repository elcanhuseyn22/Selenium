from selenium import webdriver

from time import sleep
browser = webdriver.Chrome()

browser.get("https://instagram.com")

sleep(2)

username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

username.send_keys("username")

password.send_keys("password")

sleep(2)
login = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login.click()
sleep(2)

browser.get('https://www.instagram.com/1.lezgin/')


sleep(3)

followersButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')


followersButton.click()
sleep(5)

jscommands ="""
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommands)
match=False
while(match==False):
    lastCount = lenOfPage
    sleep(1)
    lenOfPage = browser.execute_script(jscommands)
    if lastCount == lenOfPage:
        match=True
sleep(2)

followersList = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
for follower in followers:
    followersList.append(follower.text)

count = 1
with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(str(count)+" "+follower+"\n")
        count+=1

browser.close()   
