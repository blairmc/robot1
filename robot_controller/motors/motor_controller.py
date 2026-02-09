"""
Motor Controller for Four-Wheel Robot
Manages the four electric motors for robot movement.
"""

import logging

logger = logging.getLogger(__name__)


class MotorController:
    """Controls four-wheel drive system via Arduino."""
    
    def __init__(self, arduino_interface):
        """
        Initialize motor controller.
        
        Args:
            arduino_interface: ArduinoInterface instance for communication
        """
        self.arduino = arduino_interface
        self.current_speed = {
            'front_left': 0,
            'front_right': 0,
            'rear_left': 0,
            'rear_right': 0
        }
        logger.info("Motor controller initialized")
    
    def set_speed(self, front_left, front_right, rear_left, rear_right):
        """
        Set speed for all four motors.
        
        Args:
            front_left: Speed for front left motor (-100 to 100)
            front_right: Speed for front right motor (-100 to 100)
            rear_left: Speed for rear left motor (-100 to 100)
            rear_right: Speed for rear right motor (-100 to 100)
        """
        speeds = {
            'front_left': self._constrain_speed(front_left),
            'front_right': self._constrain_speed(front_right),
            'rear_left': self._constrain_speed(rear_left),
            'rear_right': self._constrain_speed(rear_right)
        }
        
        self.current_speed = speeds
        self.arduino.send_motor_command(speeds)
        logger.debug(f"Motor speeds set: {speeds}")
    
    def move_forward(self, speed=50):
        """Move robot forward at given speed."""
        self.set_speed(speed, speed, speed, speed)
    
    def move_backward(self, speed=50):
        """Move robot backward at given speed."""
        self.set_speed(-speed, -speed, -speed, -speed)
    
    def turn_left(self, speed=50):
        """Turn robot left."""
        self.set_speed(-speed, speed, -speed, speed)
    
    def turn_right(self, speed=50):
        """Turn robot right."""
        self.set_speed(speed, -speed, speed, -speed)
    
    def stop(self):
        """Stop all motors."""
        self.set_speed(0, 0, 0, 0)
    
    def _constrain_speed(self, speed):
        """Constrain speed to valid range (-100 to 100)."""
        return max(-100, min(100, speed))
    
    def get_current_speeds(self):
        """Get current motor speeds."""
        return self.current_speed.copy()
