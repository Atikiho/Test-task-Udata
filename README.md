# Mcdonald's Scrapper with API
This program fetches all the products from McDonald's menu by scraping their website and provides easy access to the data via a RESTful API.

## Installation

```
git clone https://github.com/Atikiho/Test-task-Udata.git
cd Test-task-Udata
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn API.main:app --reload
```

You are ready to use!

Documentation is available on http://127.0.0.1:8000/docs

## Features
 - Scrapping Mcdonald's full menu page
 - List of all products and their features
 - Page of specific product
 - Page of specific field of specific product

## Technologies
 - Python
 - Scrapy
 - FastAPI
 - Pydantic
 - Pytest
