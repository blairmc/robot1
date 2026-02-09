"""
Example: Basic Robot Operation
Demonstrates basic robot control and weed detection.
"""

import sys
import time
import logging
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from robot_controller.arduino import ArduinoInterface
from robot_controller.motors import MotorController
from robot_controller.gps import GPSController
from robot_controller.battery import BatteryMonitor
from robot_controller.weed_detection import WeedDetector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    """Main example function."""
    logger.info("Starting robot system...")
    
    # Initialize components
    arduino = ArduinoInterface(serial_port='/dev/ttyACM0')
    motors = MotorController(arduino)
    gps = GPSController(serial_port='/dev/ttyUSB0')
    battery = BatteryMonitor(arduino)
    detector = WeedDetector(camera_enabled=True)
    
    # Connect to Arduino
    if not arduino.connect():
        logger.error("Failed to connect to Arduino")
        return
    
    # Connect to GPS
    if not gps.connect():
        logger.warning("GPS not available, continuing without GPS")
    
    try:
        # Main operation loop
        logger.info("Robot ready. Starting operation...")
        
        for i in range(10):
            # Update battery status
            battery.update()
            battery_status = battery.get_status()
            logger.info(f"Battery: {battery_status['percentage']:.1f}% ({battery_status['voltage']:.1f}V)")
            
            # Check for low battery
            if battery_status['is_critical']:
                logger.error("Critical battery level! Stopping robot.")
                break
            
            if battery_status['is_low']:
                logger.warning("Low battery warning!")
            
            # Read GPS position
            position = gps.read_position()
            if position:
                logger.info(f"Position: {position['latitude']:.6f}, {position['longitude']:.6f}")
            
            # Perform weed detection
            result = detector.process_frame()
            if result['weed_count'] > 0:
                logger.info(f"Detected {result['weed_count']} weed(s)!")
                # Mark weed location
                weed_entry = gps.mark_weed_location(weed_type='unknown')
                if weed_entry:
                    logger.info("Weed location marked")
            
            # Simple movement pattern (example)
            if i % 4 == 0:
                logger.info("Moving forward...")
                motors.move_forward(speed=30)
            elif i % 4 == 1:
                logger.info("Turning left...")
                motors.turn_left(speed=25)
            elif i % 4 == 2:
                logger.info("Moving forward...")
                motors.move_forward(speed=30)
            elif i % 4 == 3:
                logger.info("Stopping...")
                motors.stop()
            
            time.sleep(2)
        
        # Stop motors
        logger.info("Stopping robot...")
        motors.stop()
        
        # Save weed map
        weed_locations = gps.get_weed_locations()
        if weed_locations:
            gps.save_weed_map('weed_map.json')
            logger.info(f"Saved {len(weed_locations)} weed location(s)")
        
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    finally:
        # Clean shutdown
        motors.stop()
        arduino.disconnect()
        gps.disconnect()
        logger.info("Robot system shutdown complete")


if __name__ == '__main__':
    main()
