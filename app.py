from flask import Flask, render_template, request
from twitter_client import get_tweets
import joblib

app = Flask(__name__)
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiments = []
    if request.method == 'POST':
        query = request.form['query']
        tweets = get_tweets(query)
        X = vectorizer.transform(tweets)
        preds = model.predict(X)
        sentiments = list(zip(tweets, preds))
    return render_template('index.html', sentiments=sentiments)

if __name__ == '__main__':
    app.run(debug=True)