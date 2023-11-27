
from socket import *
import keyboard

yourSock = socket(AF_INET, SOCK_DGRAM)

# Define functions to be called on key events
def on_left_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print("sending command left:")
        send_command('left')

def on_right_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print("sending command right:")
        send_command('right')

def on_up_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print("sending command forward:")
        send_command('forward')

def on_down_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print("sending command stop:")
        send_command('stop')

def on_b_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print("sending command backward:")
        send_command('backward')

# Function to send commands to the server
def send_command(msg):
    yourSock.sendto(msg.encode(), ('10.50.16.16', 25565))
    message, serverAddress = yourSock.recvfrom(2048)
    print(message)

# Bind the functions to the corresponding keys
keyboard.on_press_key('left', on_left_key)
keyboard.on_press_key('right', on_right_key)
keyboard.on_press_key('up', on_up_key)
keyboard.on_press_key('down', on_down_key)
keyboard.on_press_key('B', on_b_key)  # 'B' key for backward

# Keep the program running
keyboard.wait()
