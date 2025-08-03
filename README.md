# NLP Bigram Language Model with GUI

## Description
This project implements a bigram language model (trained on a repeated classic paragraph) and exposes it via a web GUI using Flask. Users type a word, get the most common next words, and see an example predictive sentence.

## Files
- `app.py` : Flask backend with bigram model logic.
- `templates/index.html` : Frontend HTML form and display.
- `static/style.css` : Styling for the GUI.

## Requirements
- Python 3.x
- Flask (install via `pip install flask`)

## How to run
1. Open terminal in this project directory.
2. Install Flask: `pip install flask`
3. Run: `python app.py`
4. Open browser at `http://127.0.0.1:5000/`
5. Enter a word and press Predict.

## Example
Input: `mr`
Output: Suggestions like "bennet", "is", etc., and a sample sentence built from the highest-probability bigram chain.

## Submission
Zip the folder and submit. Optionally include this README as `readme.txt`.

Submitted by: Syam Darapuneni
Date: 2025-08-03
