#!/usr/bin/env python3
"""
Custom PWM Communication for Test Jig Web Interface
"""

import RPi.GPIO as GPIO
import time
from typing import Optional


class CustomPWM:
    """Custom PWM class for web interface"""
    
    # Available PWM pins on the test jig
    AVAILABLE_PINS = {
        18: "GPIO 18 (PWM0 - Hardware)",
        23: "GPIO 23 (Software PWM)",
        24: "GPIO 24 (Software PWM)",
        25: "GPIO 25 (Software PWM)"
    }
    
    def __init__(self, pin: int, frequency: float = 1000):
        """
        Initialize PWM on a GPIO pin
        
        Parameters:
        -----------
        pin : int
            GPIO pin number (BCM numbering: 18, 23, 24, or 25)
        frequency : float
            PWM frequency in Hz (default: 1000Hz)
        """
        if pin not in self.AVAILABLE_PINS:
            raise ValueError(f"Pin {pin} not available. Use: {list(self.AVAILABLE_PINS.keys())}")
        
        self.pin = pin
        self.frequency = frequency
        self.duty_cycle = 0
        self.is_running = False
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)
        
        self.pwm = GPIO.PWM(self.pin, frequency)
    
    def start(self, duty_cycle: float = 0) -> dict:
        """Start PWM output"""
        try:
            self.duty_cycle = duty_cycle
            self.pwm.start(self.duty_cycle)
            self.is_running = True
            return {"success": True, "message": f"PWM started on GPIO {self.pin} with duty cycle: {self.duty_cycle}%"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def stop(self) -> dict:
        """Stop PWM output"""
        try:
            self.pwm.stop()
            self.is_running = False
            return {"success": True, "message": f"PWM stopped on GPIO {self.pin}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def change_duty_cycle(self, duty_cycle: float) -> dict:
        """Change PWM duty cycle"""
        try:
            if not 0 <= duty_cycle <= 100:
                return {"success": False, "message": f"Duty cycle must be between 0 and 100"}
            
            self.duty_cycle = duty_cycle
            self.pwm.ChangeDutyCycle(duty_cycle)
            return {"success": True, "message": f"Duty cycle changed to: {duty_cycle}%"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def change_frequency(self, frequency: float) -> dict:
        """Change PWM frequency"""
        try:
            if frequency <= 0:
                return {"success": False, "message": "Frequency must be positive"}
            
            self.frequency = frequency
            self.pwm.ChangeFrequency(frequency)
            return {"success": True, "message": f"Frequency changed to: {frequency}Hz"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_pulse_width(self, pulse_width_ms: float) -> dict:
        """Set duty cycle based on pulse width in milliseconds"""
        try:
            period_ms = 1000.0 / self.frequency
            duty_cycle = (pulse_width_ms / period_ms) * 100
            
            if not 0 <= duty_cycle <= 100:
                return {"success": False, "message": f"Pulse width results in invalid duty cycle"}
            
            self.duty_cycle = duty_cycle
            self.pwm.ChangeDutyCycle(duty_cycle)
            return {"success": True, "message": f"Pulse width set to {pulse_width_ms}ms (duty cycle: {duty_cycle:.2f}%)"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def get_status(self) -> dict:
        """Get current PWM status"""
        return {
            "success": True,
            "pin": self.pin,
            "frequency": self.frequency,
            "duty_cycle": self.duty_cycle,
            "is_running": self.is_running,
            "period_ms": 1000.0 / self.frequency,
            "on_time_ms": (self.duty_cycle / 100) * (1000.0 / self.frequency)
        }
    
    def cleanup(self):
        """Stop PWM and cleanup GPIO"""
        if self.is_running:
            self.pwm.stop()
        GPIO.cleanup(self.pin)
