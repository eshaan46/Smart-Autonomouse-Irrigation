# Libraries
import serial
import time
import requests
import numpy as np
# Varibles
flow_rate = 3
# Functions
def serial_read(port,baudrate,timeout):
    ser = serial.Serial(port,baudrate,timeout=timeout)
    time.sleep(1)
    line = ser.readline().decode('utf-8').rstrip()
    ser.close()
    return line
def split_data(line):
    moisture = line
    return float(moisture)
def get_weather(api_key, lat, lon):
    params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
    url = "https://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    
    main = data.get("main", {})
    wind = data.get("wind", {})
    clouds = data.get("clouds", {})
    rain = data.get("rain", {})
    temp = float(main.get("temp", 0.0)),
    humidity = float(main.get("humidity", 0.0))
    pressure = float(main.get("pressure", 0.0))
    wind_speed = float(wind.get("speed", 0.0))
    wind_deg = float(wind.get("deg", 0.0))
    clouds_for = float(clouds.get("all", 0.0))
    rain_1h = float(rain.get("1h", 0.0))
    return rain_1h, clouds_for, wind_deg, wind_speed, pressure, temp[0], humidity
def load_model(model_path):
    import joblib
    model = joblib.load(model_path)
    return model
def get_time_features(sunrise=None, sunset=None):
    current_time = time.localtime()
    hour_of_day = current_time.tm_hour
    day_of_year = current_time.tm_yday
    if sunrise and sunset:
        day_length = (sunset - sunrise) / 3600.0
    else:
        day_length = 0.0
    hour_of_day = int(hour_of_day)
    day_of_year = int(day_of_year)
    day_length = round(day_length, 2)
    return float(hour_of_day),float(day_of_year),float(day_length)
def get_input_features(moisture, weather_data,time_features):
    hour_of_day, day_of_year, day_length = time_features
    rain_1h, clouds_for, wind_deg, wind_speed, pressure, temp, humidity = weather_data
    features = np.array([moisture,temp, humidity, wind_speed,rain_1h,rain_1h,6,pressure,clouds_for,day_length,hour_of_day,day_of_year,5,3,4,26])
    return features
def predict_irrigation(model, features):
    features = features.reshape(1, -1)
    prediction = model.predict(features)
    return prediction
def calculate_irrigation_time(prediction, flow_rate):
    if prediction <= 0:
        return 0
    irrigation_time = prediction / flow_rate
    return round(irrigation_time)
def run_motor(duration):
    import RPi.GPIO as GPIO
    MOTOR_PIN = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_PIN, GPIO.OUT)
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(MOTOR_PIN, GPIO.LOW)
    GPIO.cleanup()

    
   
       
# Main
print("Reading sensor data...")
line = serial_read(port = "",baudrate = 9600,timeout = 2)
print("Processing data...")
moisture = split_data(line)
print("Fetching weather data...")
weather_data = get_weather(api_key = "", lat = 0.0, lon = 0.0)
print("Fetching Time features...")
time_features = get_time_features()
print("Preparing input features...")
features = get_input_features(moisture, weather_data, time_features)
print("Loading model and predicting irrigation need...")
model = load_model(model_path = "model.joblib")
prediction = predict_irrigation(model, features)
print(f"Predicted irrigation need (liters): {prediction[0]}")
print("Calculating irrigation time...")
irrigation_time = calculate_irrigation_time(prediction, flow_rate)
if irrigation_time > 0:
    print(f"Running motor for {irrigation_time} seconds...")
    run_motor(irrigation_time) 
#12.877643923069186, 77.56860346588182