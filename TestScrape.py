import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

custom_headers = {
    "accept-language": "en-GB,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
}


def get_product_info(url):
    response = requests.get(url, headers=custom_headers)
    if response.status_code != 200:
        print("Error in getting webpage")
        exit(-1)

    soup = BeautifulSoup(response.text, "lxml")

    title_element = soup.select_one("#productTitle")
    title = title_element.text.strip() if title_element else None

    price_element = soup.select_one("#price_inside_buybox")
    price = price_element.text.strip() if price_element else None

    rating_element = soup.select_one("#acrPopover")
    rating_text = rating_element.attrs.get("title") if rating_element else None
    rating = rating_text.replace("out of 5 stars", "") if rating_text else None

    image_element = soup.select_one("#landingImage")
    image = image_element.attrs.get("src") if image_element else None

    description_element = soup.select_one("#productDescription")
    description = description_element.text.strip() if description_element else None

    review_elements = soup.select("div.review")

    scraped_reviews = []

    for review in review_elements:
        r_author_element = review.select_one("span.a-profile-name")
        r_author = r_author_element.text if r_author_element else None

        r_rating_element = review.select_one("i.review-rating")
        r_rating = r_rating_element.text.replace("out of 5 stars", "") if r_rating_element else None

        r_title_element = review.select_one("a.review-title")
        r_title_span_element = r_title_element.select_one("span:not([class])") if r_title_element else None
        r_title = r_title_span_element.text if r_title_span_element else None

        r_content_element = review.select_one("span.review-text")
        r_content = r_content_element.text if r_content_element else None

        r_date_element = review.select_one("span.review-date")
        r_date = r_date_element.text if r_date_element else None

        r_verified_element = review.select_one("span.a-size-mini")
        r_verified = r_verified_element.text if r_verified_element else None

        r = {
            "author": r_author,
            "rating": r_rating,
            "title": r_title,
            "content": r_content,
            "date": r_date,
            "verified": r_verified
        }

        scraped_reviews.append(r)

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "image": image,
        "description": description,
        "url": url,
    }


def parse_listing(listing_url):
    response = requests.get(listing_url, headers=custom_headers)
    print(response.status_code)
    soup_search = BeautifulSoup(response.text, "lxml")
    link_elements = soup_search.select("[data-asin] h2 a")
    page_data = []
    for link in link_elements:
        full_url = urljoin(listing_url, link.attrs.get("href"))
        print(f"Scraping product from {full_url[:100]}", flush=True)
        product_info = get_product_info(full_url)
        page_data.append(product_info)

    next_page_el = soup_search.select_one('a:-soup-contains("Next")')
    if next_page_el:
        next_page_url = next_page_el.attrs.get('href')
        next_page_url = urljoin(listing_url, next_page_url)
        print(f'Scraping next page: {next_page_url}', flush=True)
        page_data += parse_listing(next_page_url)

    return page_data


def main():
    data = []
    search_url = "https://www.amazon.in/s?rh=n%3A78382736031&fs=true&ref=lp_78382736031_sar"
    data = parse_listing(search_url)
    df = pd.DataFrame(data)
    df.to_json("apple.json", orient='records')


if __name__ == '__main__':
    main()