from timeit import default_timer as timer
import multiprocessing
from helper import (
    append_to_list_in_file,
    custom_print,
    extract_quotes,
    fetch_page,
    find_next_page_url,
    print_execution_time,
    write_in_file,
)


def process_page(args):
    base_url, url = args
    soup = fetch_page(url)
    if soup:
        quotes = extract_quotes(soup, url)
        custom_print("Current Url: " + url, True)
        next_url = find_next_page_url(soup, base_url)
        return quotes, next_url
    return [], None


def scrape_quotes(base_url):
    """
    Method to get all the quotes from the URL
    Returns a list of quotes
    """
    current_url = base_url
    data = []
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    while current_url:
        results = pool.map(process_page, [(base_url, current_url)])
        for quotes, next_url in results:
            data.extend(quotes)
            current_url = next_url
    pool.close()
    pool.join()
    return data


if __name__ == "__main__":
    # Start the timer and memory tracer
    time_start = timer()

    # Base URL for the quotes
    base_url = "https://quotes.toscrape.com"

    # Get all the quotes from the website
    quotes = scrape_quotes(base_url)

    # Write the quotes to a file named "data.json"
    write_in_file(quotes, "data.json")

    # Stop the memory tracer and end the timer
    time_end = timer()

    # Print the execution time and memory usage in MB
    print_execution_time(time_start, time_end)
    append_to_list_in_file("multiprocessing", time_end - time_start)
