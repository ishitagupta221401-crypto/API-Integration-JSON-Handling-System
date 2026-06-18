def filter_weather_by_temp(weather_list, min_temp=None, max_temp=None):
    """Filter weather results by temperature range"""
    filtered = []
    for w in weather_list:
        temp = w.get("temperature_C", 0)
        if min_temp is not None and temp < min_temp:
            continue
        if max_temp is not None and temp > max_temp:
            continue
        filtered.append(w)
    return filtered

def search_news_by_keyword(news_list, keyword):
    """Search news articles by keyword in title or description"""
    keyword = keyword.lower()
    return [
        article for article in news_list
        if keyword in article.get("title", "").lower()
        or keyword in article.get("description", "").lower()
    ]