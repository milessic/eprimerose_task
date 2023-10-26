# Simple Currency Database
This is a Django  currency exchange database. and basic admin interface to read data from local database.

# API Documentation
This REST API is a simple currency exchange database.

## Endpoints
### /currency/
Fetches history records. It takes query parameters like:
- limit (int or 'none', by default returns 500 items)
- order (ASC or DESC), in case of not supported value, DESC is applied
- any other valid django filters


    get(/api/currency/) # returns last 500 records
    get(/api/currency/?limit=3&order=ASC) # returns first 3 records
    get(/api/currency/?limit=none&order=ASC) # returns all records ordered by id ASC
    get(/api/currency/?open_rate__gte=1) # returns all records, where open rate was greater oreuals to 1

### /currency/{base}/{quote}/
Fetches data from Yahoo for currency pair rate and returns the open rate. Saves the search in the history with the timestamp.

# Tools and 3rd party libraries used
* Django REST Framework - I decided on DRF, because it has great documentation, is a powerful full-stack tool and has a big community.
* yfinance - I checked on this, and kept with it.
* SQLite - this is built in database that does the job for such purposes
* django-admin-rangefilter - it's a great filtering app for django

# Environment setup
It is recommended to use python virtual environment
* Install Python 3.11 or higher
* Install packages from requirements.txt using pip
* use django makemigration to setup sqlite database
* create superuser
