# UART Communication Enhancement Summary

## Overview
The custom UART communication system has been enhanced to provide comprehensive control over serial communication, including flow control, advanced operations, and complete parameter configuration.

## New Features Added

### 1. Flow Control Options
The web interface now supports all three types of serial flow control:

- **XON/XOFF (Software Flow Control)**: Uses special characters to pause/resume transmission
- **RTS/CTS (Hardware Flow Control)**: Request To Send / Clear To Send handshaking
- **DSR/DTR (Hardware Flow Control)**: Data Set Ready / Data Terminal Ready handshaking

### 2. Timeout Configuration
- **Configurable Read Timeout**: Set timeout from 0 to 10 seconds (default: 1.0s)
- **Dynamic Timeout Adjustment**: Change timeout during runtime with `set_timeout` operation

### 3. Additional Configuration Options
- **Byte Size**: Expanded from 7-8 bits to support 5, 6, 7, and 8-bit data
- **Delay Parameter**: Configurable delay for write-read operations (0-5 seconds)
- **Break Duration**: Configurable break signal duration (0.1-2 seconds)

### 4. New Operations

#### Basic Operations
- **Write & Read**: Combined operation that writes data and reads response with configurable delay
- **Check Output**: Monitor bytes waiting in output buffer (`out_waiting`)
- **Check Input**: Monitor bytes waiting in input buffer (`in_waiting`)

#### Advanced Operations
- **Set Baud Rate**: Dynamically change baud rate during runtime
- **Set Timeout**: Adjust read timeout without reinitializing port
- **Set DTR**: Control Data Terminal Ready line (ON/OFF)
- **Set RTS**: Control Request To Send line (ON/OFF)
- **Read Control Lines**: Read status of CD (Carrier Detect), CTS, and DSR lines
- **Send Break**: Send break signal on TX line for specified duration
- **Get Config**: Display complete UART configuration including flow control

## User Interface Enhancements

### Configuration Panel
The left column now includes:
- Timeout input field (number, 0.1s increments)
- Flow control checkboxes grouped together
- Delay input for write-read operations
- Break duration input
- DTR/RTS control line checkboxes

### Operations Panel
Split into two sections:

**Basic Operations** (9 buttons):
- Write String
- Write Bytes
- Read
- Read Line
- Read All
- Write & Read (NEW)
- Flush
- Check Input (renamed from "Check Buffer")
- Check Output (NEW)

**Advanced Operations** (7 buttons):
- Set Baud Rate (NEW)
- Set Timeout (NEW)
- Set DTR (NEW)
- Set RTS (NEW)
- Read Control Lines (NEW)
- Send Break (NEW)
- Get Config

### Confirmation Modal
Enhanced to display all configuration parameters:
- Serial Port
- Baud Rate
- Parity
- Stop Bits
- Byte Size
- **Timeout** (NEW)
- **Flow Control** (NEW - shows active flow control types)
- Data to Write
- Read Size
- **Delay** (NEW)
- **DTR State** (NEW - ON/OFF)
- **RTS State** (NEW - ON/OFF)
- **Break Duration** (NEW)

## Backend Implementation

### CustomUART Class (`lib/CUSTOM/custom_uart.py`)
Enhanced `__init__` method to accept:
```python
def __init__(self, port, baudrate, bytesize, parity, stopbits, 
             timeout=1.0, xonxoff=False, rtscts=False, dsrdtr=False)
```

New methods added:
- `out_waiting()`: Get bytes in output buffer
- `write_read(data, size, delay)`: Write and read with delay
- `set_timeout(timeout)`: Change timeout dynamically
- `set_dtr(state)`: Control DTR line
- `set_rts(state)`: Control RTS line
- `get_control_lines()`: Read CD, CTS, DSR status
- `send_break(duration)`: Send break signal
- `set_baudrate(baudrate)`: Change baud rate dynamically

