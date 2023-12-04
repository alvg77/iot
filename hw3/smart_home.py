import time
import random
import threading

from queue import Queue

from light_bulb import LightBulb

LIGHTBULBS = 5
TECHNITIANS = 2

def bulb_functioning(bulb: LightBulb): 
    while True:
        if random.randint(0, 100) < 40:
            bulb.break_bulb()
            manager_queue.put(bulb)
            manager_event.set()
            manager_event.clear()
            bulb.event.wait()
        else:
            brightness = random.randint(0, 100)
            color = random.choice(["white", "yellow", "red", "green", "blue"])
            bulb.update_indicators(brightness, color)
        
        time.sleep(random.randint(3, 5))

def technician_fix_bulb(technician_id: int, lightbulb: LightBulb):
    lightbulb.fix_bulb(technician_id)
    lightbulb.event.set()
    lightbulb.event.clear()
    available_technitians.put(technician_id)

def manager():
    while True:
        manager_event.wait()
        while not manager_queue.empty():
            if not available_technitians.empty():
                threading.Thread(
                    target=technician_fix_bulb, 
                    args=(
                        available_technitians.get(), 
                        manager_queue.get()
                    ), 
                    daemon=True
                ).start()

if __name__ == "__main__":
    manager_thread = threading.Thread(target=manager, daemon=True)
    manager_queue = Queue()
    manager_event = threading.Event()
    manager_thread.start()

    available_technitians = Queue()
    for i in range(TECHNITIANS):
        available_technitians.put(i+1)
    
    bulb_ids = ["lightbulb" + str(i+1) for i in range(LIGHTBULBS)]
    lightbulbs = [LightBulb(bulb_id) for bulb_id in bulb_ids]

    lightbulb_threads = []
    for bulb in lightbulbs:
        lightbulb_thread = threading.Thread(target=bulb_functioning, args=(bulb,), daemon=True)
        lightbulb_threads.append(lightbulb_thread)

    for thread in lightbulb_threads:
        thread.start()
        time.sleep(0.5)

    for thread in lightbulb_threads:
        thread.join()