# Arduino Code for Robot Motor Controller

This directory contains Arduino code for controlling the four-wheel robot.

## Hardware Requirements

- Arduino Uno/Mega or compatible board
- Motor driver boards (L298N or similar) - 2 units for 4 motors
- 24V Li-ion battery pack (6S configuration)
- Voltage divider circuit for battery monitoring (24V -> 5V)
- Current sensor (ACS712 20A or similar)

## Installation

1. Install Arduino IDE from https://www.arduino.cc/
2. Install ArduinoJson library:
   - Open Arduino IDE
   - Go to Sketch -> Include Library -> Manage Libraries
   - Search for "ArduinoJson"
   - Install version 6.x or later

3. Upload the code:
   - Open `motor_controller.ino` in Arduino IDE
   - Select your board type (Tools -> Board)
   - Select the correct port (Tools -> Port)
   - Click Upload

## Pin Connections

### Motor Drivers
- **Front Left Motor**: PWM=3, IN1=4, IN2=5
- **Front Right Motor**: PWM=6, IN1=7, IN2=8
- **Rear Left Motor**: PWM=9, IN1=10, IN2=11
- **Rear Right Motor**: PWM=12, IN1=A0, IN2=A1

### Battery Monitoring
- **Voltage Sensor**: A2 (connect via voltage divider)
- **Current Sensor**: A3 (ACS712 output)

### Voltage Divider Circuit
For battery voltage monitoring:
```
24V ----[R1: 38kΩ]---- A2 ----[R2: 10kΩ]---- GND
```
This creates a 24V to 5V divider (safe for Arduino analog input).

## Serial Protocol

Communication uses JSON over serial at 115200 baud.

### Commands to Arduino

**Motor Control:**
```json
{"cmd": "motor", "fl": 50, "fr": 50, "rl": 50, "rr": 50}
```
- `fl`, `fr`, `rl`, `rr`: Speed for each motor (-100 to 100)

**Status Request:**
```json
{"cmd": "status"}
```

### Responses from Arduino

**Success:**
```json
{"status": "ok"}
```

**Status Response:**
```json
{
  "status": "ok",
  "battery": {
    "voltage": 24.5,
    "current": 2.3
  }
}
```

**Error:**
```json
{"status": "error", "message": "error description"}
```
