#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from datetime import date

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def main():
    login("", "")
    change_date()
    email(get_data())

def login(username, password):
    driver.get("https://www.musicnotes.com/commerce/signin.asp?si=in&rc=1")
    driver.find_element_by_id('signInEmail').send_keys(username)
    driver.find_element_by_id('signInPassword').send_keys(password)
    driver.find_element_by_id('signInButton').click()

    
def change_date():
    driver.implicitly_wait(3)
    driver.find_element_by_id('start-date-field').clear()
    driver.find_element_by_id('start-date-field').send_keys("01/01/2020")
    driver.find_element_by_id('date-range-button').click()

    
def get_data():
    
    data = " "
    
    for i in range(1, 5): 
        if (driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[2]').is_displayed()):
            title = driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[2]')
            data += title.text.upper() + " has "
        else:
            print("Can't find title!")
    
        if (driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[5]').is_displayed()):
            downloads = driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[5]')
            data += downloads.text + " downloads" 
        else:
            print(f"Can't find {title.text}'s number of downloads!")
            
        if (driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[6]').is_displayed()):
            mn_Money = driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[6]')
            data += '\n' + "MusicNotes earned " + mn_Money.text
        else:
            print(f"Can't find {mn_Money.text}'s net revenue!")
            
        if (driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[7]').is_displayed()):
            my_Money = driver.find_element_by_xpath(f'//*[@id="royalties-table"]/tbody/tr[{i}]/td[7]')
            data += "; You earned " + my_Money.text + '\n\n'
        else:
            print(f"Can't find {my_Money.text}'s your revenue!")
            
    if (driver.find_element_by_xpath('//*[@id="totals-row"]/td[7]').is_displayed()):
        my_Total_Money = driver.find_element_by_xpath('//*[@id="totals-row"]/td[7]')
        data += "YOUR TOTAL REVENUE: " + my_Total_Money.text + '\n'
    else:
        print(f"Can't find {my_Total_Money.text}'s your revenue!")
            
    return data
    
def email(data):
    today = date.today()
    d = today.strftime("%m/%d/%y")
    
    server = smtplib.SMTP_SSL("", 000) #enter correct server
    server.ehlo()
    server.login("", "")
    server.sendmail("", "", d + '\n\n' + data)
    
    server.quit()
    
main()

