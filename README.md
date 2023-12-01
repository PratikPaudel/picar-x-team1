# Robot Control Program

## Overview

This program enables you to control a robot car (picar) using a keyboard, sending commands over a UDP connection.

## Setup

- Ensure that Python and the 'keyboard' library are installed. You can install 'keyboard' using 'pip install keyboard'.
- The script communicates with the robot server at the 'port no.':25565.

## Usage

### Run the Script

- Start the python server script on picar, and client program on client computer. 
- Once the client code is running, it will ask for IP of the server(the picar-x) so it can send the commands to the picar.

### Control Keys

- **Left Arrow:** Move the wheels to the left. Press to start and release to stop.
- **Right Arrow:** Move the wheels to the right. Press to start and release to stop.
- **Up Arrow:** Moves the car forward. Press to start and release to stop.
- **Down Arrow:** Move the car backward. Press to start and release to stop.
- **J Key:** Set robot's speed (0-100). Press 'J', then enter the speed, then press Enter. If you input an invalid speed, it will reset to 30 speed.
- **Exit:** Stop the script with Ctrl + C or by closing Python; this will halt the code.
- **'A', 'D', 'W', and 'S' keys:** Control the camera movement and direction.
- **H key:** Honk function.
- **T key:** Take photo from the picar camera as you move the angle of the camera.

## Troubleshooting

- Make sure that the robot's server is running first.
- Check if you have the correct IP address.
- Ensure that 'keyboard' is installed and functioning correctly.
