#文化大學版 成功
#  python PCCU_AutoConnect.py
#  pyinstaller -F .\PCCU_AutoConnect.py         打包指令
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'usernameStr'
passwordStr = 'passwordStr'

browser = webdriver.Chrome()
browser.get(('https://ap1.pccu.edu.tw/index.asp?user=student'))

# fill in username and hit the next button

#設定第二選項

username = browser.find_element_by_id('Account')
username.send_keys(usernameStr)
             
# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'PassWord')))
password.send_keys(passwordStr)
 
signInButton = browser.find_element_by_css_selector("span[title=\"登入專區\"]")#有沒有辦法改成找title
signInButton.click()

browser.close()
