# Basic Weather App — Oasis Infobyte Internship

## Project Overview

A Python-based weather application developed as part of my Oasis Infobyte Python Programming Internship. It allows users to search for weather information through a simple graphical interface.

## Features

- Search weather by city name.
- Search by Pakistani postal code.
- Display current weather conditions.
- Display weather forecasts.
- Retrieve weather data using the OpenWeather API.
- Provide a simple graphical interface using Tkinter.
- Handle common errors, including invalid locations and connection issues.

## Technologies Used

- **Python** — Main programming language.
- **Tkinter** — Graphical user interface.
- **OpenWeather API** — Weather data provider.
- **Requests** — HTTP requests to the weather API.
- **python-dotenv** — Loads environment variables from a `.env` file.

## Project Structure

```text
basic-weather-app-oasis-internship/
├── weather_app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

- Python installed on your system.
- An OpenWeather API key.
- An internet connection.

### Steps

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project directory and add your API key:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key. **Do not upload your real API key to GitHub.**

5. Run the application:

```bash
python weather_app.py
```

6. Enter a city name or a supported Pakistani postal code to view weather information.

## Error Handling

The application handles common issues such as invalid locations, unsuccessful API requests, and connection timeouts.

## Limitations

- Weather information depends on internet connectivity and API availability.
- API usage may be subject to the provider's plan and rate limits.
- Forecast availability depends on the API endpoint and account access.

## Future Improvements

- Add more weather details and forecast visualizations.
- Improve the interface and user experience.
- Add options to save frequently searched locations.

## Author

Developed as part of the Oasis Infobyte Python Programming Internship.