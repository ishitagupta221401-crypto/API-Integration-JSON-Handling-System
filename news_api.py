import requests

def get_news(keyword, max_results=10):
    """
    Fetches latest news headlines using GNews API (free tier)
    Filters articles by keyword search
    """
    try:
        # Using GNews free API
        url = (
            f"https://gnews.io/api/v4/search?"
            f"q={keyword}&lang=en&max={max_results}"
            f"&apikey=26ccf5960fa43dde8d110452e858591f"  # Replace with your free key from gnews.io
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            print(f"[INFO] No news found for '{keyword}'")
            return []

        # Parse only needed fields
        parsed = []
        for article in articles:
            parsed.append({
                "title": article.get("title", "N/A"),
                "source": article.get("source", {}).get("name", "N/A"),
                "published_at": article.get("publishedAt", "N/A"),
                "url": article.get("url", "N/A"),
                "description": article.get("description", "N/A")
            })

        return parsed

    except requests.exceptions.ConnectionError:
        print("[ERROR] No internet connection.")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"[HTTP ERROR] {e}")
        return []
    except Exception as e:
        print(f"[ERROR] {e}")
        return []