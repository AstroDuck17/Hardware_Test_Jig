#!/usr/bin/env python3
"""
Custom I2C Communication for Test Jig Web Interface
"""

import smbus2
import time
from typing import List, Optional


class CustomI2C:
    """Custom I2C communication class for web interface"""
    
    def __init__(self, bus: int = 1, device_address: int = 0x00):
        """
        Initialize I2C communication
        
        Parameters:
        -----------
        bus : int
            I2C bus number (usually 1 for Raspberry Pi 3/4)
        device_address : int
            7-bit I2C device address (0x00 to 0x7F)
        """
        self.bus_number = bus
        self.device_address = device_address
        self.bus = smbus2.SMBus(bus)
    
    def write_byte(self, data: int) -> dict:
        """Write a single byte to the I2C device"""
        try:
            self.bus.write_byte(self.device_address, data)
            return {"success": True, "message": f"Written byte: 0x{data:02X}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read_byte(self) -> dict:
        """Read a single byte from the I2C device"""
        try:
            data = self.bus.read_byte(self.device_address)
            return {"success": True, "message": f"Read byte: 0x{data:02X}", "data": data}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def write_byte_data(self, register: int, data: int) -> dict:
        """Write a byte to a specific register"""
        try:
            self.bus.write_byte_data(self.device_address, register, data)
            return {"success": True, "message": f"Written to register 0x{register:02X}: 0x{data:02X}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read_byte_data(self, register: int) -> dict:
        """Read a byte from a specific register"""
        try:
            data = self.bus.read_byte_data(self.device_address, register)
            return {"success": True, "message": f"Read from register 0x{register:02X}: 0x{data:02X}", "data": data}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def write_block_data(self, register: int, data: List[int]) -> dict:
        """Write a block of bytes to a specific register"""
        try:
            self.bus.write_i2c_block_data(self.device_address, register, data)
            return {"success": True, "message": f"Written block to register 0x{register:02X}: {[hex(b) for b in data]}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read_block_data(self, register: int, length: int) -> dict:
        """Read a block of bytes from a specific register"""
        try:
            data = self.bus.read_i2c_block_data(self.device_address, register, length)
            return {"success": True, "message": f"Read block from register 0x{register:02X}: {[hex(b) for b in data]}", "data": data}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def scan_bus(self) -> dict:
        """Scan I2C bus for connected devices"""
        devices = []
        try:
            for addr in range(0x03, 0x78):
                try:
                    self.bus.read_byte(addr)
                    devices.append(f"0x{addr:02X}")
                except:
                    pass
            return {"success": True, "message": f"Found {len(devices)} device(s)", "devices": devices}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def close(self):
        """Close I2C bus connection"""
        self.bus.close()
