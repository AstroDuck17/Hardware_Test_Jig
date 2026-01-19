#!/usr/bin/env python3
"""
Custom UART Communication for Test Jig Web Interface
Enhanced with flow control and advanced operations
"""

import serial
import time
from typing import Optional, Union, List


class CustomUART:
    """Custom UART communication class for web interface with full control"""
    
    def __init__(self, port: str = "/dev/ttyS0", baudrate: int = 9600,
                 bytesize: int = 8, parity: str = 'N', stopbits: float = 1,
                 timeout: Optional[float] = 1.0, xonxoff: bool = False,
                 rtscts: bool = False, dsrdtr: bool = False):
        """
        Initialize UART communication
        
        Parameters:
        -----------
        port : str
            Serial port (e.g., "/dev/ttyS0", "/dev/ttyAMA0", "/dev/ttyUSB0")
        baudrate : int
            Baud rate
        bytesize : int
            Number of data bits (5, 6, 7, or 8)
        parity : str
            Parity checking: 'N', 'E', 'O', 'M', 'S'
        stopbits : float
            Number of stop bits (1, 1.5, or 2)
        timeout : float
            Read timeout in seconds
        xonxoff : bool
            Enable software flow control
        rtscts : bool
            Enable hardware (RTS/CTS) flow control
        dsrdtr : bool
            Enable hardware (DSR/DTR) flow control
        """
        self.port_name = port
        
        parity_map = {
            'N': serial.PARITY_NONE,
            'E': serial.PARITY_EVEN,
            'O': serial.PARITY_ODD,
            'M': serial.PARITY_MARK,
            'S': serial.PARITY_SPACE
        }
        
        stopbits_map = {
            1: serial.STOPBITS_ONE,
            1.5: serial.STOPBITS_ONE_POINT_FIVE,
            2: serial.STOPBITS_TWO
        }
        
        bytesize_map = {
            5: serial.FIVEBITS,
            6: serial.SIXBITS,
            7: serial.SEVENBITS,
            8: serial.EIGHTBITS
        }
        
        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=bytesize_map.get(bytesize, serial.EIGHTBITS),
            parity=parity_map.get(parity.upper(), serial.PARITY_NONE),
            stopbits=stopbits_map.get(stopbits, serial.STOPBITS_ONE),
            timeout=timeout,
            xonxoff=xonxoff,
            rtscts=rtscts,
            dsrdtr=dsrdtr
        )
    
    def write(self, data: Union[str, List[int]]) -> dict:
        """Write data to UART"""
        try:
            if isinstance(data, str):
                bytes_written = self.serial.write(data.encode('utf-8'))
                return {"success": True, "message": f"Written {bytes_written} bytes: {data}"}
            elif isinstance(data, list):
                bytes_written = self.serial.write(bytes(data))
                return {"success": True, "message": f"Written {bytes_written} bytes: {[hex(b) for b in data]}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read(self, size: int = 1) -> dict:
        """Read bytes from UART"""
        try:
            data = self.serial.read(size)
            if data:
                return {"success": True, "message": f"Read {len(data)} bytes: {data.hex()}", "data": data.hex()}
            else:
                return {"success": True, "message": "No data received", "data": ""}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read_line(self) -> dict:
        """Read a line from UART"""
        try:
            line = self.serial.readline().decode('utf-8', errors='ignore').strip()
            return {"success": True, "message": f"Read line: {line}", "data": line}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def read_all(self) -> dict:
        """Read all available data"""
        try:
            data = self.serial.read(self.serial.in_waiting or 1)
            if data:
                return {"success": True, "message": f"Read {len(data)} bytes: {data.hex()}", "data": data.hex()}
            else:
                return {"success": True, "message": "No data available", "data": ""}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def flush(self) -> dict:
        """Flush input and output buffers"""
        try:
            self.serial.flush()
            self.serial.reset_input_buffer()
            self.serial.reset_output_buffer()
            return {"success": True, "message": "Buffers flushed"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def in_waiting(self) -> dict:
        """Get number of bytes in input buffer"""
        try:
            count = self.serial.in_waiting
            return {"success": True, "message": f"Bytes in input buffer: {count}", "count": count}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def out_waiting(self) -> dict:
        """Get number of bytes in output buffer"""
        try:
            count = self.serial.out_waiting
            return {"success": True, "message": f"Bytes in output buffer: {count}", "count": count}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def write_read(self, data: Union[str, List[int]], read_size: int = 1024, delay: float = 0.1) -> dict:
        """Write data and read response"""
        try:
            write_result = self.write(data)
            if not write_result["success"]:
                return write_result
            time.sleep(delay)
            read_result = self.read(read_size)
            return {"success": True, "message": f"Write: {write_result['message']}, Read: {read_result['message']}", "data": read_result.get("data", "")}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_timeout(self, timeout: Optional[float]) -> dict:
        """Change read timeout"""
        try:
            self.serial.timeout = timeout
            return {"success": True, "message": f"Timeout changed to: {timeout}s"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_dtr(self, state: bool) -> dict:
        """Set DTR (Data Terminal Ready) line"""
        try:
            self.serial.dtr = state
            return {"success": True, "message": f"DTR set to: {'HIGH' if state else 'LOW'}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_rts(self, state: bool) -> dict:
        """Set RTS (Request To Send) line"""
        try:
            self.serial.rts = state
            return {"success": True, "message": f"RTS set to: {'HIGH' if state else 'LOW'}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def get_control_lines(self) -> dict:
        """Get state of control lines (CD, CTS, DSR)"""
        try:
            cd = self.serial.cd
            cts = self.serial.cts
            dsr = self.serial.dsr
            return {
                "success": True,
                "message": f"CD: {'HIGH' if cd else 'LOW'}, CTS: {'HIGH' if cts else 'LOW'}, DSR: {'HIGH' if dsr else 'LOW'}",
                "cd": cd,
                "cts": cts,
                "dsr": dsr
            }
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def send_break(self, duration: float = 0.25) -> dict:
        """Send break condition"""
        try:
            self.serial.send_break(duration)
            return {"success": True, "message": f"Break sent for {duration}s"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def set_baudrate(self, baudrate: int) -> dict:
        """Change baud rate"""
        try:
            self.serial.baudrate = baudrate
            return {"success": True, "message": f"Baud rate changed to: {baudrate}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {e}"}
    
    def get_config(self) -> dict:
        """Get current UART configuration"""
        return {
            "success": True,
            "port": self.serial.port,
            "baudrate": self.serial.baudrate,
            "bytesize": self.serial.bytesize,
            "parity": self.serial.parity,
            "stopbits": self.serial.stopbits,
            "timeout": self.serial.timeout,
            "xonxoff": self.serial.xonxoff,
            "rtscts": self.serial.rtscts,
            "dsrdtr": self.serial.dsrdtr,
            "is_open": self.serial.is_open
        }
    
    def close(self):
        """Close UART connection"""
        if self.serial.is_open:
            self.serial.close()
