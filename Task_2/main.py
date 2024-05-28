from helper import fetch_page, print_list, custom_print

base_url = "https://priceoye.pk/mobiles?page=20"


soup = fetch_page(base_url)


# data = [
#     div.select_one(".ga-dataset").get("href")
#     for div in soup.select(".category-heading")
#     if div.select_one(".ga-dataset")
# ]

# print_list(data)

data = soup.select_one(".productBox.b-productBox")

# data = [div for div in soup.select(".pagination")]

custom_print(soup.prettify())
