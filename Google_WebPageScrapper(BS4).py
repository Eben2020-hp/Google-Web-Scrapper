## Install necessary packages
# pip install beautifulsoup4
# pip install lxml
# pip install requests

## Import necessary packages
from asyncore import compact_traceback
import requests                 ### Request information from a website
from bs4 import BeautifulSoup

# i = 1              ### Variable to keep track of the page number.

def start():
    global company_name
    company_name = input("Enter your Company Name: ").lower()
    company_name = company_name.replace(' ','+')
    url_request()

def url_request():
    global url
    url = [f'https://www.google.com/search?q={company_name}']

    ## Request information from a website.
    html_text = requests.get(f'{url[-1]}', headers= {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}).text      ### In order to get the HTML text from the website.
    global soup
    soup = BeautifulSoup(html_text, 'lxml')
    main()

def main():
    pages = soup.find_all('div', class_= ['g tF2Cxc','tF2Cxc'])
    try:
        for page in pages:
            page_link = page.find('cite', class_= ['iUh30 tjvcx','iUh30 qLRx3b tjvcx']).text
            page_name = page.find('h3', class_="LC20lb MBeuO DKV0Md").text
            page_content = page.find('div', class_= ["VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf", "IsZvec", "VwiC3b MUxGbd yDYNvb lyLwlc", "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]).text

            print(f"Page Link: {page_link}, \n Page Name: {page_name}, \n Content: {page_content}")
            print("\n")

    except Exception as e:
        print(e.with_traceback)

    else:
        ##### Uncomment these lines when the we want to scrape all the pages (Properly indent the start() function also). #####

        # try:
        #     global i
        #     i += 1
        #     next_pages = soup.find_all('table', class_= ['AaVjTc'])
        #     for next_page in next_pages:
        #         page_nextlink = next_page.find('a', attrs= {'aria-label': f"Page {i}", "class": "fl"})['href']
        #         new_url =  'https://www.google.com' + page_nextlink

        #         url.append(new_url)
        #         url_request()

        # except: 
        #     print('There are no more pages to extract information from')
        
        start()


if __name__ == '__main__':
    start()