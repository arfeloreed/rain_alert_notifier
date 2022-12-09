import requests
from twilio.rest import Client

PARAMETERS = {
    "lat": your latitude,
    "lon": your longitude,
    "appid": "your_app_id from openweathermap",
}
account_sid = "your_account id from twilio"
auth_token = "your auth token from twilio"

client = Client(account_sid, auth_token)
response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=PARAMETERS)
# print(response.status_code)
response.raise_for_status()
data = response.json()["list"]
data_list = data[:6]
weather_data = [datum["weather"][0]["id"] for datum in data_list]
print(weather_data)
if min(weather_data) < 700:
    message = client.messages.create(
        body="Today's Weather Forecast. Please bring an umbrella, it's going to rain this day.",
        from_="your personal number from twilio",
        to="number you want to send the message to"
    )
    print(message.status)
