from flask import Flask, request, render_template
from  weather_api import  retrieve_json_weather
app = Flask(__name__)
weather_history = []

@app.route('/')
def index():
     return render_template('base_index.html')

@app.route('/user', methods=['GET', 'POST'])
def weather_app(): 
    user_city = request.args.get('city')
    cmd = request.args.get('action')
    try:
        weather_info = retrieve_json_weather(user_city)
        weather_history.append(weather_info)
        return render_template('weather.html', weather_info=weather_info)
    except KeyError as e: #当retrieve_json_weather()输入参数非法时，捕获该错误
        if cmd == u'帮助':
           return render_template('help.html')
        elif cmd == u'历史':
            return render_template('history.html', weather_history=weather_history)
        else:
            return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)