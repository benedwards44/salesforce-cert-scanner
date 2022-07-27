import constants
import re
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Load Chrome drive
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# The CSV output to save
csv_file = open('all_certs.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Name', 'Certification', 'Date'])

for practioner_name, search_string in constants.PRACTITIONERS:

    # Retrieve URL 
    url = constants.URL_PREFIX + search_string

    # Load in the URL
    browser.get(url)

    # Load the Soup to process the HTML
    soup = BeautifulSoup(browser.page_source, "html.parser")

    cert_divs = soup.find_all(text=re.compile('Salesforce Certified')) 

    # Retrieve all the cert names
    for cert_div in cert_divs:

        # Load the cert name
        cert_name = cert_div.string 

        # Remove the paragraph at the end, bit of a hack to be honest
        if len(cert_name) < 400:

            # Retrieve the cert date
            cert_date = cert_div.find_next('div').string

            # Write Row to CSV
            writer.writerow([practioner_name, cert_name, cert_date])    

browser.close()