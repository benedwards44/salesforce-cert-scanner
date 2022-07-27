import constants
import re
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Load Chrome drive
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# the CSV file to save
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

    certs = soup.find_all(text=re.compile('Salesforce Certified')) 

    for cert in certs:

        cert_name = cert.string 

        # Remove the paragraph at the end, bit of a back
        if len(cert_name) < 400:
            writer.writerow([practioner_name, cert_name, ''])

# Close browser
browser.close()