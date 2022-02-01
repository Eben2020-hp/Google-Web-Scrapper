## Download ChromeDriver from https://sites.google.com/chromium.org/driver/downloads

## Install Selenium
# pip install selenium  --> Check using <import selenium>


## Import necessary packages
from numpy import NaN
from selenium import webdriver              #### webdriver links up with the browserand performs the necessary actions.
from selenium.webdriver.common.keys import Keys         #### Keys is a class that contains keys that we can use to simulate keystrokes.
import time

##### EXPLICIT WAIT IMPORTS #####   
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tensorboard import summary



## Open the website
def start():
    global company_name, driver
    PATH = '/Users/eben.emmanuel/Downloads/chromedriver'
    driver = webdriver.Chrome(PATH)             #### Webbrowser is Chrome and the webdriver is in the Path specified.

    ## Input Company Name from user --> eg: Facebook or Open Financial Technologies
    company_name = input("Enter your Company Name: ").lower()
    company_name = company_name.replace(' ','+')

    driver.get(f'https://www.google.com/search?q={company_name}')
    main()


def main():
    try:
        for article in driver.find_elements_by_xpath('//div[@ class= "jtfYYd"]'):
            try:
                link = article.find_element_by_xpath('.//div[@ class= "TbwUpd NJjxre"]/cite').text
                name = article.find_element_by_xpath('.//h3[@ class= "LC20lb MBeuO DKV0Md"]').text
            except:
                pass

            variables = ["VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf", "VwiC3b MUxGbd yDYNvb lyLwlc", "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]
            for i in variables:
                try:
                    content = article.find_element_by_xpath(f'.//div[@ class= "{i}"]').text
                except:
                    pass

            print(link)
            print(name)
            print(content)
            print()

        
        for article in driver.find_elements_by_xpath('//div[@ class= "tF2Cxc"]'):
            link = article.find_element_by_xpath('.//div[@ class= "TbwUpd NJjxre"]/cite').text
            name = article.find_element_by_xpath('.//h3[@ class= "LC20lb MBeuO DKV0Md"]').text
            content = article.find_element_by_xpath('.//div[@ class= "IsZvec"]').text
            
            print(link)
            print(name)
            print(content)
            print()


    except Exception as e:
        print(e.with_traceback)

    else:
        try:        ##### REMOVE THIS Try-Except block when the we want to scrape only the first page. #####
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Next")))
            element.click()
            main()
        
        except:
            print('There are no more pages to extract information from')
            time.sleep(5)

            ## Close the browser
            driver.quit()

            question = input('Do you want to Continue? yes/no').lower()
            if question == 'yes':
                start()
            else:
                pass



if __name__ == '__main__':
    start()