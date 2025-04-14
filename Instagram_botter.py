import time
import random
import uuid
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

def delay_random(min_s: float, max_s: float):
    duration = round(random.uniform(min_s, max_s), 2)
    time.sleep(duration)
    return duration

def simulate_followers():
    for i in range(3):
        fake_user = f"user_{uuid.uuid4().hex[:6]}"
        delay = delay_random(2.5, 5.5)
        print(f"[+] Follower #{i+1}: {fake_user} followed after {delay}s.")
    logging.info("Follower batch completed.\n")

def run_bot_forever():
    logging.info("Bot loop started.")
    while True:
        simulate_followers()
        sleep_between_batches = random.randint(30, 90)
        logging.info(f"Sleeping {sleep_between_batches}s before next batch...")
        time.sleep(sleep_between_batches)

if __name__ == "__main__":
    run_bot_forever()
