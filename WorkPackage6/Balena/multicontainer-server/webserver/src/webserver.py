from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/SensorStream')
def sensor_stream():
    with open("/data/sensorlog.txt", "r") as sl:
        logs = sl.read()
        return logs


@app.route('/download')
def download_file():
    path = "/data/sensorlog.txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5080, debug=True)
    app.run(host='0.0.0.0', port=80)
