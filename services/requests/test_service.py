import requests
import time
import random as rnd
import logging

logger = logging.getLogger('request_sender')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
URL = 'http://ml_service:8000/api/prediction'
BAD_REQUEST_PROB = .15


def generate_data():
    return {
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
        "px_height": rnd.randint(200, 1900),
        "px_width": rnd.randint(500, 2000),
        "ram": rnd.randint(250, 4000),
        "sc_h": rnd.randint(5, 20),
        "sc_w": rnd.randint(0, 20),
        "talk_time": rnd.randint(2, 20),
        "three_g": rnd.randint(0, 1),
        "touch_screen": rnd.randint(0, 1),
        "wifi": rnd.randint(0, 1)
    }


def send_requests(url, start_id, n_requests):
    for phone_id in range(start_id, start_id + n_requests):
        params = {'phone_id': phone_id}
        value = rnd.random()
        if value < BAD_REQUEST_PROB:
            data = {}
        elif value > 1 - BAD_REQUEST_PROB:
            data = generate_data() | {'wifi': ''}
        else:
            data = generate_data()
        try:
            response = requests.post(url, params=params, json=data)
            time.sleep(rnd.random() * 2)
            logger.info('Response: %s', response.json())
        except Exception as e:
            logger.error(f'Cant send request {value=} {phone_id=} {data=}: {e}')

def main():
    return send_requests(URL, rnd.randint(1, 100), rnd.randint(1, 100))

        
if __name__ == "__main__":
    main()