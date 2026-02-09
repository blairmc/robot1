"""
Battery Monitor for 24V Li-ion Battery System
Monitors battery voltage, current, and health.
"""

import logging
import time

logger = logging.getLogger(__name__)


class BatteryMonitor:
    """Monitors 24V Li-ion battery system."""
    
    # Battery parameters for 24V Li-ion (6S configuration)
    CELL_COUNT = 6
    CELL_NOMINAL_VOLTAGE = 3.7
    CELL_MAX_VOLTAGE = 4.2
    CELL_MIN_VOLTAGE = 3.0
    
    NOMINAL_VOLTAGE = CELL_NOMINAL_VOLTAGE * CELL_COUNT  # 22.2V
    MAX_VOLTAGE = CELL_MAX_VOLTAGE * CELL_COUNT  # 25.2V
    MIN_VOLTAGE = CELL_MIN_VOLTAGE * CELL_COUNT  # 18.0V
    
    def __init__(self, arduino_interface):
        """
        Initialize battery monitor.
        
        Args:
            arduino_interface: ArduinoInterface instance for reading battery data
        """
        self.arduino = arduino_interface
        self.voltage = 0.0
        self.current = 0.0
        self.last_update = None
        logger.info("Battery monitor initialized")
    
    def update(self):
        """Update battery readings from Arduino."""
        try:
            status = self.arduino.get_status()
            if status and 'battery' in status:
                self.voltage = status['battery'].get('voltage', 0.0)
                self.current = status['battery'].get('current', 0.0)
                self.last_update = time.time()
                logger.debug(f"Battery: {self.voltage:.2f}V, {self.current:.2f}A")
                return True
        except Exception as e:
            logger.error(f"Error updating battery readings: {e}")
        
        return False
    
    def get_voltage(self):
        """Get current battery voltage."""
        return self.voltage
    
    def get_current(self):
        """Get current battery current."""
        return self.current
    
    def get_percentage(self):
        """
        Calculate battery percentage based on voltage.
        
        Returns:
            float: Battery percentage (0-100)
        """
        if self.voltage < self.MIN_VOLTAGE:
            return 0.0
        elif self.voltage > self.MAX_VOLTAGE:
            return 100.0
        else:
            percentage = ((self.voltage - self.MIN_VOLTAGE) / 
                         (self.MAX_VOLTAGE - self.MIN_VOLTAGE)) * 100
            return round(percentage, 1)
    
    def is_low_battery(self, threshold=20.0):
        """
        Check if battery is low.
        
        Args:
            threshold: Battery percentage threshold for low warning
            
        Returns:
            bool: True if battery is below threshold
        """
        return self.get_percentage() < threshold
    
    def is_critical_battery(self):
        """
        Check if battery is critically low.
        
        Returns:
            bool: True if battery voltage is below minimum safe voltage
        """
        return self.voltage < self.MIN_VOLTAGE
    
    def get_status(self):
        """
        Get comprehensive battery status.
        
        Returns:
            dict: Battery status information
        """
        return {
            'voltage': self.voltage,
            'current': self.current,
            'percentage': self.get_percentage(),
            'is_low': self.is_low_battery(),
            'is_critical': self.is_critical_battery(),
            'last_update': self.last_update
        }
