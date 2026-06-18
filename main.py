from weather_api import get_weather
from news_api import get_news
from json_handler import save_to_json
from csv_handler import save_to_csv
from utils import filter_weather_by_temp, search_news_by_keyword

def main():
    print("=" * 50)
    print("   🌐 API Integration & JSON Handling Tool")
    print("=" * 50)

    # ── WEATHER SECTION ──────────────────────────────
    print("\n📍 Fetching weather for multiple cities...\n")
    cities = ["Delhi", "London", "New York", "Tokyo", "Sydney"]
    weather_results = []

    for city in cities:
        data = get_weather(city)
        if data:
            weather_results.append(data)
            print(f"  ✅ {data['city']}, {data['country']} → "
                  f"{data['temperature_C']}°C | "
                  f"Wind: {data['wind_speed_kmh']} km/h")

    # Save all weather data to JSON
    save_to_json(weather_results, "weather_data.json")

    # Filter: cities with temp above 25°C
    print("\n🔍 Filtering cities with temperature > 25°C:")
    hot_cities = filter_weather_by_temp(weather_results, min_temp=25)
    for w in hot_cities:
        print(f"  🌡️  {w['city']}: {w['temperature_C']}°C")

    # Save filtered results to CSV
    if weather_results:
        save_to_csv(
            weather_results,
            "weather_data.csv",
            fieldnames=list(weather_results[0].keys())
        )

    # ── NEWS SECTION ─────────────────────────────────
    print("\n📰 Fetching latest news on 'Python programming'...\n")
    news = get_news("Python programming", max_results=5)

    for i, article in enumerate(news, 1):
        print(f"  {i}. {article['title']}")
        print(f"     Source: {article['source']} | {article['published_at']}\n")

    # Save news to JSON
    save_to_json(news, "news_data.json")

    # Search filter on news
    print("🔍 Searching news containing 'AI':")
    filtered_news = search_news_by_keyword(news, "AI")
    for a in filtered_news:
        print(f"  📌 {a['title']}")

    # Save news to CSV
    if news:
        save_to_csv(
            news,
            "news_data.csv",
            fieldnames=list(news[0].keys())
        )

    print("\n✅ Task 2 Complete! Check the output/ folder.")
    print("=" * 50)

if __name__ == "__main__":
    main()