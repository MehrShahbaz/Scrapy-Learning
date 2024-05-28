import requests
import json
from bs4 import BeautifulSoup

# Constant to use for printing separation lines
breakPrint = "\n==========================================================================================\n"
# HTTP status code for a successful response
response_ok = 200


def custom_print(data, endPrint=False):
    """
    Print data with a custom separator before and after the content.
    If endPrint is True, print the separator after the content as well.
    """
    print(breakPrint)
    print(data)
    if endPrint:
        print(breakPrint)


def print_list(data):
    """
    Print each item in the list using custom_print function.
    """
    for x in data:
        custom_print(x)
    print(breakPrint)


def write_in_file(data, file_name):
    """
    Write data to a file in JSON format. If an error occurs, print an error message.
    """
    try:
        f = open(file_name, "w")
        json.dump(data, f)
        f.close()
    except:
        print(f"Error Writing to the file: {file_name}")


def fetch_page(url):
    """
    Fetch the HTML content of a given URL using requests and parse it with BeautifulSoup.
    If an error occurs, print an error message and return None.
    """
    try:
        response = requests.get(url)
        if response.status_code != response_ok:
            raise Exception("Bad Response")
        return BeautifulSoup(response.text, "html.parser")
    except:
        print(f"Error fetching the URL: {url}")
        return None
