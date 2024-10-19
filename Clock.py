import time
from datetime import datetime

try: 
    while True: 
        now = datetime.now().strftime(
            "%H:%M:%S")
        print(
            "\rHora actual: {}".format(now),
            end = "")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nReloj interrupido")
        