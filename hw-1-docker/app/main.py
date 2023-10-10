from flask import Flask, jsonify
import datetime
import psutil

app = Flask(__name__)

@app.route("/battery", methods=["GET"])
def getBattery():
    batteryInfo = psutil.sensors_battery()

    if batteryInfo:
        batterySecs = batteryInfo.secsleft
        
        minutes, seconds = divmod(batterySecs, 60) 
        hours, minutes = divmod(minutes, 60)

        return jsonify({'data': f"{hours}:{minutes}:{seconds}"})
    else:
        return jsonify({'error': 'could not get battery info'}), 404

@app.route("/process", methods=["GET"])
def getProcess():
    process = psutil.Process()
    
    if process:
        return jsonify(
            {
                'ID': process.pid,
                'name': process.name(),
                'status': process.status(),
                'started': datetime.datetime.fromtimestamp(process.create_time()),
            }
        )
    else:
        return jsonify({'error': 'could not get process info'}), 404

@app.route("/cpu", methods=["GET"])
def getCPU():
    cores = psutil.cpu_percent(percpu=True)

    if cores:
        return jsonify(
            { 'data': [ core for core in cores ] }
        )
    else:
        return jsonify({'error': 'could not get cpu info'}), 404

if __name__ == '__main__':
    app.run('0.0.0.0', port=9090)