from bs4 import BeautifulSoup
import re
import selenium
from selenium import webdriver
import time
import pandas as pd

output = {'key':'value'}

#List of urls to iterate over
url = [
"https://adviserinfo.sec.gov/Firm/170562",
"https://adviserinfo.sec.gov/Firm/161538",
"https://adviserinfo.sec.gov/Firm/167677",
"https://adviserinfo.sec.gov/Firm/109779",
"https://adviserinfo.sec.gov/Firm/282721",
"https://adviserinfo.sec.gov/Firm/160721"
        ]

driver = webdriver.Chrome()

for i in url:
    #Go from Investment Adviser Firm Summary page to View Form ADV by Section
    driver.get(i)
    elem = driver.find_element_by_link_text("View Form ADV By Section")
    elem.click()
    driver.switch_to.window(driver.window_handles[-1])
    form = driver.page_source
    soup = BeautifulSoup(form, "lxml")

    # find all the tags with red text
    tags = list(soup.find_all('span', {'class': 'PrintHistRed'}))
    # find all the radio checkbox icons (need to look into this code and see if it works correctly)
    tags.extend(list(soup.find_all('img', alt=re.compile('Radio|Checkbox')))[2:])  # 2: skip "are you an adviser" at the top
    # extend the script to add a list comprehension that finds "No Information filed"
    tags.extend([t.parent for t in soup.find_all(text="No Information Filed")])

    # original code: for entry in sorted(tags)
    for entry in (tags):
        if entry.name == 'img':
            alt = entry['alt']
            if 'Radio' in alt:
                output['key'] = ('NO' if 'not selected' in alt else 'YES')
            else:
                output['value'] = ('O' if 'not checked' in alt else 'X')
        else:
            output['value'] = entry.text

    # Go from View Form ADV section to Item 7.B
    elem = driver.find_element_by_link_text("Item 7.B Private Fund Reporting")
    elem.click()
    driver.switch_to.window(driver.window_handles[-1])
    form = driver.page_source
    soup = BeautifulSoup(form, "lxml")

    # find all the tags with red text
    tags = list(soup.find_all('span', {'class':'PrintHistRed'}))
    # find all the radio checkbox icons (need to look into this code and see if it works correctly)
    tags.extend(list(soup.find_all('img', alt=re.compile('Radio|Checkbox')))[2:])# 2: skip "are you an adviser" at the top
    # extend the script to add a list comprehension that finds "No Information filed"
    tags.extend([t.parent for t in soup.find_all(text="No Information Filed")])

    #original code: for entry in sorted(tags)
    for entry in tags:
        if entry.name == 'img':
            alt = entry['alt']
            if 'Radio' in alt:
                output['key'] = ('NO' if 'not selected' in alt else 'YES')
            else:
                output['value'] = ('O' if 'not checked' in alt else 'X')
        else:
            output['value'] = entry.text

    print(output)