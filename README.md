# salesforce-cert-scanner
Web scraper for retrieving Salesforce certifications for individuals based on their Trailhead link

## Quick Start

Requires virtualenvwrapper to be installed:
https://formulae.brew.sh/formula/virtualenvwrapper


```
mkvirtualenv scanner
pip install -r requirements
python scanner.py
```

Will output a list of individuals from the constants.py file into a CSV file.