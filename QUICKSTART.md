# Quick Start Guide

Get your four-wheel robotic weed detector up and running quickly.

## Prerequisites

- Raspberry Pi with Raspbian/Raspberry Pi OS installed
- Arduino with motor controller code uploaded
- All hardware assembled and connected (see docs/HARDWARE_SETUP.md)
- Python 3.7+ installed

## Installation (5 minutes)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/blairmc/robot1.git
   cd robot1
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configure serial ports:**
   
   Find your serial ports:
   ```bash
   ls -l /dev/tty*
   ```
   
   Edit `config/robot_config.ini` and set:
   - `arduino_port` to your Arduino port (usually `/dev/ttyACM0`)
   - `gps_port` to your GPS port (usually `/dev/ttyUSB0`)

4. **Add user to dialout group** (for serial port access):
   ```bash
   sudo usermod -a -G dialout $USER
   ```
   
   Log out and back in for this to take effect.

## First Test (2 minutes)

### Test 1: Manual Control

Control the robot with keyboard:

```bash
python3 examples/manual_control.py
```

Commands:
- `w` - Forward
- `s` - Backward
- `a` - Turn left
- `d` - Turn right
- `x` - Stop
- `b` - Battery status
- `q` - Quit

### Test 2: GPS Mapping

Test GPS positioning:

```bash
python3 examples/gps_mapping.py
```

This will:
- Read GPS positions for 30 seconds
- Mark simulated weed locations
- Save results to `weed_map.json`

### Test 3: Full System

Run the complete system:

```bash
python3 examples/basic_operation.py
```

This demonstrates:
- Motor control
- GPS tracking
- Battery monitoring
- Weed detection framework

## Troubleshooting

### "Permission denied" on serial port
```bash
sudo chmod 666 /dev/ttyACM0  # Temporary fix
# Or add user to dialout group (permanent)
sudo usermod -a -G dialout $USER
```

### Arduino not connecting
1. Check USB cable is connected
2. Verify Arduino code is uploaded
3. Try a different USB port
4. Check port with: `ls -l /dev/ttyACM*`

### GPS not getting fix
- Ensure antenna has clear view of sky
- Wait 2-5 minutes for initial fix
- Check GPS LED is blinking
- Verify correct baud rate (9600)

### Motors not moving
1. Check battery voltage (should be 18-25V)
2. Verify motor driver connections
3. Test with basic Arduino sketch first
4. Check enable pins on motor drivers

## Next Steps

1. **Calibrate motors**: Adjust speeds if motors run at different rates
2. **Test outdoors**: GPS requires outdoor operation
3. **Add weed detection**: Integrate camera and ML model
4. **Create mission plans**: Add waypoint navigation
5. **Optimize battery**: Monitor and tune for runtime

## Safety Reminders

- ⚠️ Always test in safe, open area
- ⚠️ Keep emergency stop readily accessible
- ⚠️ Monitor battery levels
- ⚠️ Start with low speeds (25-30%)
- ⚠️ Never leave robot unattended while running

## Getting Help

- Check README.md for detailed documentation
- See docs/HARDWARE_SETUP.md for assembly help
- Review example code in `examples/` directory
- Open an issue on GitHub for bugs or questions

## Sample Output

Successful operation looks like:

```
2026-02-09 12:00:00 - INFO - Starting robot system...
2026-02-09 12:00:01 - INFO - Connected to Arduino
2026-02-09 12:00:02 - INFO - Battery: 85.5% (24.1V)
2026-02-09 12:00:03 - INFO - Position: 37.774929, -122.419416
2026-02-09 12:00:04 - INFO - Moving forward...
2026-02-09 12:00:06 - INFO - Detected 1 weed(s)!
2026-02-09 12:00:06 - INFO - Weed location marked
```

Happy robot building! 🤖🌱
