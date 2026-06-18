# 🌐 API Integration & JSON Handling
> Task 2 — Alfido Tech Python Developer Internship

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API-FF6B6B?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-4CAF50?style=flat)

---

## 📌 About
A Python tool that fetches **live Weather & News data** from real APIs, applies filters, and exports results to **JSON & CSV** files.

---

## ✅ Requirements Covered

| Requirement | Status |
|---|---|
| Fetch data using Requests library | ✅ |
| Parse JSON responses | ✅ |
| Apply filtering / search logic | ✅ |
| Handle API errors (try-except) | ✅ |

---

## 📁 Project Structure
```
Task2_API_Integration/
├── main.py           # Main runner
├── weather_api.py    # Fetches live weather
├── news_api.py       # Fetches latest news
├── json_handler.py   # Save/load JSON
├── csv_handler.py    # Export to CSV
├── utils.py          # Filter & search logic
└── output/           # Auto-generated results
    ├── weather_data.json
    ├── weather_data.csv
    ├── news_data.json
    └── news_data.csv
```

---

## ⚙️ Setup & Run

```bash
# Install dependency
pip install requests

# Run the project
python main.py
```

---

## 📤 Sample Output
```
✅ Delhi, India       → 38°C | Wind: 12.5 km/h
✅ London, UK         → 18°C | Wind: 20.1 km/h
✅ New York, US       → 28°C | Wind: 15.3 km/h

🔍 Cities above 25°C: Delhi, New York

📰 Top News: "Python 3.13 Released..." — TechCrunch

[SAVED] output/weather_data.json
[SAVED] output/weather_data.csv
[SAVED] output/news_data.json
[SAVED] output/news_data.csv
```

---

## 🛠️ Tech Stack
`Python` `Requests` `JSON` `CSV` `Open-Meteo API` `GNews API`

---

## 👩‍💻 Author
**Ishita Gupta** — Python Developer Intern @ Alfido Tech  
🐙 [GitHub](https://github.com/ishitagupta221401-crypto) • 💼 [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---
<div align="center">Made with ❤️ during Alfido Tech Internship</div>
