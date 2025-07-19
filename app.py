from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)

# Load quotes from JSON
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

@app.route('/')
def home():
    return jsonify({"message": "Quote Generator API is running"}), 200

@app.route('/quote', methods=['GET'])
def get_random_quote():
    mood = request.args.get('mood')
    if mood:
        filtered_quotes = [q for q in quotes if q['mood'].lower() == mood.lower()]
        if not filtered_quotes:
            return jsonify({"error": f"No quotes found for mood '{mood}'"}), 404
        return jsonify(random.choice(filtered_quotes)), 200
    else:
        return jsonify(random.choice(quotes)), 200

@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes), 200

@app.route('/add-quote', methods=['POST'])
def add_quote():
    new_quote = request.get_json()
    quotes.append(new_quote)
    with open('quotes.json', 'w') as f:
        json.dump(quotes, f, indent=4)
    return jsonify({"message": "Quote added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
