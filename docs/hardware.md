# Hardware Specifications for robot1

## Overview
The hardware architecture focuses on reliability, power efficiency, and modularity for a field-deployable robotic weeder. Primary components include controllers, actuators, sensors, and power systems.

## Controllers
- **Primary Controller (Initial Phase)**: Arduino boards for low-level control tasks, such as motor driving and sensor interfacing.
- **Advanced Controller (Operational Phase)**: Jetson Nano for high-level processing, including computer vision and AI inference.

## Mechanical Design
- **Chassis and Mobility**:
  - Differential drive configuration.
  - Two rear wheels, each driven by an independent motor.
  - Two front wheels configured as 360-degree casters for free rotation.
- **Weeding Mechanism**:
  - Mechanical arm designed to pinch and remove weeds.
  - Actuator: To be determined (e.g., servo or linear actuator for precise control).

## Motors and Drivers
- **Motors**: Stepper motors (one per rear wheel) for accurate positioning and speed control.
- **Drivers**: Compatible stepper motor drivers (e.g., A4988 or DRV8825) interfaced with Arduino.

## Sensors
- **Vision System**:
  - USB camera for general imaging.
  - OpenMV camera module for embedded vision processing and weed detection.
## Power System
- **Batteries**: Two 12V 200Ah Li-ion batteries connected in series to produce 24V.
- **Power Management**: Voltage regulators and distribution boards to supply appropriate voltages to components (e.g., 5V for Arduino, 12V/24V for motors).

## Additional Components
- Wiring and enclosures to ensure durability in outdoor environments.
- Safety features: Emergency stop switches and overcurrent protection.

## Next Steps
- Finalize part numbers and suppliers.
- Create wiring diagrams (to be added as images or schematics in this repository).