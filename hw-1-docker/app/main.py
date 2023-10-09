from flask import Flask, jsonify
import datetime
import psutil

app = Flask(__name__)

@app.route("/battery", methods=["GET"])
def getBattery():
    batterySecs = psutil.sensors_battery().secsleft

    minutes, seconds = divmod(batterySecs, 60) 
    hours, minutes = divmod(minutes, 60)

    return jsonify({'remainig': f"{hours}:{minutes}:{seconds}"})

@app.route("/process", methods=["GET"])
def getProcess():
    process = psutil.Process()
    
    return jsonify(
        {
            'ID': process.pid,
            'name': process.name(),
            'status': process.status(),
            'started': datetime.datetime.fromtimestamp(process.create_time()),
        }
    )

@app.route("/cpu", methods=["GET"])
def getCPU():
    cores = psutil.cpu_percent(percpu=True)
    return jsonify(
        { f'core {i}': core for i, core in enumerate(cores) }
    )

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=9090)