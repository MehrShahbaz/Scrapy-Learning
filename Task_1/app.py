from timeit import default_timer as timer
import tracemalloc
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/..")

from utils import (
    append_to_list_in_file,
    convert_to_mbs,
    custom_print,
    extract_quotes,
    fetch_page,
    find_next_page_url,
    print_execution_time,
    print_memory_use,
    write_in_file,
)


def scrape_quotes(base_url: str):
    """
    Method to get all the quotes from the URL
    Returns a list of quotes
    """
    current_url = base_url
    data = []
    while current_url:
        soup = fetch_page(current_url)
        if soup:
            data.extend(extract_quotes(soup, current_url))
            custom_print("Current Url: " + current_url, True)
            current_url = find_next_page_url(soup, base_url)
            break
        else:
            break
    return data


# Start the timer and memory tracer
time_start = timer()
tracemalloc.start()

# Base URL for the quotes
base_url = "https://quotes.toscrape.com"

# Get all the quotes from the website
quotes = scrape_quotes(base_url)

# Write the quotes to a file named "data.json"
write_in_file(quotes, "data.json")

# Get the current and peak memory usage
current, peak = tracemalloc.get_traced_memory()

# Stop the memory tracer and end the timer
tracemalloc.stop()
time_end = timer()

# Print the execution time and memory usage in MB
print_execution_time(time_start, time_end)
append_to_list_in_file("simple", time_end - time_start)
print_memory_use(convert_to_mbs(current), convert_to_mbs(peak))
