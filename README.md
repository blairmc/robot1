# robot1 - Four-Wheel Robotic Weeder

A GPS-enabled four-wheel robot for autonomous weed detection and mapping in yards.

## Overview

This project implements a robotic weed detection system using:
- **24V Li-ion batteries** for power
- **Four electric motors** for mobility
- **Arduino** for low-level motor control
- **Python** for high-level control and logic
- **GPS module** for location tracking and weed mapping
- **Camera/sensors** for weed detection (framework included)

## Features

- Four-wheel drive control with independent motor control
- GPS-based location tracking and weed mapping
- Battery monitoring for 24V Li-ion system (6S configuration)
- Serial communication between Python and Arduino
- Extensible weed detection framework
- Example scripts for operation and testing

## Hardware Requirements

### Main Components
- Raspberry Pi (or similar) for running Python code
- Arduino Uno/Mega for motor control
- 2x Motor driver boards (L298N or similar)
- 4x DC motors (24V compatible)
- 24V Li-ion battery pack (6S - 22.2V nominal)
- GPS module (UART/Serial compatible)
- Voltage sensor (voltage divider for battery monitoring)
- Current sensor (ACS712 20A or similar)

### Optional
- Camera module for weed detection
- Additional sensors (ultrasonic, IR, etc.)

## Software Installation

### 1. Python Setup

```bash
# Clone the repository
git clone https://github.com/blairmc/robot1.git
cd robot1

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Arduino Setup

1. Install Arduino IDE
2. Install ArduinoJson library (via Library Manager)
3. Upload `arduino_code/motor_controller.ino` to your Arduino
4. See `arduino_code/README.md` for detailed hardware connections

## Configuration

Edit `config/robot_config.ini` to match your hardware setup:
- Serial ports for Arduino and GPS
- Battery voltage thresholds
- Motor speed limits
- Detection parameters

## Usage

### Basic Operation

```bash
python examples/basic_operation.py
```

This example demonstrates:
- Connecting to Arduino and GPS
- Reading battery status
- Performing simple movement patterns
- Detecting and mapping weed locations

### Manual Control

```bash
python examples/manual_control.py
```

Control the robot with keyboard:
- `w` - Move forward
- `s` - Move backward
- `a` - Turn left
- `d` - Turn right
- `x` - Stop
- `b` - Check battery status
- `q` - Quit

### GPS Mapping

```bash
python examples/gps_mapping.py
```

Demonstrates GPS positioning and weed location mapping.

## Project Structure

```
robot1/
├── arduino_code/          # Arduino motor controller code
│   ├── motor_controller.ino
│   └── README.md
├── robot_controller/      # Python package
│   ├── motors/           # Motor control module
│   ├── gps/              # GPS tracking module
│   ├── arduino/          # Arduino interface
│   ├── battery/          # Battery monitoring
│   └── weed_detection/   # Weed detection framework
├── config/               # Configuration files
│   └── robot_config.ini
├── examples/             # Example scripts
│   ├── basic_operation.py
│   ├── manual_control.py
│   └── gps_mapping.py
├── requirements.txt      # Python dependencies
└── README.md
```

## Module Documentation

### Motors Module
Controls four-wheel drive system via Arduino serial interface.
- `MotorController`: Main class for motor control
- Methods: `move_forward()`, `move_backward()`, `turn_left()`, `turn_right()`, `stop()`

### GPS Module
Handles GPS positioning and weed location mapping.
- `GPSController`: GPS interface and data parsing
- Methods: `read_position()`, `mark_weed_location()`, `save_weed_map()`

### Arduino Module
Serial communication with Arduino for motor commands.
- `ArduinoInterface`: Serial protocol handler
- JSON-based command protocol

### Battery Module
Monitors 24V Li-ion battery status.
- `BatteryMonitor`: Battery voltage and current monitoring
- Automatic percentage calculation and low battery warnings

### Weed Detection Module
Framework for weed detection (placeholder for actual implementation).
- `WeedDetector`: Detection and classification framework
- Ready for integration with camera and ML models

## Development

### Adding Weed Detection

The weed detection module is a framework. To implement actual detection:

1. Install computer vision libraries:
   ```bash
   pip install opencv-python numpy
   ```

2. Implement detection logic in `robot_controller/weed_detection/weed_detector.py`
3. Train or integrate a weed classification model
4. Update the `detect()` and `identify_weed_type()` methods

### Extending Navigation

To add autonomous navigation:
- Implement waypoint navigation using GPS
- Add obstacle avoidance using sensors
- Create scan patterns for yard coverage

## Safety

- Always test in a safe, controlled environment
- Monitor battery levels to prevent over-discharge
- Implement emergency stop functionality
- Ensure proper motor driver heat dissipation
- Use appropriate fuses and circuit protection

## License

This project is open source. See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Support

For questions or issues, please open an issue on GitHub.
