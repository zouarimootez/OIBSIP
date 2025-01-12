def extract_city(text):
    """Extracts the city name from a sentence."""
    if "in" in text:
        return text.split("in ")[-1]
    return "New York"  # Default city