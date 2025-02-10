import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "use your api key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):
    try:
        res = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        if res.status_code == 200:
            return res.json()
        else:
            print("Error fetching data:", res.status_code)
            return None
    except Exception as e:
        print("Request failed:", e)
        return None


def prepare_data(data):
    if not data:
        return None

    return pd.DataFrame([{
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Wind Speed (m/s)": data["wind"]["speed"],
        "Condition": data["weather"][0]["main"]
    }])


def display_table(df):
    if df is None or df.empty:
        print("No data to display.")
        return

    fig, ax = plt.subplots(figsize=(8, 2))
    ax.axis("off")

    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")

    for (i, _), cell in table.get_celld().items():
        if i == 0:
            cell.set_facecolor("#007acc")
            cell.set_text_props(color="white", weight="bold")
        else:
            cell.set_facecolor("#d1ecf1")

    plt.show()


if __name__ == "__main__":
    city = input("Enter city name: ")

    weather_data = fetch_weather(city)

    if weather_data:
        df = prepare_data(weather_data)
        print(df.to_string(index=False))
        display_table(df)
    else:
        print("Could not retrieve weather data.")
