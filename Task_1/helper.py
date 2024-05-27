import requests
import json
import re
from bs4 import BeautifulSoup

breakPrint = "\n==========================================================================================\n"
response_ok = 200


def custom_print(data, endPrint=False):
    print(breakPrint)
    print(data)
    if endPrint:
        print(breakPrint)


def print_list(data):
    for x in data:
        custom_print(x)
    print(breakPrint)


def write_in_file(data, file_name):
    try:
        f = open(file_name, "w")
        json.dump(data, f)
        f.close()
    except:
        print(f"Error Writting to the file: {file_name}")


def find_next_page_url(soup, base_url):
    next_li = soup.select_one(".next a")

    return base_url + next_li.get("href") if next_li else None


def remove_character(string, char):
    result = re.sub(char, "", string)

    return result


def format_quote(data):
    data = remove_character(data, "”")
    data = remove_character(data, "“")

    return data


def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code != response_ok:
            raise Exception("Bad Response")

        return BeautifulSoup(response.text, "html.parser")
    except:
        print(f"Error fetching the URL: {url}")
        return None


def extract_quotes(soup, url):
    return [
        {
            "quote": format_quote(div.select_one("span.text").text),
            "author": div.select_one(".author").text,
            "tags": [x.text for x in div.select(".tag")],
            "url": url,
        }
        for div in soup.select(".quote")
    ]
