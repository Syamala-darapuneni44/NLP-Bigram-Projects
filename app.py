import tkinter as tk
from tkinter import ttk
from nltk.corpus import movie_reviews
from nltk import word_tokenize, bigrams
from collections import defaultdict, Counter
from fractions import Fraction
import nltk

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('movie_reviews')

# Load IMDB movie reviews corpus
documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
corpus_text = ' '.join(documents)
tokens = word_tokenize(corpus_text.lower())

# Build Bigram Model
bigram_model = defaultdict(Counter)
for w1, w2 in bigrams(tokens):
    bigram_model[w1][w2] += 1

# Function to get next word predictions with fractional probabilities
def get_next_word_probs(word):
    word = word.lower()
    next_words = bigram_model.get(word, {})
    total = sum(next_words.values())
    sorted_probs = sorted(next_words.items(), key=lambda x: x[1], reverse=True)
    return [(w, f"{Fraction(count, total)}") for w, count in sorted_probs[:5]]

# Function to generate sentence using bigram predictions
def generate_sentence(seed, max_words=10):
    seed = seed.lower()
    result = [seed]
    current = seed
    for _ in range(max_words - 1):
        next_words = bigram_model.get(current)
        if not next_words:
            break
        next_word = max(next_words, key=next_words.get)
        result.append(next_word)
        current = next_word
    return ' '.join(result)

# GUI Setup
def predict_next_words():
    input_word = entry.get().strip()
    output_text.delete('1.0', tk.END)

    if not input_word:
        output_text.insert(tk.END, "Please enter a word.\n")
        return

    predictions = get_next_word_probs(input_word)
    output_text.insert(tk.END, "🔮 Top Predictions with Probabilities (fractions):\n")
    for word, prob in predictions:
        output_text.insert(tk.END, f"{word} — Probability: {prob}\n")

    sentence = generate_sentence(input_word)
    output_text.insert(tk.END, f"\n✨ Generated Sentence:\n{sentence}")

# GUI Design
root = tk.Tk()
root.title("Bigram Language Model with IMDB Corpus")

frame = ttk.Frame(root, padding=20)
frame.grid()

label = ttk.Label(frame, text="Enter a word:")
label.grid(column=0, row=0)

entry = ttk.Entry(frame, width=30)
entry.grid(column=1, row=0)

button = ttk.Button(frame, text="Predict", command=predict_next_words)
button.grid(column=2, row=0)

output_text = tk.Text(frame, height=15, width=70)
output_text.grid(column=0, row=1, columnspan=3, pady=10)

root.mainloop()
