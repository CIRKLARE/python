import time

count = 0
while True:
    print(f"{count}", end="\r", flush=True)
    count += 1
    time.sleep(0.1)