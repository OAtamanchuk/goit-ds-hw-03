## Description
This repository contains a homework assignment focused on working with MongoDB.  
The project consists of two main parts:
1. Implementation of CRUD (Create, Read, Update, Delete) operations using PyMongo.
2. Web scraping of quotes and authors from the website quotes.toscrape.com with further data export to JSON files and import into MongoDB Atlas.

## Technologies
- **Python**
- **MongoDB**
- **MongoDB Atlas**
- **PyMongo** - for database operations
- **BeautifulSoup / Requests** - for web scraping
- **JSON** - for data storage and import

## Functionality
### Part 1 MongoDB CRUD
- Creation of a MongoDB database with documents describing cats
- Each document contains:
  - name
  - age
  - list of features
- Python script (main.py) that implements:
  - reading all records from the collection
  - searching a cat by name
  - updating a cat’s age by name
  - adding a new feature to a cat
  - deleting a cat by name
  - deleting all records from the collection
- Handling of possible database exceptions
- Clear and structured functions for each operation

### Part 2 Web Scraping 
- Scraping all quotes from quotes.toscrape.com across all pages
- Scraping detailed information about authors
- Creation of two JSON files:
  - quotes.json - quotes, authors, and tags
  - authors.json - author details (name, birth date, location, description)
- Creation of MongoDB Atlas cloud database
- Import of scraped data into MongoDB collections:
  - quotes
  - authors

## Links
- **GitHub Repository:**  
  https://github.com/OAtamanchuk/goit-ds-hw-03
