from selenium import webdriver
import time
import re
import csv

URL_MOBILE = 'https://m.facebook.com/settings/notifications/groups/'
URL = 'https://m.facebook.com'
USER = 'xxxxx'
PASS = 'xxxxx'
ARQUIVO = 'arquivo.csv'

def fb_open():
    browser = webdriver.Firefox(timeout=20)
    time.sleep(1)
    print('Abriu o navegador')
    return browser

def fb_login(browser):
    browser.get(URL_MOBILE)
    user = browser.find_element_by_id('m_login_email')
    user.send_keys(USER)
    password = browser.find_element_by_name('pass')
    password.send_keys(PASS)
    login = browser.find_element_by_name('login')
    login.click()
    #um caso possível
    #ok = browser.find_element_by_xpath('/html/body/div/div/div/div/table/tbody/tr/td/div/form/div/input')
    #ok.click()
    time.sleep(1)
    print('Entrou no facebook')

def fb_getGroups(browser):
    elementos = browser.find_elements_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/h3/a')

    with open(ARQUIVO, 'w') as data:
        writer = csv.writer(data)
        for item in elementos:

            href = str(item.get_attribute('href'))
            id = re.findall(r'[0-9]{15}', href)

            if len(id) != 0:
                endereco = 'https://www.facebook.com/groups/' + id[0]
                writer.writerow([item.text, endereco])

browser = fb_open()
fb_login(browser)
fb_getGroups(browser)
browser.close()
print('Fechou o navegador')