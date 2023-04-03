import requests
from bs4 import BeautifulSoup

base_url = "https://uk.trustpilot.com/review/katkin.com?page={}"

num_pages = 1  # change this to the number of pages to scrape

# specify the star rating to filter by (1 for 1-star reviews, 5 for 5-star reviews, etc.)
star_rating = 1

for page in range(1, num_pages + 1):
    url = base_url.format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    reviews = soup.find_all("article", {"data-service-review-card-paper": True})

    for review in reviews:
        title = review.find("a", {"data-review-title-typography": True}).text.strip()
        text = review.find("p", {"data-service-review-text-typography": True}).text.strip()
        date = review.find("p", {"data-service-review-date-of-experience-typography": True}).text.strip().split(":")[-1].strip()
        try:
            rating = review.find("div", {"data-service-review-rating": True}).find("img").get("alt").split()[1]
        except AttributeError:
            rating = "N/A"
        
        if rating == str(star_rating):
            print(f"Title: {title}\nText: {text}\nDate: {date}\nRating: {rating}\n")