### FastAPI Route (`fastapi_app/routes.py`)
Enhanced `/run-custom-uart` endpoint signature:
```python
async def run_custom_uart(request, operation, port="/dev/ttyS0",
                         baudrate=9600, bytesize=8, parity="N",
                         stopbits=1, timeout=1.0, xonxoff=False,
                         rtscts=False, dsrdtr=False, data="", size=1,
                         delay=0.1, dtr=False, rts=False, 
                         break_duration=0.25)
```

Operation handlers added for all new operations with proper parameter passing.

### HTML Template (`fastapi_app/templates/custom_uart.html`)
- Added 7 new form groups for configuration
- Split operations into Basic (9) and Advanced (7) sections
- Enhanced `showConfirmModal()` to display flow control status
- Updated `executeOperation()` to send all 16 parameters
- Modal displays flow control as comma-separated list

## Usage Examples

### Example 1: UART with Hardware Flow Control
1. Select port: `/dev/ttyUSB0`
2. Set baud rate: `115200`
3. Enable RTS/CTS flow control (check box)
4. Set timeout: `2.0` seconds
5. Click "Write String" to send data

The modal will show:
```
Flow Control: RTS/CTS
Timeout: 2.0s
```

### Example 2: Check Control Lines Status
1. Configure UART as needed
2. Click "Read Control Lines"
3. Output shows: `CD: LOW, CTS: HIGH, DSR: HIGH`

### Example 3: Write and Read with Delay
1. Enter data: `AT+CGMI`
2. Set read size: `128`
3. Set delay: `0.5` seconds
4. Click "Write & Read"
5. System writes data, waits 0.5s, then reads response

## Technical Notes

### Flow Control Implementation
- **XON/XOFF**: Implemented via `serial.xonxoff` parameter
- **RTS/CTS**: Implemented via `serial.rtscts` parameter  
- **DSR/DTR**: Implemented via `serial.dsrdtr` parameter
- All three can be enabled simultaneously if needed

### Parameter Passing
All parameters are properly typed:
- Booleans: `xonxoff`, `rtscts`, `dsrdtr`, `dtr`, `rts`
- Floats: `timeout`, `delay`, `break_duration`, `stopbits`
- Integers: `baudrate`, `bytesize`, `size`
- Strings: `port`, `parity`, `data`, `operation`

### Error Handling
All operations return structured responses:
```python
{
    "success": True/False,
    "message": "Operation result or error message",
    "data": "Optional data payload"
}
```

## Files Modified

1. **custom_uart.html** (152 lines modified)
   - Added 7 new configuration form groups
   - Added 7 new operation buttons
   - Enhanced modal with 8 new display fields
   - Updated JavaScript functions for 16 parameters

2. **routes.py** (already enhanced in previous session)
   - Updated endpoint signature with 9 new parameters
   - Added handlers for 7 new operations
   - Enhanced initialization with flow control

3. **custom_uart.py** (already enhanced in previous session)
   - Updated `__init__` with 3 flow control parameters
   - Added 9 new methods
   - Enhanced `get_config()` to return flow control status

## Compatibility
- Works with all standard serial ports: `/dev/ttyS*`, `/dev/ttyAMA*`, `/dev/ttyUSB*`
- Compatible with USB-to-serial adapters
- Supports all standard baud rates (9600 to 115200 and beyond)
- Flow control depends on hardware support (some USB adapters may not support all types)

## Testing Recommendations

1. **Test basic operations** without flow control first
2. **Test flow control** with known compatible hardware
3. **Verify timeout** works for slow devices
4. **Test control lines** with devices that use hardware handshaking
5. **Verify write-read** with command-response protocols (e.g., AT commands, Modbus)

## Future Enhancements (Optional)

- Add support for custom parity types (Mark, Space)
- Implement data logging to file
- Add hex/ASCII toggle for data display
- Implement continuous read mode with auto-scroll
- Add support for multiple simultaneous UART instances
