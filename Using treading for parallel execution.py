import threading
import time

def print_numbers():
    for i in range(500):
        print(i)
        time.sleep(0.5)


thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
# 0
# 1
# 2
# 3
# 4
