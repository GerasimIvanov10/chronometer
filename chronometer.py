import time

while True:
    try:
        input("Click Enter to start the stopwatch")
        timer_start = time.time()
        print("The stopwatch has started")
        while True:
            print("Time elapsed:", round(time.time() - timer_start, 0), "seconds")
            time.sleep(1)
    except KeyboardInterrupt:
        timer_end = time.time()
        print("The stopwatch has stopped")
        print("Time elapsed:", round(timer_end - timer_start, 2), "seconds")
    break

