import python_weather
import asyncio

async def get_weather(city):
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find(city)
    await client.close()
    return f"The temperature in {city} is {weather.current.temperature}°F."