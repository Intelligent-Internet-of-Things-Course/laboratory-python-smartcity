
import paho.mqtt.client as mqtt
import time
from resources.gpx_gps_resource import GpxGeoLocation
from conf.mqtt_conf_params import MqttConfigurationParameters


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def publish_test_data(updated_loc_obj):
    target_topic = "{0}/{1}".format(
            MqttConfigurationParameters.MQTT_BASIC_TOPIC,
            MqttConfigurationParameters.TEST_TOPIC)
    device_payload_string = updated_loc_obj.to_json()
    mqtt_client.publish(target_topic, device_payload_string, 0, False)
    print(f"Telemetry Data Published: Topic: {target_topic} Payload: {device_payload_string}")


# Configuration variables
client_id = "python-demo-publisher-{0}".format(MqttConfigurationParameters.LAB_GROUP_ID)
message_limit = 1000

mqtt_client = mqtt.Client(client_id)
mqtt_client.on_connect = on_connect

# Set Account Username & Password
mqtt_client.username_pw_set(MqttConfigurationParameters.MQTT_USERNAME, MqttConfigurationParameters.MQTT_PASSWORD)

print("Connecting to " + MqttConfigurationParameters.BROKER_ADDRESS + " port: " + str(MqttConfigurationParameters.BROKER_PORT))
mqtt_client.connect(MqttConfigurationParameters.BROKER_ADDRESS, MqttConfigurationParameters.BROKER_PORT)

mqtt_client.loop_start()

# Create Demo GeoGpxLocation Resource
target_gpx_file = "../tracks/mantova_demo_track.gpx"
gpx_geo_location = GpxGeoLocation(target_gpx_file)


for message_id in range(message_limit):
    updated_loc = gpx_geo_location.update_measurements()
    print(f'Sending Updated GeoLoc: Lat: {updated_loc.latitude} - Lng: {updated_loc.longitude} - Ele: {updated_loc.elevation}')
    publish_test_data(updated_loc)
    time.sleep(1)

mqtt_client.loop_stop()
