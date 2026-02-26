# tools.py

def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def get_weather(city: str) -> str:
    return f"🌤️ Weather in {city}: 28°C, Sunny"