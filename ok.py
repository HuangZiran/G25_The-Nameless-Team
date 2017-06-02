from microbit import *
import random
images = [Image.HAPPY, Image.SAD, Image.ANGRY, Image.CONFUSED, Image.MEH , Image.SURPRISED]
          
while True:
    sleep(20)
    x = random.randint(0,4)
    y = random.randint(0,4)
    brightness = random.randint(0, 9)
    display.set_pixel(x, y, brightness)
    if button_a.is_pressed():
        display.show(random.choice(images))
        sleep(1000)
    if button_b.is_pressed():
        display.scroll("YES", delay=100)
        