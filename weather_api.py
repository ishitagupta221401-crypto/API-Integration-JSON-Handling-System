import requests

def get_weather(city):
    """
    Fetches current weather data for a given city
    using Open-Meteo API (completely free, no key needed)
    """
    try:
        # Step 1: Get coordinates for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            print(f"[ERROR] City '{city}' not found.")
            return None

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        country = geo_data["results"][0]["country"]

        # Step 2: Fetch weather using coordinates
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current_weather=true&hourly=relative_humidity_2m"
        )
        weather_response = requests.get(weather_url, timeout=10)
        #TO
        weather_response = requests.get(weather_url, timeout=15)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current_weather"]

        # Step 3: Parse and return relevant fields
        result = {
            "city": city.title(),
            "country": country,
            "temperature_C": current["temperature"],
            "wind_speed_kmh": current["windspeed"],
            "weather_code": current["weathercode"],
            "is_day": bool(current["is_day"])
        }
        return result

    except requests.exceptions.ConnectionError:
        print("[ERROR] No internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP error: {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return None