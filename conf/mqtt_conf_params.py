class MqttConfigurationParameters(object):

    LAB_GROUP_ID = "g00"
    BROKER_ADDRESS = "155.185.4.4"
    BROKER_PORT = 7883
    MQTT_USERNAME = "smartcity-lab-22"
    MQTT_PASSWORD = "brbzoveuxwofsrlo"
    MQTT_BASIC_TOPIC = "/iot/user/{0}".format(MQTT_USERNAME)
    TEST_TOPIC = "test"