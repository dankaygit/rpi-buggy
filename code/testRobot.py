# Write your code here :-)
from gpiozero import InputDevice, OutputDevice, Robot
from time import sleep, time

duration = 15
end_time = time() + duration
running = True

trig = OutputDevice(4)
echo = InputDevice(17)

sleep(2)

def get_pulse_time():
    """Returns the time for the pulse to be reflected
    back by an object (in seconds)"""
    pulse_start, pulse_end = 0, 0
    
    trig.on()
    sleep(1e-5)
    trig.off()
    
    while not echo.is_active:
        pulse_start = time()

    while echo.is_active:
        pulse_end = time()
    
    travel_time = pulse_end - pulse_start
    return (travel_time)

def calculate_distance():
    duration = get_pulse_time()
    speed = 343 #m/s
    distance = speed * duration / 2  # calculate distance in metres
    

    return (distance)



robin = Robot(left = (10,9), right = (7,8))

robin.backward(0.6)
sleep(0.6)

while running:
    if time() > end_time:
        running = False
        robin.stop()
    
    distance = calculate_distance()
    
    if distance < 0.35:
        robin.left(0.3)
        sleep(0.2)
    else:
        robin.forward(0.8)

    sleep(0.06)
    print(distance)

robin.stop()