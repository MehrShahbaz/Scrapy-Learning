from timeit import default_timer as timer
import tracemalloc
from helper import (
    fetch_page,
    find_next_page_url,
    custom_print,
    write_in_file,
    extract_quotes,
    print_execution_time,
    print_memory_use,
    convert_to_mbs,
)

# Method to get all the quotes from the URL
# Returns a list of quotes
def scrape_quotes(base_url):
    current_url = base_url
    data = []
    while current_url:
        # Fetch the page and parse it with BeautifulSoup
        soup = fetch_page(current_url)
        if soup:
            # Extract quotes from the page and add them to the data list
            data.extend(extract_quotes(soup, current_url))
            custom_print("Current Url: " + current_url, True)
            # Find the URL for the next page
            current_url = find_next_page_url(soup, base_url)
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
print_memory_use(convert_to_mbs(current), convert_to_mbs(peak))
