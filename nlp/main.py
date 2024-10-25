from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  data = request.json
  text = data['text']
  sentiment_scores = sia.polarity_scores(text)

  if sentiment_scores['compound'] >= 0.05:
    sentiment = 'Positive'
  elif sentiment_scores['compound'] <= -0.05:
    sentiment = 'Negative'
  else:
    sentiment = 'Neutral'
  return jsonify({'sentiment':sentiment})

if __name__ == '__main__':
  app.run(debug = True)