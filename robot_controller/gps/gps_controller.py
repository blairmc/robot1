"""
GPS Controller for Location Tracking
Manages GPS module to track robot position and map weed locations.
"""

import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)


class GPSController:
    """Manages GPS for robot location tracking."""
    
    def __init__(self, serial_port='/dev/ttyUSB0', baudrate=9600):
        """
        Initialize GPS controller.
        
        Args:
            serial_port: Serial port for GPS module
            baudrate: Baud rate for serial communication
        """
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.current_position = None
        self.weed_locations = []
        logger.info(f"GPS controller initialized on {serial_port}")
    
    def connect(self):
        """Connect to GPS module."""
        try:
            import serial
            self.gps_serial = serial.Serial(self.serial_port, self.baudrate, timeout=1)
            logger.info("GPS module connected")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to GPS: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from GPS module."""
        if hasattr(self, 'gps_serial'):
            self.gps_serial.close()
            logger.info("GPS module disconnected")
    
    def read_position(self):
        """
        Read current GPS position.
        
        Returns:
            dict: Position data with latitude, longitude, altitude
        """
        try:
            # Read NMEA sentence from GPS
            if hasattr(self, 'gps_serial'):
                line = self.gps_serial.readline().decode('ascii', errors='replace')
                position = self._parse_nmea(line)
                if position:
                    self.current_position = position
                    return position
        except Exception as e:
            logger.error(f"Error reading GPS: {e}")
        
        return self.current_position
    
    def get_current_position(self):
        """Get last known position."""
        return self.current_position
    
    def mark_weed_location(self, weed_type=None):
        """
        Mark current location as weed location.
        
        Args:
            weed_type: Optional type/species of weed detected
        """
        if self.current_position:
            weed_entry = {
                'position': self.current_position.copy(),
                'timestamp': datetime.now().isoformat(),
                'weed_type': weed_type
            }
            self.weed_locations.append(weed_entry)
            logger.info(f"Weed marked at {self.current_position}")
            return weed_entry
        return None
    
    def get_weed_locations(self):
        """Get list of all marked weed locations."""
        return self.weed_locations.copy()
    
    def save_weed_map(self, filename):
        """
        Save weed locations to file.
        
        Args:
            filename: Path to save weed map
        """
        import json
        with open(filename, 'w') as f:
            json.dump(self.weed_locations, f, indent=2)
        logger.info(f"Weed map saved to {filename}")
    
    def _parse_nmea(self, nmea_sentence):
        """
        Parse NMEA sentence to extract position.
        
        Args:
            nmea_sentence: NMEA GPS sentence string
            
        Returns:
            dict: Parsed position data or None
        """
        if not nmea_sentence.startswith('$GPGGA'):
            return None
        
        try:
            parts = nmea_sentence.split(',')
            if len(parts) > 9 and parts[2] and parts[4]:
                # Extract latitude
                lat_raw = float(parts[2])
                lat_deg = int(lat_raw / 100)
                lat_min = lat_raw - (lat_deg * 100)
                latitude = lat_deg + (lat_min / 60)
                if parts[3] == 'S':
                    latitude = -latitude
                
                # Extract longitude
                lon_raw = float(parts[4])
                lon_deg = int(lon_raw / 100)
                lon_min = lon_raw - (lon_deg * 100)
                longitude = lon_deg + (lon_min / 60)
                if parts[5] == 'W':
                    longitude = -longitude
                
                # Extract altitude
                altitude = float(parts[9]) if parts[9] else 0.0
                
                return {
                    'latitude': latitude,
                    'longitude': longitude,
                    'altitude': altitude,
                    'timestamp': time.time()
                }
        except (ValueError, IndexError) as e:
            logger.debug(f"Failed to parse NMEA: {e}")
        
        return None
