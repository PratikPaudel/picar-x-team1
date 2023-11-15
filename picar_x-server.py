from socket import *
from picarx import Picarx
import time


mySock = socket(AF_INET, SOCK_DGRAM)
mySock.bind(('', 25565))

def move(px):
    try:
        px.forward(30)
        time.sleep(0.5)
        for angle in range(0,35):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
            px.forward(0)
            time.sleep(1)
        for angle in range(0,35):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0,35):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
            
    finally:
        px.stop()
        time.sleep(.2)

if __name__ == "__main__":
    px = Picarx()
    while True:
        message, clientAddress = mySock.recvfrom(2048)
        message = message.decode()
        print(message)
        mySock.sendto("got it".encode(), clientAddress)
        move(px)
