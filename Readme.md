
# 📝 Quote Generator API

A lightweight Flask-based REST API that returns inspirational, emotional, and motivational quotes — with mood-based filtering. Built to demonstrate backend development fundamentals including API routing, JSON data handling, and cloud deployment via Render.

---

## 🚀 Features

- 🎯 Get a random quote
- 🎭 Filter quotes by mood using query parameters (`/quote?mood=happy`)
- 🧠 Quotes stored in a structured `quotes.json` file (author, text, mood)
- ☁️ **🔗 [Deployed on Render](https://quotegen-api.onrender.com)**
- 🔧 Easily extendable (add support for author filtering, mood listing, etc.)

---

## 📦 Endpoints

| Method | Route              | Description                                 |
|--------|--------------------|---------------------------------------------|
| GET    | `/`                | Health check message                        |
| GET    | `/quote`           | Get a random quote                          |
| GET    | `/quote?mood=mood` | Get a quote filtered by mood (e.g. sad)     |
| GET    | `/quotes`          | Get all quotes                              |
| POST   | `/add-quote`       | Add a new quote via JSON (see format below) |

---

## 🧪 Example `/add-quote` Request

```json
POST /add-quote
Content-Type: application/json

{
  "text": "The only limit to our realization of tomorrow is our doubts of today.",
  "author": "Franklin D. Roosevelt",
  "mood": "motivational"
}
