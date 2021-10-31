from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/SensorStream')
def sensor_stream():
    #TODO: Add code that displays the contents of log file /data/sensorlog.txt 

@app.route('/download')
def download_file():
    #TODO: Add code to download the file /data.sensorlog.txt



#TODO Add the remaining functions requested either by adding more pages to the template or get fancy with more templates and better formatting




if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5080, debug=True) #Use this line to test basic functionality locally before trying to deploy on Pi
    app.run(host='0.0.0.0', port=80)
