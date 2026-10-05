import requests
import tkinter as tk
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
def get_weather():
    location = city_entry.get()

    if not location.strip():
        result_label.config(text="Please enter a city name.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
    "appid": api_key,
   
    "units": "metric"
    }

    if location.strip().isdigit():
        params["zip"] = location.strip() + ",PK"
    else:
        params["q"] = location.strip()

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        result_label.config(text="Could not connect to the weather service.")
        return
    
    data = response.json()

    if data.get("cod") == 401:
        result_label.config(text="Invalid API key.")
        return

    if "main" not in data:
        result_label.config(text="City not found.")
        return
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    try:
        forecast_response = requests.get(
        forecast_url,
        params=params,
        timeout=10
    )
    except requests.exceptions.RequestException:
        result_label.config(text="Could not get forecast data.")
        return

    forecast_data = forecast_response.json()

    daily_forecast = {}
    current_time = datetime.now()
    upcoming_forecasts = []

    for item in forecast_data["list"]:
        forecast_time = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")

        if forecast_time > current_time:
            upcoming_forecasts.append(item)

        date = item["dt_txt"].split(" ")[0]
        temperature = item["main"]["temp"]

        if date not in daily_forecast:
            daily_forecast[date] = {
                "min": temperature,
                "max": temperature
            }
        else:
            daily_forecast[date]["min"] = min(
                daily_forecast[date]["min"], temperature
            )
            daily_forecast[date]["max"] = max(
                daily_forecast[date]["max"], temperature
            )

    next_six_hours = upcoming_forecasts[:2]

    forecast_text = "Next 6 hours\n"

    for item in next_six_hours:
        forecast_time = item["dt_txt"]
        forecast_temperature = item["main"]["temp"]
        forecast_condition = item["weather"][0]["description"]

        forecast_text += (
            f"{forecast_time} → "
            f"{forecast_temperature:.2f} °C → "
            f"{forecast_condition}\n"
    )
    daily_text = "\n5-Day Forecast\n"

    for date, temperatures in list(daily_forecast.items())[:5]:
        daily_text += (
        f"{date} → "
        f"{temperatures['min']:.2f} °C - "
        f"{temperatures['max']:.2f} °C\n"
    )

    forecast_text += daily_text
    forecast_label.config(text=forecast_text)

    temperature_c = data["main"]["temp"]
    temperature_f = (temperature_c * 9/5) + 32
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    if unit_var.get() == "Celsius":
        temperature = f"{temperature_c:.2f} °C"
    else:
        temperature = f"{temperature_f:.2f} °F"

    result_label.config(
        text=f"Temperature: {temperature}\n"
         f"Humidity: {humidity}%\n"
         f"Condition: {condition}\n"
         f"Wind speed: {wind_speed} m/s"
)

window = tk.Tk()
window.title("Weather App")
window.geometry("500x400")

title_label = tk.Label(window, text="Weather App")
title_label.pack(pady=15)

city_label = tk.Label(window, text="Enter City or ZIP code:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack(pady=5)
unit_var = tk.StringVar(value="Celsius")
unit_menu = tk.OptionMenu(window, unit_var, "Celsius", "Fahrenheit")
unit_menu.pack(pady=5)

weather_button = tk.Button(window, text="Get Weather", command=get_weather)
weather_button.pack(pady=5)

result_label = tk.Label(window, text="", pady=20)
result_label.pack()

forecast_label = tk.Label(window, text="", pady=10)
forecast_label.pack()

window.mainloop()