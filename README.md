# Eprimerose task
This is Django application task repository.

# API Documentation
This REST API is a simple EUR/USD currency exchange database.

## Endpoints
### /currency/
Fetches history records. It takes query parameters like:
- limit (int or 'none', by default returns 500 items)
- order (ASC or DESC), in case of not supported value, DESC is applied
- any other valid django filters


    get(/api/currency/) # returns last 500 records
    get(/api/currency/?limit=3&order=ASC) # returns first 3 records
    get(/api/currency/?limit=none&order=ASC) # returns all records ordered by id ASC
    get(/api/currency/?open_rate__gte=1) # returns all records, where EURUSD rate was greater oreuals to 1

### /currency/EUR/USD/
Fetches data from Yahoo for EUR/USD rate and returns the rage. Saves the search in the history with the timestamp.

# Tools used
* Django REST Framework - I decided on DRF, beacuse it has great documentation, is a powerfull full-stack tool and has a big community.
* yfinance - I checked on this, and kept with it. Also use of yfinance Ticker data needs user to be in the USA, instead of resolving this to work for all countiers I decided to inform user that only US ones are supported. 

# Environment setup
It is recommended to use python virtual environment
* Install Python 3.11 or higher
* Install packages from requirements.txt using pip
* use django makemigration to setup sqlite database