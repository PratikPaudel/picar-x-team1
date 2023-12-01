# Robot Control Program

## Overview

This program enables you to control a robot using a keyboard, sending commands over a UDP connection.

## Setup

- Ensure that Python and the 'keyboard' library are installed. You can install 'keyboard' using 'pip install keyboard'.
- The script communicates with the robot server at the 'ip':25565.

## Usage

### Run the Script

- Start the script in Python. You might need to run it in administrative mode.
- Once the script is running, it will listen for the client to press keys and send the commands to the robot.

### Control Keys

- **Left Arrow:** Move the robot left. Press to start and release to stop.
- **Right Arrow:** Move robot right. Press to start and release to stop.
- **Up Arrow:** Move robot forward. Press to start and release to stop.
- **Down Arrow:** Move robot backward. Press to start and release to stop.
- **J Key:** Set robot's speed (0-100). Press 'J', then enter the speed, then press Enter. If you input an invalid speed, it will reset to 30 speed.
- **Exit:** Stop the script with Ctrl + C or by closing Python; this will halt the code.
- **'A', 'D', 'W', and 'S' keys:** Control the camera movement and direction.
- **H key:** Honk function.
- **T key:** Take photo function.

## Troubleshooting

- Make sure that the robot's server is running first.
- Check if you have the correct IP address.
- Ensure that 'keyboard' is installed and functioning correctly.
