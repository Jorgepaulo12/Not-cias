from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_latest_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=0c340072912c4e349fa3cae9af07c979"
    response = requests.get(url)
    data = response.json()
    if 'articles' in data:
        articles = data['articles']
        news_list = []
        for article in articles:
            title = article['title']
            source = article['source']['name']
            image_url = article['urlToImage']
            published_at = article['publishedAt']
            news_list.append({'title': title, 'source': source, 'image_url': image_url, 'published_at': published_at})
        return news_list
    else:
        return []

def search_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey=0c340072912c4e349fa3cae9af07c979"
    response = requests.get(url)
    data = response.json()
    if 'articles' in data:
        articles = data['articles']
        news_list = []
        for article in articles:
            title = article['title']
            source = article['source']['name']
            image_url = article['urlToImage']
            published_at = article['publishedAt']
            news_list.append({'title': title, 'source': source, 'image_url': image_url, 'published_at': published_at})
        return news_list
    else:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        news_list = search_news(query)
    else:
        news_list = get_latest_news()
        query = None
    return render_template('index.html', latest_news=news_list, query=query)

if __name__ == '__main__':
    app.run(debug=True)
