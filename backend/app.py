from flask import Flask, jsonify
import requests
from mqtt_client import publish_message

app = Flask(__name__)

# Obtener la IP pública y la localización
def get_instance_info():
    # Obtener la IP pública de la instancia EC2
    ip = requests.get("http://3.87.8.88/latest/meta-data/public-ipv4").text
    # Obtener la localización de la IP
    location = requests.get(f"http://ip-api.com/json/{ip}").json()
    return {"ip": ip, "location": location}

@app.route('/stream-info', methods=['GET'])
def stream_info():
    instance_info = get_instance_info()
    return jsonify(instance_info)

@app.route('/mqtt-publish', methods=['GET'])
def mqtt_publish():
    publish_message("streaming", "streaming video message")
    return jsonify({"message": "Message published to MQTT"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
