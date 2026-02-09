# Hardware Setup Guide

This document provides detailed instructions for assembling and configuring the four-wheel robotic weed detector.

## Bill of Materials (BOM)

### Computing
- 1x Raspberry Pi 3B+ or 4 (or similar single-board computer)
- 1x Arduino Uno or Mega 2560
- 1x MicroSD card (16GB+) for Raspberry Pi
- 1x USB cable (A to B) for Arduino connection

### Power System
- 1x 24V Li-ion battery pack (6S configuration, 5000mAh+ recommended)
- 1x Battery Management System (BMS) for 6S Li-ion
- 1x DC-DC buck converter (24V to 5V, 3A+) for Raspberry Pi
- 1x Voltage divider resistors (38kΩ and 10kΩ)
- 1x Current sensor (ACS712 20A module)
- 1x Power switch
- Appropriate fuses and circuit protection

### Motors and Drivers
- 4x DC motors (24V, suitable for robot wheels)
- 2x Dual H-Bridge motor driver (L298N or similar)
- 4x Wheels (matching motor shaft)
- Motor mounting brackets

### Navigation
- 1x GPS module (NEO-6M or better, UART interface)
- 1x GPS antenna (if not included with module)

### Optional Components
- 1x Raspberry Pi Camera Module V2 (for weed detection)
- Ultrasonic distance sensors (HC-SR04) for obstacle avoidance
- IMU/Compass module for heading information
- LED indicators for status

### Chassis and Hardware
- Robot chassis or custom frame
- Mounting plates/brackets
- Screws, nuts, bolts, standoffs
- Wire (various gauges)
- Connectors (JST, Dupont, etc.)
- Heat shrink tubing

## Safety Checklist

- [ ] All connections properly insulated
- [ ] No exposed high-voltage wires
- [ ] Fuses installed in power circuit
- [ ] Emergency stop mechanism in place
- [ ] Battery secured and cannot move
- [ ] Robot tested in controlled environment

For complete assembly instructions, see README.md
