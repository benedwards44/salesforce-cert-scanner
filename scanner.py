import constants
import re
import csv
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Load Chrome drive
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# The CSV output to save
csv_file = open('all_certs.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Name', 'URL', 'Certification', 'Date'])

for search_string in constants.SEARCH_STRINGS:

    # Retrieve URL 
    url = constants.URL_PREFIX + search_string

    print('Processing for URL: ' + url)

    # Load in the URL
    browser.get(url)

    # Load the Soup to process the HTML
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # Not very reliable but seems to be only one div using slds-size--1-of-2 in the current HTML
    try:
        practioner_name = soup.find_all("div", {"class": "slds-size--1-of-2"})[0].string

    except Exception as ex:

        print('Could not retrieve Practitioner Name: ' + str(ex))

        # Set name as search string instead
        practioner_name = search_string

    # Retrieve all the divs that contains "Salesforce Certified..."
    cert_divs = soup.find_all(text=re.compile('Salesforce Certified')) 

    # Retrieve all the cert names
    for cert_div in cert_divs:

        # Load the cert name
        cert_name = cert_div.string 

        # Remove the paragraph at the end, bit of a hack to be honest
        if len(cert_name) < 400:

            # Retrieve the cert date
            cert_date = cert_div.find_next('div').string

            # Re-format date
            cert_date_formatted = datetime.strptime(cert_date, '%B %d, %Y').strftime('%d/%m/%Y')

            # Write Row to CSV
            writer.writerow([practioner_name, url, cert_name, cert_date_formatted])    

browser.close()