import json
import time

from flask import Flask
from flask import jsonify
from flask import request
#from flask_cors import CORS

#from lightControl import get_serial_port, init_serial_port, set_light_level_color_temperature
from light_regressor import LightRegressor

light_regressor = LightRegressor()

app = Flask(__name__)
#CORS(app)

session_timer = int(time.time())


def initialize_lamp():
    port_name = get_serial_port()
    if port_name:
        # port Exists so init it
        serial_device = init_serial_port(port_name)

        if serial_device:
            serialize_device = serial_device
            return serialize_device


#serialized_device = initialize_lamp()
base_value = 0
light_volume = 0
running_session = False


@app.route('/send_volume', methods=["POST", "GET"])
def send_volume():
    global base_value
    global light_volume
    global session_timer
    global running_session
    if int(time.time()) - session_timer > 10:
        base_value = light_volume
    if request.method == 'POST':
        data = request.data
        print(data)
        json_data = json.loads(str(data, encoding='utf-8'))
        light_volume_temp = json_data.get("light_volume")
        print(light_volume_temp)
        light_volume = base_value + light_volume_temp * 100
        light_volume = 100 if light_volume > 100 else light_volume
        light_volume = 0 if light_volume < 0 else light_volume
        print("Changing the value to:", light_volume)
        set_light_level_color_temperature(serialized_device, _lightLevelValue=light_volume)
        session_timer = int(time.time())
        running_session = True
        return jsonify({"light_volume": light_volume}), 200
    elif request.method == "GET":
        return jsonify({"Status": "Hello"})


@app.route('/send_end_volume', methods=["POST", "GET"])
def send_end_volume():
    global base_value
    global running_session
    global light_volume
    if not running_session:
        return 400
    if request.method == 'POST':
        base_value = light_volume
        print("Changing the BASE value to:", light_volume)
        running_session = False
        return jsonify({"base_volume": light_volume}), 200
    elif request.method == "GET":
        return jsonify({"Status": "Hello"})


@app.route('/send_start_volume', methods=["POST", "GET"])
def send_start_volume():
    global running_session
    if request.method == 'POST':
        running_session = True
        return jsonify({"base_volume": light_volume}), 200
    elif request.method == "GET":
        return jsonify({"Status": "Hello"})


@app.route('/send_temperature', methods=["POST"])
def send_temperature():
    # TODO
    if request.method == 'POST':
        data = request.data
        json_data = json.loads(str(data, encoding='utf-8'))
        light_temp = json_data.get("light_temperature")
        set_light_level_color_temperature(serialized_device, _lightLevelValue=light_temp)
        return {"light_temperature": light_temp}, 200


@app.route('/light_intensity_predictions', methods=['POST'])
def light_intensity_predictions():
    if request.method == 'POST':
        data = request.data
        json_data = json.loads(str(data, encoding='utf-8'))
        lights_list = json_data.get("lights", None)
        if lights_list is None:
            return {"light_intensity_predictions": json.dumps([])}, 200

        preds = light_regressor.predict_light_intensity(lights_list)
        return json.dumps({"light_intensity_predictions": preds.tolist()}), 200


@app.route('/light_warmth_predictions', methods=['POST'])
def light_warmth_predictions():
    if request.method == 'POST':
        data = request.data
        json_data = json.loads(str(data, encoding='utf-8'))
        lights_list = json_data.get("lights", None)
        if lights_list is None:
            return {"light_warmth_predictions": []}, 200

        preds = light_regressor.predict_light_warmth(lights_list)
        return json.dumps({"light_warmth_predictions": preds.tolist()}), 200


@app.route('/room_temperature_predictions', methods=['POST'])
def room_temperature_predictions():
    if request.method == 'POST':
        data = request.data
        json_data = json.loads(str(data, encoding='utf-8'))
        rooms_list = json_data.get("rooms", None)
        if rooms_list is None:
            return {"room_temperature_predictions": []}, 200
        preds = light_regressor.predict_temperature(rooms_list)
        return json.dumps({"room_temperature_predictions": preds.tolist()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
