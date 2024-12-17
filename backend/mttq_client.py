import paho.mqtt.client as mqtt

# Configurar cliente MQTT
broker = "localhost"  # O la dirección de tu broker MQTT en AWS
port = 1883
topic = "video-streaming"

def on_connect(client, userdata, flags, rc):
    print(f"Conectado con código {rc}")
    # Se puede suscribir a un tópico aquí si se necesita

def publish_message(topic, message):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    client.loop_start()
    
    # Publicar un mensaje
    client.publish(topic, message)
    print(f"Mensaje publicado: {message}")

    # Detener el loop después de publicar
    client.loop_stop()
