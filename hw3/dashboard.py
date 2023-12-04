import json
import os
import time

if __name__ == "__main__":
    while True:
        # in case new bulbs are added
        filenames = os.listdir("./digital-twins")
        bulb_data = []

        for filename in filenames:
            with open("./digital-twins/" + filename, 'r') as f:
                bulb_data.append(json.load(f))

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Bulb ID | Color | Brightness | State")
        for i in bulb_data:
            print(
                f"{i['thing_id']} | \
                {i['features']['indicators']['properties']['color']} | \
                {i['features']['indicators']['properties']['brightness']} | \
                {i['features']['state']['properties']['on']} \
            ")
        
        time.sleep(1)
