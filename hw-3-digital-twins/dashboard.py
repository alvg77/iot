import json
import os
import time

if __name__ == "__main__":
    if os.listdir("./digital-twins") == []:
        print("No bulbs found")
        exit(-1)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # in case new bulbs are added
        filenames = os.listdir("./digital-twins")

        print("Bulb ID | Color | Brightness | State")
        print("------------------------------------")
        for filename in filenames:
            with open("./digital-twins/" + filename, 'r') as f:
                try:
                    data = json.load(f)
                    print(
                        f"{data['thing_id']} | \
                        {data['features']['indicators']['properties']['color']} | \
                        {data['features']['indicators']['properties']['brightness']} | \
                        {data['features']['state']['properties']['on']} \
                    ")
                except json.decoder.JSONDecodeError as e:
                    print("Error loading file: " + filename)
        
        time.sleep(1)
