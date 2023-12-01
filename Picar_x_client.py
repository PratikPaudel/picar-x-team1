#Import statements for sockets and keyboard input
from socket import *
import keyboard
import webbrowser

#this will get the IP address from the user
ip = input("Enter the IP address of the robot server: ")

#Prints instructions for the user
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
      
        -Left Arrow: Move the robot left. Press to start and release to stop.
      
        -Right Arrow: Move robot right. Press to start and release to stop.
      
        -Up Arrow: Move robot forward. Press to start and release to stop.
      
        -Down Arrow: Move robot backward. Press to start and release stop.
      
        -J Key: Set robots speed (0-100). Press 'J', then enter the speed, then press Enter, if you put in an invalid speed and it will reset to 30 speed.
      
        -Exit: Stop the script with Ctrl + C or by closing Python this will stop the code.
      
        -'A', 'D', 'W', and 'S' keys: Control the camera movement and direction.
      
        -H key: for honk function
      
        -T key: take photo function

Troubleshooting:
      
        -Make sure that the robots server is running first.
      
        -Check if you have the correct IP address.
      
        -Make sure that 'keyboard' is installed and working right.  
          
---------------------------------------------------------------------------------------------------------------
''')


#Concatenate the IP address with the rest of the URL
url = f"http://{ip}:9000/mjpg"
webbrowser.open(url)

#Connects to the socket
yourSock = socket(AF_INET, SOCK_DGRAM)

#Will get us an IP address from the user

# Define functions to be called on key events
#Function for when left arrow is pressed down
def on_left_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('left')

#Function for when left arrow is released
def on_not_left_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('notleft')

#Function for when right arrow is pressed down
def on_right_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('right')

#Function for when right arrow is released
def on_not_right_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('notright')

#Function for when up arrow is pressed down
def on_up_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('forward')

#Function for when up arrow is released
def on_not_up_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('notforward')

#Function for when down arrow is pressed down
def on_down_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('backward')

#Function for when down arrow is released
def on_not_down_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('notbackward')

#Camera functions!!!
#Function for when a is pressed down
def on_a_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('a')

#Function for when a is released
def on_not_a_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('nota')

#Function for when d is pressed down
def on_d_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('d')

#Function for when d is released
def on_not_d_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('notd')

#Function for when w is pressed down
def on_w_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('w')

#Function for when w is released
def on_not_w_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('notw')

#Function for when s is pressed down
def on_s_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('s')

#Function for when s is released
def on_not_s_key(event):
    #Checks is the event type is a KEY_UP
    if event.event_type == keyboard.KEY_UP:
        #Calls the send command function to send the corresponding command
        send_command('nots')

#Function for when 'J' is pressed down
def on_j_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('speed')
        #Calls the speed function to prompt the user for the desired speed
        speed_select()

#Function for when 'H' is pressed down
def on_h_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('h')

#Function for when 'T' is pressed down
def on_t_key(event):
    #Checks is the event type is a KEY_DOWN
    if event.event_type == keyboard.KEY_DOWN:
        #Calls the send command function to send the corresponding command
        send_command('t')

# Function to send commands to the server
def send_command(msg):
    #Encodes and sends the command to the picar
    yourSock.sendto(msg.encode(), (ip, 25565))

# Function to change speed
def speed_select():
    #Try block to catch invalid input types
    try:
        #Prompts the user for the new desired speed
        speed = int(input("What speed would you like the robot to move (0-100): "))

        #Checks to see if the number given is within the possible speed range
        while((speed > 100) or (speed < 0)):
            #Declares invalid input was received and reprompts the user for the new desired speed
            speed = int(input("Invalid speed. What speed would you like the robot to move (0-100): "))
    except ValueError:
        #Prints that an invalid entry type was received and resets the speed to the default speed
        print("Invalid entry type. Resetting robot speed to 30.")
        #Resets the speed to the default speed
        speed = "30"
        
    #Converts the input to a string in preparation for sending
    speed = str(speed)
    #Encodes and sends the new desired speed to the server
    yourSock.sendto(speed.encode(), (ip, 25565))

# Bind the functions to the corresponding keys with the corresponding event type
#Left arrow pressed/released binding and function call
keyboard.on_press_key('left', on_left_key)
keyboard.on_release_key('left', on_not_left_key)

#Right arrow pressed/released binding and function call
keyboard.on_press_key('right', on_right_key)
keyboard.on_release_key('right', on_not_right_key)

#Up arrow pressed/released binding and function call
keyboard.on_press_key('up', on_up_key)
keyboard.on_release_key('up', on_not_up_key)

#Down arrow pressed/released binding and function call
keyboard.on_press_key('down', on_down_key)
keyboard.on_release_key('down', on_not_down_key)

#Camera key bindings
#A pressed/released binding and function call
keyboard.on_press_key('A', on_a_key)
keyboard.on_release_key('A', on_not_a_key)

#D pressed/released binding and function call
keyboard.on_press_key('D', on_d_key)
keyboard.on_release_key('D', on_not_d_key)

#W pressed/released binding and function call
keyboard.on_press_key('W', on_w_key)
keyboard.on_release_key('W', on_not_w_key)

#S arrow pressed/released binding and function call
keyboard.on_press_key('S', on_s_key)
keyboard.on_release_key('S', on_not_s_key)

#'J' key pressed/released binding and function call
keyboard.on_press_key('J', on_j_key)  # 'J' key for speed select

#'H' key pressed/released binding and function call
keyboard.on_press_key('H', on_h_key)  # 'H' key for speed select

#'T' key pressed/released binding and function call
keyboard.on_press_key('T', on_t_key)  # 'T' key for speed select

# Keep the program running
keyboard.wait()
