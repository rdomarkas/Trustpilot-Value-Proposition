import requests
from bs4 import BeautifulSoup
import random
from summarizer import summarize_review


def scrape_reviews(base_url, num_pages, star_rating, summary_prompt=None):
    all_reviews = []

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

            review_data = {
                "title": title,
                "text": text,
                "date": date,
                "rating": rating
            }

            if rating == str(star_rating) and review_data not in all_reviews:
                all_reviews.append(review_data)

    random_reviews = random.sample(all_reviews, min(10, len(all_reviews)))
    if summary_prompt:
        for review in random_reviews:
            summary = summarize_review(review["text"], prompt=summary_prompt)
            review["summary"] = summary

    return random_reviews
