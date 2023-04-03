from flask import Flask, render_template, request, jsonify
from trustpilot_scraper import scrape_reviews
import os

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/scrape_reviews', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data['url']
    num_pages = int(data['num_pages'])
    star_rating = int(data['star_rating'])
    summary_prompt = data['summary_prompt']

    reviews = scrape_reviews(url, num_pages, star_rating, summary_prompt)
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
