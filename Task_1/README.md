# Task 1

This python Script scrapes website [Quotes to Scrape](https://quotes.toscrape.com/) 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Description
- After the Usage command is run the website will be scrapped
- A new file (data.json) if not existing will be created
- The data will be stored in the file

## Data Format

```bash
{
    "quote": "String", // The Quote
    "author": "String", // Author Name
    "tags": ["String"], // List of Tags
    "url": "String" // Url on which this tag is present
}
```