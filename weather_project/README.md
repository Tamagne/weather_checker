# Weather Checker Website 🌦️

A dynamic and user-friendly website built using Django that allows users to check real-time weather conditions for any city in the world. The site features a sleek, animated interface and integrates the OpenWeatherMap API for accurate and up-to-date weather data.

---

## Features 🚀

1. **Real-Time Weather Data**: Displays current weather conditions including:
   - Temperature (in Celsius and Fahrenheit)
   - Humidity
   - Wind speed
   - Weather description (e.g., clear sky, rain, etc.)
   - Weather icons

2. **City Search**: Users can search for weather data for any city worldwide.

3. **Responsive Design**: Works seamlessly on all devices (desktop, tablet, mobile).

4. **Animated Interface**: Includes CSS animations for a visually appealing user experience.

5. **Error Handling**: Displays user-friendly error messages for invalid city names or API issues.

---

## Installation ⚙️

Follow these steps to run the project locally:

### Prerequisites
- Python (3.10 or later)
- Pip (Python package installer)
- Django (5.1 or later)
- OpenWeatherMap API key

### Steps
1. Clone the repository:
   ```bash
   git clone <https://github.com/Tamagne/weather_checker.git>
   cd weather_project
Create a virtual environment:


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Configure environment variables:

Create a .env file in the project root directory:
env

OPENWEATHER_API_KEY=your_openweathermap_api_key
Replace your_openweathermap_api_key with your OpenWeatherMap API key.
Run migrations:


python manage.py migrate

Start the development server:


python manage.py runserver
Access the website: Open your browser and visit http://127.0.0.1:8000/.

Usage 💻
Search for Weather:

Enter a city name in the search bar on the home page.
Click "Check Weather" to view real-time weather details.
Error Handling:

If the city name is invalid, an error message will be displayed.
Project Structure 🗂️
bash
Copy
Edit
weather_project/
├── weather_project/
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project-level URL routing
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
├── weather/
│   ├── views.py             # Main application views
│   ├── models.py            # Application models
│   ├── urls.py              # Application-specific URL routing
│   ├── templates/           # HTML templates
│   │   └── weather/
│   │       └── weather_home.html
│   ├── static/              # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css
│   │   └── images/
│   │       └── weather-icons/
└── .env                     # Environment variables (hidden)
API Integration 🌐
This project integrates with the OpenWeatherMap API to fetch weather data. Ensure you have a valid API key and include it in your .env file.

Screenshots 📸

Description of the home page with a search bar and animated weather icons.


Detailed weather information displayed for the searched city.

Technologies Used 🛠️
Backend: Django
Frontend: HTML, CSS, JavaScript
API: OpenWeatherMap API
Future Enhancements 🌟
Add a feature to show weather forecasts for the next 7 days.
Implement user authentication for saving favorite cities.
Add support for multiple languages.
Enhance animations and design.




Acknowledgments 🙏
Django Documentation
OpenWeatherMap API
Author 🖊️
Tamagne Gedefaye
GitHub Profile
tamagne13@gmail.com


