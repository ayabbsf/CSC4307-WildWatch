import os

weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'
weather_api_key = os.environ['ENV_weather'] # environment variable defined at Heroku Config Var level
yolo_api_url = 'https://wildfire-project-backend.herokuapp.com/predict'
