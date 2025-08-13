from flask import Flask, request, jsonify, render_template
import nltk
from nltk.corpus import movie_reviews
from nltk import bigrams, FreqDist

app = Flask(__name__)

nltk.download("punkt")
nltk.download("movie_reviews")

# Load movie review sentences
sentences = movie_reviews.sents()
words = [word.lower() for word in movie_reviews.words()]
unique_words = sorted(set(words))

# Build a bigram model
bigram_model = {}
for sentence in sentences:
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        w1 = w1.lower() if w1 else ""
        w2 = w2.lower() if w2 else ""
        if w1 not in bigram_model:
            bigram_model[w1] = []
        bigram_model[w1].append(w2)

# Convert lists to FreqDist
for word in bigram_model:
    bigram_model[word] = FreqDist(bigram_model[word])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['GET'])
def suggest():
    prefix = request.args.get('prefix', '').lower()
    matches = [w for w in unique_words if w.startswith(prefix)]
    return jsonify(matches[:5])

@app.route('/predict', methods=['GET'])
def predict():
    text = request.args.get('text', '').strip().lower()
    if not text:
        return jsonify([])
    last_word = text.split()[-1]
    # FIX: Use empty FreqDist() instead of {} to avoid AttributeError
    predictions = bigram_model.get(last_word, FreqDist()).most_common(5)
    return jsonify([w for w, _ in predictions])

if __name__ == '__main__':
    app.run(debug=True)
