import paho.mqtt.client as mqtt

# Configuration du broker MQTT
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "#"

# Cette fonction est appelée lorsqu'un message est reçu
def on_message(client, userdata, message):
    print(f"Message reçu: {message.payload.decode('utf-8')}")
    # Ici, vous pouvez définir l'action à effectuer à la réception d'un message

# Cette fonction est appelée lors de la connexion au serveur MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT")
        # S'abonner au topic
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Échec de la connexion, code de retour {rc}")

# Configuration du client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_forever()
