import requests

KEY = '832fbfa10cba418596a92e7dae682a5a' 
API = 'https://free-api.heweather.com/v5/weather' 
LANGUAGE = 'zh-cn'

def get_api_data(city):
        results = requests.get(API,
                               params= {'key': KEY,
                                        'city':  city,
                                        'lang' : LANGUAGE}
                                        )
        json_result = results.json()
        return json_result

def retrieve_json_weather(city):
        json_result = get_api_data(city)
        retrieve_data = json_result['HeWeather5'][0]
        city = retrieve_data['basic']['city']
        weather_status = retrieve_data['now']['cond']['txt']
        wind = retrieve_data['now']['wind']
        humidity = retrieve_data['now']['hum']
        temperature = retrieve_data['now']['tmp']
        return u'{0}：{1}度，{2}，{3}，湿度{4}'.format(city, temperature, weather_status, wind['dir'], humidity)
