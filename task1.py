import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


NASA_API_KEY = "use your api key"
NASA_API_URL = "https://api.nasa.gov/planetary/apod"

def fetch_nasa_apod():
    params = {"api_key": NASA_API_KEY}
    response = requests.get(NASA_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching NASA APOD: {response.status_code}")
        return None

def display_nasa_apod(apod_data):
    if not apod_data:
        print("No NASA APOD data available.")
        return

    title = apod_data["title"]
    explanation = apod_data["explanation"]
    image_url = apod_data["url"]

    print(f"\n🌌 NASA APOD: {title}\n")
    print(explanation)


    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))


        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={"height_ratios": [3, 1]})


        ax1.imshow(img)
        ax1.axis("off")
        ax1.set_title(title, fontsize=12, fontweight="bold")


        ax2.axis("off")
        ax2.text(0.5, 0.5, explanation, fontsize=10, ha="center", va="center", wrap=True)

        plt.tight_layout()
        plt.show()
    else:
        print("Failed to load image.")

def main():

    nasa_apod_data = fetch_nasa_apod()
    display_nasa_apod(nasa_apod_data)

if __name__ == "__main__":
    main()