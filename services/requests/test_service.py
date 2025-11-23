import requests
import time
import random as rnd

URL = 'http://ml_service:8000/api/prediction'

def send_requests(url, start_id, n_requests):
    for i in range(start_id, start_id + n_requests):
        params = {'phone_id': i}
        data = {
            "battery_power": rnd.randint(500, 2000),
            "blue": rnd.randint(0, 1),
            "clock_speed": rnd.uniform(0.5, 3),
            "dual_sim": rnd.randint(0, 1), 
            "fc": rnd.randint(0,  19),
            "four_g": rnd.randint(0, 1),
            "int_memory": rnd.randint(2, 64),
            "m_dep": rnd.uniform(0.1, 1),
            "mobile_wt": rnd.randint(80, 200),
            "n_cores": rnd.randint(1, 8),
            "pc": rnd.randint(0, 20),
            "px_height": rnd.randint(0, 1900),
            "px_width": rnd.randint(500, 2000),
            "ram": rnd.randint(250, 4000),
            "sc_h": rnd.randint(5, 20),
            "sc_w": rnd.randint(0, 20),
            "talk_time": rnd.randint(2, 20),
            "three_g": rnd.randint(0, 1),
            "touch_screen": rnd.randint(0, 1),
            "wifi": rnd.randint(0, 1)
        } 

        response = requests.post(url, params=params, json=data)
        time.sleep(rnd.random() * 5)
        print('Response:')
        print(response.json())


def main():
    return send_requests(URL, rnd.randint(1, 100), rnd.randint(1, 100))

        
if __name__ == "__main__":
    main()