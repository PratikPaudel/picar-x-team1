# Import statements for sockets and keyboard input
from socket import *
import keyboard
import webbrowser

# This will get the IP address from the user
ip = input("Enter the IP address of the robot server: ")

# Prints instructions for the user
print()
print('----------------------------------------------------------------------------------------------------')
print('''- Robot Control Instructions -
     
Overview:
     
        -This Program allows you to control a robot using a keyboard it sends the robot over a UDP connection
Setup:
     
        -Make Sure Python and 'keyboard' are installed you get keyboard from pip install extension.
     
        -Script communicates with the robot server at the 'ip':25565.
Usage:
     
    -Run the Script:
     
        -Start the script in Python. You might need to run it in adminstrative mode.
     
        -Once the script is running it will listen for the client to press keys and it will send the commands to the robot
   
    -Control Keys:
         
        Left Arrow: Move the wheels to the left. Press to start and release to stop.
      
        Right Arrow: Move the wheels to the right. Press to start and release to stop.
      
        Up Arrow: Moves the car forward. Press to start and release to stop.
      
        Down Arrow: Move the car backward. Press to start and release to stop.
      
        J Key: Set robot's speed (0-100). Press 'J', then enter the speed, then press Enter. If you input an invalid speed, it will reset to 30 speed.
      
        Exit: Stop the script with Ctrl + C or by closing Python; this will halt the code.
      
        'A', 'D', 'W', and 'S' keys: Control the camera movement and direction.
      
        H key: Honk function.
      
        T key: Take photo from the picar camera as you move the angle of the camera.
      
      
Troubleshooting:
     
        -Make sure that the robots server is running first.
     
        -Check if you have the correct IP address.
     
        -Make sure that 'keyboard' is installed and working right.  
         
---------------------------------------------------------------------------------------------------------------
''')


# Concatenate the IP address with the rest of the URL
url = f"http://{ip}:9000/mjpg"
webbrowser.open(url)

# Connects to the socket
yourSock = socket(AF_INET, SOCK_DGRAM)

# Will get us an IP address from the user

# Define functions to be called on key events
def on_left_key(event):
    """
    Handles the press of the left arrow key and triggers a 'left' command.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('left')

def on_not_left_key(event):
    """
    Handles the release of the left arrow key and triggers a 'notleft' command.

    Parameters:
    - event: The keyboard event associated with the key release.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('notleft')

def on_right_key(event):
    """
    Handles the press of the right arrow key and triggers a 'right' command.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('right')

def on_not_right_key(event):
    """
    Handles the release of the right arrow key and triggers a 'notright' command.

    Parameters:
    - event: The keyboard event associated with the key release.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('notright')

def on_up_key(event):
    """
    Handles the press of the up arrow key and triggers a 'forward' command.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('forward')

def on_not_up_key(event):
    """
    Handles the release of the up arrow key and triggers a 'notforward' command.

    Parameters:
    - event: The keyboard event associated with the key release.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('notforward')

def on_down_key(event):
    """
    Handles the press of the down arrow key and triggers a 'backward' command.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('backward')

def on_not_down_key(event):
    """
    Handles the release of the down arrow key and triggers a 'notbackward' command.

    Parameters:
    - event: The keyboard event associated with the key release.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('notbackward')

def on_a_key(event):
    """
    Handles the press of the 'A' key and triggers an 'a' command for camera movement.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('a')

def on_not_a_key(event):
    """
    Handles the release of the 'A' key and triggers a 'nota' command.

    Parameters:
    - event: The keyboard event associated with the key release.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('nota')

def on_d_key(event):
    """
    Handles the press of the 'D' key and triggers an 'd' command for camera movement.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('d')

def on_not_d_key(event):
    """
    Sends 'notd' command when the 'D' key is released.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('notd')

def on_w_key(event):
    """
    Handles the press of the 'W' key and triggers an 'w' command for camera movement.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('w')

def on_not_w_key(event):
    """
    Sends 'notw' command when the 'W' key is released.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('notw')

def on_s_key(event):
    """
    Handles the press of the 'S' key and triggers an 's' command for camera movement.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('s')

def on_not_s_key(event):
    """
    Sends 'nots' command when the 'S' key is released.
    """
    if event.event_type == keyboard.KEY_UP:
        send_command('nots')

def on_j_key(event):
    """
    Handles the press of the 'J' key and triggers an 'speed' command for camera movement.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('speed')
        speed_select()

def on_h_key(event):
    """
    Handles the press of the 'H' key and triggers an 'h' command for honking sound.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('h')

def on_t_key(event):
    """
    Handles the press of the 'T' key and triggers an 't' command for taking pictures on the server side.

    Parameters:
    - event: The keyboard event associated with the key press.
    """
    if event.event_type == keyboard.KEY_DOWN:
        send_command('t')

def send_command(msg):
    """
    Sends a command to the server side program (running on raspberry pi (picar)).
   
    Parameters:
    - msg (str): The command message to be sent.
    """
    yourSock.sendto(msg.encode(), (ip, 25565))

def speed_select():
    """
    Prompts the user to select a speed and sends it to the picar.
    """
    try:
        speed = int(input("Enter robot speed (0-100): "))
        while speed < 0 or speed > 100:
            speed = int(input("Invalid speed. Enter a value between 0-100: "))
    except ValueError:
        print("Invalid entry. Resetting speed to 30.")
        speed = "30"
   
    yourSock.sendto(str(speed).encode(), (ip, 25565))
   
# Bind the functions to the corresponding keys with the corresponding event type
# Left arrow pressed/released binding and function call
keyboard.on_press_key('left', on_left_key)
keyboard.on_release_key('left', on_not_left_key)

# Right arrow pressed/released binding and function call
keyboard.on_press_key('right', on_right_key)
keyboard.on_release_key('right', on_not_right_key)

# Up arrow pressed/released binding and function call
keyboard.on_press_key('up', on_up_key)
keyboard.on_release_key('up', on_not_up_key)

# Down arrow pressed/released binding and function call
keyboard.on_press_key('down', on_down_key)
keyboard.on_release_key('down', on_not_down_key)

# Camera key bindings
# A pressed/released binding and function call
keyboard.on_press_key('A', on_a_key)
keyboard.on_release_key('A', on_not_a_key)

# D pressed/released binding and function call
keyboard.on_press_key('D', on_d_key)
keyboard.on_release_key('D', on_not_d_key)

# W pressed/released binding and function call
keyboard.on_press_key('W', on_w_key)
keyboard.on_release_key('W', on_not_w_key)

# S arrow pressed/released binding and function call
keyboard.on_press_key('S', on_s_key)
keyboard.on_release_key('S', on_not_s_key)

# 'J' key pressed/released binding and function call
keyboard.on_press_key('J', on_j_key)  # 'J' key for speed select

# 'H' key pressed/released binding and function call
keyboard.on_press_key('H', on_h_key)  # 'H' key for speed select

# 'T' key pressed/released binding and function call
keyboard.on_press_key('T', on_t_key)  # 'T' key for taking picture

# Keep the program running
keyboard.wait()

