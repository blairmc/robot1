"""
Arduino Interface for Motor Control
Handles serial communication with Arduino for motor control.
"""

import logging
import json
import time

logger = logging.getLogger(__name__)


class ArduinoInterface:
    """Interface for communicating with Arduino motor controller."""
    
    def __init__(self, serial_port='/dev/ttyACM0', baudrate=115200):
        """
        Initialize Arduino interface.
        
        Args:
            serial_port: Serial port for Arduino connection
            baudrate: Baud rate for serial communication
        """
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.connected = False
        logger.info(f"Arduino interface initialized on {serial_port}")
    
    def connect(self):
        """Connect to Arduino."""
        try:
            import serial
            self.serial = serial.Serial(self.serial_port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for Arduino to reset
            self.connected = True
            logger.info("Connected to Arduino")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Arduino: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Disconnect from Arduino."""
        if self.connected and hasattr(self, 'serial'):
            self.serial.close()
            self.connected = False
            logger.info("Disconnected from Arduino")
    
    def send_motor_command(self, speeds):
        """
        Send motor speed command to Arduino.
        
        Args:
            speeds: Dictionary with motor speeds
                   {'front_left': speed, 'front_right': speed,
                    'rear_left': speed, 'rear_right': speed}
        """
        if not self.connected:
            logger.warning("Not connected to Arduino")
            return False
        
        try:
            command = {
                'cmd': 'motor',
                'fl': speeds['front_left'],
                'fr': speeds['front_right'],
                'rl': speeds['rear_left'],
                'rr': speeds['rear_right']
            }
            
            message = json.dumps(command) + '\n'
            self.serial.write(message.encode())
            logger.debug(f"Sent command: {command}")
            return True
        except Exception as e:
            logger.error(f"Error sending motor command: {e}")
            return False
    
    def read_response(self):
        """
        Read response from Arduino.
        
        Returns:
            dict: Parsed response or None
        """
        if not self.connected:
            return None
        
        try:
            if self.serial.in_waiting > 0:
                line = self.serial.readline().decode('utf-8').strip()
                if line:
                    return json.loads(line)
        except Exception as e:
            logger.error(f"Error reading Arduino response: {e}")
        
        return None
    
    def get_status(self):
        """
        Request status from Arduino.
        
        Returns:
            dict: Status information
        """
        if not self.connected:
            return None
        
        try:
            command = {'cmd': 'status'}
            message = json.dumps(command) + '\n'
            self.serial.write(message.encode())
            
            # Wait for response
            time.sleep(0.1)
            return self.read_response()
        except Exception as e:
            logger.error(f"Error getting Arduino status: {e}")
            return None
