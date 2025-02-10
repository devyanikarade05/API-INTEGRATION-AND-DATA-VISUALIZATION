# API-INTEGRATION-AND-DATA-VISUALIZATION

- **Company:** CODTECH IT SOLUTIONS  
- **Name:** Devyani Karade  
- **Intern ID:** CT08LTW  
- **Domain:** Python  
- **Batch Duration:** February 5th, 2025 - March 5th, 2025  
- **Mentor:** Neela Santhosh  

This repository contains two Python-based API integration projects that fetch real-time data and present it using data visualization techniques.

## Weather Data Application

The weather application provides users with instant weather updates for any city worldwide. By integrating the OpenWeatherMap API, the program retrieves accurate real-time temperature, humidity, wind speed, and weather conditions. The inclusion of Pandas ensures efficient data handling, while Matplotlib enhances data visualization. This allows users to interpret weather conditions effortlessly, making the application useful for daily planning and meteorological analysis.

## NASA APOD Viewer

NASA’s APOD API allows users to explore a new astronomical image each day. This application fetches the latest APOD and displays the high-resolution image with a detailed scientific explanation. The project demonstrates how to retrieve and visualize image-based data while maintaining an interactive and informative user experience.

### 1. Weather Data Fetching and Visualization

This project utilizes the OpenWeatherMap API to retrieve real-time weather information based on a user-provided city name. The script fetches and displays the following weather details:

- **Temperature (°C)**
- **Humidity (%)**
- **Wind Speed (m/s)**
- **Weather Condition**

The data is structured using Pandas and displayed in tabular format. Additionally, Matplotlib is used to visualize the data effectively.

### 2. NASA Astronomy Picture of the Day (APOD) Viewer

This project fetches NASA’s Astronomy Picture of the Day (APOD) using NASA’s API. The script:

- Retrieves the latest APOD, along with its title and explanation.
- Displays the image using the PIL library.
- Uses Matplotlib to present the image alongside its description.

This project provides an interactive way to explore NASA’s daily astronomy images and their scientific explanations.

### Obtain API Keys
- Get an API key from [OpenWeatherMap](https://openweathermap.org/)
- Get an API key from [NASA API](https://api.nasa.gov/)
- Replace `"use your api key"` in the script with your actual API key.

## Usage

### Running the Weather Data Script
- Enter the name of a city when prompted.
- The script will fetch and display weather details for the city.

### Running the NASA APOD Script
- The script will fetch and display NASA's Astronomy Picture of the Day with its explanation.

## Technologies Used

- **Python** - Core programming language
- **Requests** - Fetching data from APIs
- **Pandas** - Data processing and tabular representation
- **Matplotlib** - Data visualization
- **PIL (Pillow)** - Handling and displaying images

## Features

✅ Fetch real-time weather data for any city  
✅ Display weather details in a structured table  
✅ Retrieve and display NASA’s Astronomy Picture of the Day  
✅ Interactive and user-friendly presentation of data  
✅ Simple and easy-to-use command-line interface  


## OUTPUT of NASA Astronomy Picture of the Day (APOD) Viewer: 

![Image](https://github.com/user-attachments/assets/3fef9968-7617-4ffa-9184-080cbcb12615)


## OUTPUT of  Weather Data Fetching and Visualization: 

![Image](https://github.com/user-attachments/assets/a7a17f46-573b-4dc6-bcf9-2a6ccccb43d8)




