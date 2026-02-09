"""
Example: Manual Control
Allows manual control of the robot using keyboard input.
"""

import sys
import time
import logging
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from robot_controller.arduino import ArduinoInterface
from robot_controller.motors import MotorController
from robot_controller.battery import BatteryMonitor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def print_controls():
    """Print control instructions."""
    print("\n" + "="*50)
    print("ROBOT MANUAL CONTROL")
    print("="*50)
    print("Controls:")
    print("  w - Move forward")
    print("  s - Move backward")
    print("  a - Turn left")
    print("  d - Turn right")
    print("  x - Stop")
    print("  b - Check battery status")
    print("  q - Quit")
    print("="*50 + "\n")


def main():
    """Main manual control function."""
    logger.info("Starting manual control mode...")
    
    # Initialize components
    arduino = ArduinoInterface(serial_port='/dev/ttyACM0')
    motors = MotorController(arduino)
    battery = BatteryMonitor(arduino)
    
    # Connect to Arduino
    if not arduino.connect():
        logger.error("Failed to connect to Arduino")
        return
    
    print_controls()
    
    try:
        running = True
        while running:
            # Get user input
            command = input("Enter command: ").strip().lower()
            
            if command == 'w':
                logger.info("Moving forward")
                motors.move_forward(speed=50)
            elif command == 's':
                logger.info("Moving backward")
                motors.move_backward(speed=50)
            elif command == 'a':
                logger.info("Turning left")
                motors.turn_left(speed=40)
            elif command == 'd':
                logger.info("Turning right")
                motors.turn_right(speed=40)
            elif command == 'x':
                logger.info("Stopping")
                motors.stop()
            elif command == 'b':
                battery.update()
                status = battery.get_status()
                print(f"\nBattery Status:")
                print(f"  Voltage: {status['voltage']:.2f}V")
                print(f"  Current: {status['current']:.2f}A")
                print(f"  Percentage: {status['percentage']:.1f}%")
                print(f"  Low: {status['is_low']}")
                print(f"  Critical: {status['is_critical']}\n")
            elif command == 'q':
                logger.info("Quitting...")
                running = False
            else:
                print("Unknown command. Use w/a/s/d/x/b/q")
    
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        # Clean shutdown
        motors.stop()
        arduino.disconnect()
        logger.info("Manual control shutdown complete")


if __name__ == '__main__':
    main()
