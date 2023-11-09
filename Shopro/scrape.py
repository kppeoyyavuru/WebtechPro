from bs4 import BeautifulSoup

# Read the HTML file
with open('index2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div', class_='sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-4-of-20 sg-col-4-of-24 s-list-col-left')

# Iterate through each div element and extract the required information
for div in div_elements:
    # Find the image element
    img_element = div.find('img', class_='s-image')
    
    # Find the price element
    price_element = div.find('span', class_='a-price-whole')
    
    # Find the star rating element
    star_rating_element = div.find('span', class_='a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom')
    
    # Find the rating span within the star rating element
    rating_span = star_rating_element.find('span', class_='a-icon-alt') if star_rating_element else None
    
    # Print the extracted information
    print("Image URL:", img_element['src'] if img_element else "N/A")
    print("Price:", price_element.text if price_element else "N/A")
    print("Rating:", rating_span.text if rating_span else "N/A")
    print("\n")
