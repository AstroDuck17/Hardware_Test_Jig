#!/usr/bin/env python3
"""
Custom SPI Communication for Test Jig Web Interface
"""

import spidev
import time
from typing import List


class CustomSPI:
    """Custom SPI communication class for web interface"""
    
    def __init__(self, bus: int = 0, device: int = 0, mode: int = 0, max_speed_hz: int = 500000):
        """
        Initialize SPI communication
        
        Parameters:
        -----------
        bus : int
            SPI bus number (0 or 1)
        device : int
            SPI device/CS number (0 or 1)
        mode : int
            SPI mode (0, 1, 2, or 3)
        max_speed_hz : int
            Maximum SPI clock speed in Hz
        """
        self.bus_number = bus
        self.device_number = device
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        
        self.spi.mode = mode
        self.spi.max_speed_hz = max_speed_hz
        self.spi.bits_per_word = 8
    
    def transfer(self, data: List[int]) -> dict:
        """Full-duplex SPI transfer"""
        try:
            received = self.spi.xfer2(data)
            return {
                "success": True,
                "message": f"Transferred: {[hex(b) for b in data]}, Received: {[hex(b) for b in received]}",
                "sent": [hex(b) for b in data],
                "received": [hex(b) for b in received]
            }
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def write(self, data: List[int]) -> dict:
        """Write-only SPI transfer"""
        try:
            self.spi.writebytes(data)
            return {"success": True, "message": f"Written: {[hex(b) for b in data]}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read(self, length: int) -> dict:
        """Read-only SPI transfer"""
        try:
            data = self.spi.readbytes(length)
            return {"success": True, "message": f"Read {length} bytes: {[hex(b) for b in data]}", "data": [hex(b) for b in data]}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_mode(self, mode: int) -> dict:
        """Change SPI mode"""
        try:
            if mode not in [0, 1, 2, 3]:
                return {"success": False, "message": "Mode must be 0, 1, 2, or 3"}
            self.spi.mode = mode
            return {"success": True, "message": f"SPI mode changed to: {mode}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_speed(self, speed_hz: int) -> dict:
        """Change SPI clock speed"""
        try:
            self.spi.max_speed_hz = speed_hz
            return {"success": True, "message": f"SPI speed changed to: {speed_hz}Hz"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def get_config(self) -> dict:
        """Get current SPI configuration"""
        return {
            "success": True,
            "bus": self.bus_number,
            "device": self.device_number,
            "mode": self.spi.mode,
            "max_speed_hz": self.spi.max_speed_hz,
            "bits_per_word": self.spi.bits_per_word
        }
    
    def close(self):
        """Close SPI connection"""
        self.spi.close()
