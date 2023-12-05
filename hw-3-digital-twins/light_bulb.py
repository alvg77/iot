import json
import time
from threading import Event

class LightBulb:
    def __init__(self, thing_id: str):
        self.thing_id = self.policy_id = thing_id
        self.file_name = thing_id + '.json'
        self.event = Event()
        self.attributes = {
            "model": "Smart Light Bulb",
            "diameter": 10,
            "diameter_metric": "cm",
            "warranty": 2,
        }
        self.features = {
            "indicators": {
                "properties": {
                    "brightness": 0,
                    "color": "white",
                }
            },
            "state":{
                "properties": {
                    "on": False,
                }
            },
        }
        

    def save_to_json(self):
        serializable = {
            "thing_id": self.thing_id,
            "policy_id": self.policy_id,
            "attributes": self.attributes,
            "features": self.features
        }

        with open("./digital-twins/" + self.file_name, 'w') as f:
            json.dump(serializable, f, indent=4, ensure_ascii=False)
    
    def break_bulb(self):
        print("Bulb ID: " + self.thing_id + " is broken")

        self.features["state"]["properties"]["on"] = False

        self.save_to_json()

    def fix_bulb(self, tech_id: int):
        print("Bulb ID: " + self.thing_id + " is being fixed by technician ID: " + str(tech_id))
        time.sleep(3)
        print("Bulb ID: " + self.thing_id + " is fixed")

        self.features["state"]["properties"]["on"] = True

        self.save_to_json()

    def update_indicators(self, brightness: float, color: str):
        if (brightness < 0 or brightness > 100):
            raise ValueError("Brightness must be between 0 and 100")

        self.features["indicators"]["properties"]["brightness"] = brightness
        self.features["indicators"]["properties"]["color"] = color

        print("Bulb ID: " + self.thing_id + " is now " + color + " with brightness " + str(brightness) + "%")

        self.save_to_json()