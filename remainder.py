import time
from plyer import notification
while True:
    print("Drink some water")
    notification.notify(title="Drink some water",message="It's important to stay hydrated!",timeout=10)
    time.sleep(60*60)

