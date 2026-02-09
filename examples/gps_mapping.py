"""
Example: GPS Mapping
Demonstrates GPS-based weed mapping and navigation.
"""

import sys
import time
import logging
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from robot_controller.gps import GPSController

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    """Main GPS mapping example."""
    logger.info("Starting GPS mapping example...")
    
    # Initialize GPS
    gps = GPSController(serial_port='/dev/ttyUSB0')
    
    # Connect to GPS
    if not gps.connect():
        logger.error("Failed to connect to GPS")
        return
    
    try:
        logger.info("Reading GPS positions. Press Ctrl+C to stop and save map.")
        
        # Read positions for 30 seconds
        for i in range(30):
            position = gps.read_position()
            
            if position:
                logger.info(f"Position {i+1}: "
                          f"Lat={position['latitude']:.6f}, "
                          f"Lon={position['longitude']:.6f}, "
                          f"Alt={position['altitude']:.1f}m")
                
                # Simulate weed detection every 5 readings
                if (i + 1) % 5 == 0:
                    logger.info("Simulating weed detection...")
                    weed_entry = gps.mark_weed_location(weed_type='dandelion')
                    if weed_entry:
                        logger.info(f"Weed marked at position")
            else:
                logger.warning(f"No GPS fix yet ({i+1}/30)")
            
            time.sleep(1)
        
        # Display summary
        weed_locations = gps.get_weed_locations()
        logger.info(f"\nSummary:")
        logger.info(f"Total weeds marked: {len(weed_locations)}")
        
        # Save weed map
        if weed_locations:
            filename = 'weed_map.json'
            gps.save_weed_map(filename)
            logger.info(f"Weed map saved to {filename}")
            
            # Display weed locations
            print("\nWeed Locations:")
            for idx, weed in enumerate(weed_locations, 1):
                pos = weed['position']
                print(f"  {idx}. Lat={pos['latitude']:.6f}, "
                      f"Lon={pos['longitude']:.6f}, "
                      f"Type={weed['weed_type']}, "
                      f"Time={weed['timestamp']}")
    
    except KeyboardInterrupt:
        logger.info("\nInterrupted by user")
    finally:
        # Save map before exit
        weed_locations = gps.get_weed_locations()
        if weed_locations:
            gps.save_weed_map('weed_map.json')
            logger.info(f"Saved {len(weed_locations)} weed location(s)")
        
        gps.disconnect()
        logger.info("GPS mapping shutdown complete")


if __name__ == '__main__':
    main()
