from helper import (
    fetch_page,
    find_next_page_url,
    custom_print,
    write_in_file,
    extract_quotes,
)


def scrape_quotes(base_url):
    current_url = base_url
    data = []
    while current_url:
        soup = fetch_page(current_url)
        if soup:
            data.extend(extract_quotes(soup, current_url))
            custom_print("Current Url: " + current_url, True)
            current_url = find_next_page_url(soup, base_url)
        else:
            break
    return data


base_url = "https://quotes.toscrape.com"
quotes = scrape_quotes(base_url)
write_in_file(quotes, "data.json")
