# Hardware Test Jig - SCRC

**Version:** 2.0  
**Platform:** Raspberry Pi 3  
**Framework:** FastAPI (Web), Tkinter (GUI), Python CLI  
**Last Updated:** January 16, 2026

A comprehensive, modular testing platform for Raspberry Pi 3 that enables testing and interaction with multiple hardware communication protocols and connected devices. Features a modern web interface with protocol-based navigation, custom communication capabilities, and dual theme support.

---

## 🎯 Overview

The Hardware Test Jig provides a unified interface for testing and controlling hardware devices through seven communication protocols. It offers both pre-configured device testing and low-level custom protocol communication, making it suitable for:

- **Hardware Validation:** Test sensors and modules with pre-built configurations
- **Protocol Development:** Low-level control of I2C, SPI, UART, and PWM
- **Educational Projects:** Learn hardware protocols with visual feedback
- **IoT Integration:** Interface with various sensors and actuators
- **Production Testing:** Automated device verification

---

## ✨ Key Features

### 🌐 Modern Web Interface
- **Protocol-Based Navigation:** Direct access to 7 protocols from homepage
- **Dual Theme Support:** Dark (violet) and Light (golden) themes with smooth transitions
- **Real-Time Streaming:** Server-Sent Events (SSE) for live test output
- **Modal Dialogs:** Intuitive protocol selection with existing devices vs. custom communication
- **Responsive Design:** Works on desktop, tablet, and mobile devices
- **No Display Required:** Access from any networked device

### 🔧 Dual Testing Modes

#### 1. Existing Devices (Pre-Configured)
Test popular sensors and modules with ready-to-use configurations:
- **I2C:** BH1750 Light Sensor, OLED Display, MLX90614 IR Temperature
- **SPI:** SPI OLED Display
- **UART:** PM Sensor (Air Quality - SDS011)
- **PWM:** LED Fading, RGB LED, Servo Motor
- **GPIO:** LED, Button, DHT11, Ultrasonic, DS18B20
- **ADC:** Potentiometer, LDR, TDS Water Quality
- **RS485:** Modbus RTU Communication

#### 2. Custom Communication (Protocol Control)
Low-level protocol access for development and testing:
- **I2C Custom:** Bus scanning, register read/write, block transfers
- **SPI Custom:** Mode configuration, speed control, full-duplex transfer
- **UART Custom:** Baud rate configuration, string/byte operations, buffer management
- **PWM Custom:** 4 independent pins (GPIO 18, 23, 24, 25), frequency and duty cycle control

### 🎨 User Interface Options
1. **Web App** (Primary): FastAPI-based, accessible from any browser
2. **GUI** (Desktop): Tkinter-based graphical interface for local use
3. **CLI** (Terminal): Command-line interface for scripting and automation

---

## 📁 Project Structure

```
Hardware_Test_Jig/
├── readme.md                        # This file
├── requirements.txt                 # Python dependencies (68 packages)
├── IMPLEMENTATION_SUMMARY.md        # Detailed technical documentation
├── PROJECT_DETAILS.md               # Complete project reference
├── QUICK_REFERENCE.md              # Quick start guide
├── THEME_IMPLEMENTATION.md         # Theme system documentation
├── THEME_COLORS.md                 # Color palette reference
│
└── web_test_jig/
    ├── main.py                     # Entry point (CLI/GUI launcher)
    ├── cli.py                      # Command-line interface
    ├── gui.py                      # Tkinter GUI interface
    ├── protocol_devices.csv        # Protocol-device mapping
    ├── README.md                   # Web app documentation
    ├── service.txt                 # Systemd service configuration
    │
    ├── fastapi_app/                # Web Application
    │   ├── __init__.py
    │   ├── main.py                 # FastAPI app initialization
    │   ├── routes.py               # 40+ API endpoints
    │   │
    │   ├── static/
    │   │   └── style.css          # Global styles (legacy)
    │   │
    │   └── templates/              # HTML pages (13 total)
    │       ├── homepage.html       # Protocol selection landing page
    │       │
    │       ├── devices_i2c.html    # I2C existing devices
    │       ├── devices_spi.html    # SPI existing devices
    │       ├── devices_uart.html   # UART existing devices
    │       ├── devices_pwm.html    # PWM existing devices
    │       ├── devices_gpio.html   # GPIO existing devices
    │       ├── devices_adc.html    # ADC existing devices
    │       │
    │       ├── custom_i2c.html     # I2C custom communication
    │       ├── custom_spi.html     # SPI custom communication
    │       ├── custom_uart.html    # UART custom communication
    │       ├── custom_pwm.html     # PWM custom communication (4 pins)
    │       │
    │       ├── rs485.html          # RS485 Modbus communication
    │       └── testjig.html        # Legacy page (backward compatibility)
    │
    └── lib/                        # Protocol Implementation Modules
        ├── __init__.py
        ├── pin_details.py          # GPIO pin mapping reference
        │
        ├── I2C/                    # I2C Device Modules
        │   ├── BH1750.py           # Light sensor
        │   ├── i2c_oled.py         # SH1106 OLED display
        │   ├── mlx90614.py         # IR temperature sensor
        │   └── I2C.py              # I2C utilities
        │
        ├── SPI/                    # SPI Device Modules
        │   └── spi_oled.py         # SPI OLED display
        │
        ├── UART/                   # UART Device Modules
        │   └── PM_Sensor.py        # PM2.5/PM10 air quality sensor
        │
        ├── PWM/                    # PWM Device Modules
        │   ├── fade.py             # LED brightness fading
        │   ├── rgb.py              # RGB LED color control
        │   └── servo.py            # Servo motor angle control
        │
        ├── GPIO/                   # GPIO Device Modules
        │   ├── led.py              # Simple LED on/off
        │   ├── button.py           # Push button input
        │   ├── dht.py              # DHT11 temp/humidity
        │   ├── ultrasonic.py       # HC-SR04 distance sensor
        │   └── DS18B20.py          # 1-Wire temperature sensor
        │
        ├── ADC/                    # ADC Device Modules (via ADS1115)
        │   ├── pot.py              # Potentiometer
        │   ├── ldr.py              # Light dependent resistor
        │   └── tds.py              # Water quality sensor
        │
        ├── RS485/                  # RS485 Modbus Modules
        │   ├── rsReceive.py        # Modbus client (receiver)
        │   └── rsTransmitter.py    # Modbus server (transmitter)
        │
        └── CUSTOM/                 # Custom Communication Modules (NEW)
            ├── __init__.py
            ├── custom_i2c.py       # I2C protocol control
            ├── custom_spi.py       # SPI protocol control
            ├── custom_uart.py      # UART protocol control
            └── custom_pwm.py       # PWM control (4 independent pins)
```

---

## 🚀 Quick Start

### Prerequisites
- Raspberry Pi 3 (or compatible model)
- Python 3.7 or higher
- Internet connection (for initial setup)
- Hardware devices to test (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Hardware_Test_Jig
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Enable hardware interfaces**
   ```bash
   sudo raspi-config
   ```
   - Navigate to "Interfacing Options"
   - Enable: I2C, SPI, Serial Port, 1-Wire
   - Disable Serial Console (keep Serial Port enabled)
   - Reboot when prompted

4. **Start the web application**
   ```bash
   cd web_test_jig
   uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Access the interface**
   - Open browser at `http://<raspberry-pi-ip>:8000`
   - Example: `http://192.168.1.100:8000`

### Alternative Interfaces

**Launch CLI:**
```bash
cd web_test_jig
python3 main.py --cli
```

**Launch GUI:**
```bash
cd web_test_jig
python3 main.py --gui
```

---

## 📡 Supported Protocols & Devices

### I2C Protocol (GPIO 2 & 3)
**Existing Devices:**
- **BH1750** - Digital light sensor (0x23)
- **I2C OLED** - SH1106 128x64 display (0x3C)
- **MLX90614** - Non-contact IR temperature sensor (0x5A)

**Custom Operations:**
- 🔍 Scan Bus - Detect all I2C devices
- ✏️ Write Byte / Read Byte
- 📝 Write Register / Read Register
- 📦 Write Block / Read Block

### SPI Protocol (GPIO 8, 9, 10, 11)
**Existing Devices:**
- **SPI OLED** - 128x64 monochrome display

**Custom Operations:**
- 🔄 Transfer - Full-duplex data exchange
- ✏️ Write Only / 📖 Read Only
- ⚙️ Set Mode (0-3) / Set Speed (500kHz - 10MHz)
- ℹ️ Get Config

### UART Protocol (GPIO 14 & 15)
**Existing Devices:**
- **PM Sensor (SDS011)** - Air quality sensor (PM2.5, PM10)

**Custom Operations:**
- ✏️ Write String / Write Bytes
- 📖 Read / Read Line / Read All
- 🗑️ Flush Buffer
- ℹ️ Check Buffer / Get Config
- Configurable: Baud rate (9600-230400), parity, stop bits, data bits

### PWM Protocol
**Existing Devices:**
- **LED Fading** - GPIO 18 (Hardware PWM)
- **RGB LED** - GPIOs 18, 23, 24 (Red, Green, Blue)
- **Servo Motor** - GPIO 25 (0-180 degrees)

**Custom Operations (4 Independent Pins):**
- GPIO 18 (Hardware PWM0) - Best precision
- GPIO 23 (Software PWM)
- GPIO 24 (Software PWM)
- GPIO 25 (Software PWM)

Operations: ▶️ Start, ⏹️ Stop, 🎚️ Duty Cycle (0-100%), ⚡ Frequency (1Hz-100kHz)

### GPIO Protocol
**Devices:**
- **LED** - GPIO 5 (Digital output)
- **Button** - GPIO 6 (Digital input with debounce)
- **DHT11** - GPIO 13 (Temperature & humidity)
- **Ultrasonic** - GPIOs 26 (Trigger) & 19 (Echo) - Distance measurement
- **DS18B20** - GPIO 4 (1-Wire temperature sensor)

### ADC Protocol (via ADS1115 on I2C)
**Devices:**
- **Potentiometer** - Analog voltage reading
- **LDR** - Light level measurement
- **TDS** - Water quality (total dissolved solids)

All use ADS1115 16-bit ADC connected via I2C (address 0x48)

### RS485 Protocol
**Modbus RTU Communication:**
- Configurable baud rate, parity, stop bits
- Slave ID and register address selection
- Scaling factor for sensor readings
- Transmit (server) and Receive (client) modes

---

## 🎨 Theme System

### Dark Theme (Default)
- **Colors:** Violet gradients (#8a2be2 → #da70d6)
- **Backgrounds:** Dark grays (#121212, #1e1e1e, #2e2e2e)
- **Icon:** ☀ (Sun) - "Click for Light theme"

### Light Theme
- **Colors:** Golden gradients (#DAA520 → #FDB813)
- **Backgrounds:** Whites and warm tones (#ffffff, #fef9f0, #fff8e7)
- **Icon:** 🌙 (Moon) - "Click for Dark theme"

**Features:**
- Smooth 0.3s transitions
- Persistent preference (localStorage)
- Accessible contrast ratios (WCAG AAA compliant)
- Available on all 13 pages

---

## 🌐 Web Interface Navigation

### Homepage
```
http://your-rpi-ip:8000
├─ I2C Card     → Modal → [Existing Devices] or [Custom Communication]
├─ SPI Card     → Modal → [Existing Devices] or [Custom Communication]
├─ UART Card    → Modal → [Existing Devices] or [Custom Communication]
├─ PWM Card     → Modal → [Existing Devices] or [Custom Communication]
├─ GPIO Card    → Direct → Existing Devices
├─ ADC Card     → Direct → Existing Devices
└─ RS485 Card   → Direct → Custom Communication
```

### URL Structure
- Homepage: `/` or `/homepage.html`
- Existing Devices: `/devices-{protocol}.html` (i2c, spi, uart, pwm, gpio, adc)
- Custom Communication: `/custom-{protocol}.html` (i2c, spi, uart, pwm)
- RS485: `/rs485.html`

---

## 🔌 Pin Mapping Reference

All code uses **BCM (Broadcom)** GPIO numbering.

### Complete Pin Allocation

| GPIO Pin | Protocol | Function | Device(s) |
|----------|----------|----------|-----------|
| **2** | I2C | SDA | All I2C devices, ADS1115 |
| **3** | I2C | SCL | All I2C devices, ADS1115 |
| **4** | 1-Wire | Data | DS18B20 |
| **5** | GPIO | Output | LED |
| **6** | GPIO | Input | Button |
| **8** | SPI | CE0 | SPI OLED CS |
| **9** | SPI | MISO | (Future: SD Card) |
| **10** | SPI | MOSI | SPI OLED |
| **11** | SPI | SCLK | SPI OLED |
| **13** | GPIO | I/O | DHT11 |
| **14** | UART | TXD | PM Sensor |
| **15** | UART | RXD | PM Sensor |
| **18** | PWM | Hardware PWM0 | LED Fade, RGB Red, Custom PWM |
| **19** | GPIO | Input | Ultrasonic Echo |
| **22** | SPI | GPIO | SPI OLED DC |
| **23** | PWM | Software PWM | RGB Green, Custom PWM |
| **24** | PWM | Software PWM | RGB Blue, Custom PWM |
| **25** | PWM | Software PWM | Servo, Custom PWM |
| **26** | GPIO | Output | Ultrasonic Trigger |
| **27** | SPI | GPIO | SPI OLED RST |

Detailed pin mappings available in `lib/pin_details.py` and on each device page.

---

## 📚 API Endpoints

### Page Routes (GET)
```
/                      # Homepage
/homepage.html         # Homepage (alias)
/devices-{protocol}.html    # Existing devices (i2c, spi, uart, pwm, gpio, adc)
/custom-{protocol}.html     # Custom communication (i2c, spi, uart, pwm)
/rs485.html            # RS485 Modbus page
```

### Testing Routes
```
GET  /run-test/{protocol}/{device}     # Run existing device test
POST /stop-test                        # Stop current test
```

### Custom Communication Routes (NEW)
```
GET /run-custom-i2c?operation=scan&bus=1&address=0x48&register=0x01&data=0xFF
GET /run-custom-spi?operation=transfer&bus=0&device=0&mode=0&speed=1000000&data=...
GET /run-custom-uart?operation=write_string&port=/dev/ttyS0&baudrate=9600&data=...
GET /run-custom-pwm?operation=start&pin=18&frequency=1000&duty_cycle=50
POST /cleanup-custom    # Cleanup protocol instances
     Body: { "protocol": "i2c|spi|uart|pwm" }
```

### RS485 Routes
```
GET  /run-rs485        # Run RS485 operation
POST /stop-rs485       # Stop RS485 operation
```

---

## 🛠️ Advanced Usage

### Running as System Service

Create `/etc/systemd/system/testjig.service`:
```ini
[Unit]
Description=Hardware Test Jig Web App
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Hardware_Test_Jig/web_test_jig
ExecStart=/usr/bin/python3 -m uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable testjig.service
sudo systemctl start testjig.service
```

### Custom PWM Example
```python
# Access custom PWM page: http://rpi-ip:8000/custom-pwm.html
# Select GPIO 18 (hardware PWM for best precision)
# Set frequency: 1000 Hz
# Set duty cycle: 50%
# Click "Start PWM"
# Adjust duty cycle in real-time with slider
```

### I2C Bus Scanning
```python
# Access: http://rpi-ip:8000/custom-i2c.html
# Select Bus: 1 (default)
# Click "Scan Bus"
# View detected devices with their addresses
```

---

## 📖 Documentation Files

- **IMPLEMENTATION_SUMMARY.md** - Technical implementation details, API endpoints, backend architecture
- **PROJECT_DETAILS.md** - Complete project reference, pin mappings, device specifications
- **QUICK_REFERENCE.md** - Quick start guide, common tasks, troubleshooting
- **THEME_IMPLEMENTATION.md** - Theme system architecture and implementation
- **THEME_COLORS.md** - Color palette reference for both themes

---

## 🐛 Troubleshooting

### Web App Won't Start
- Check if port 8000 is already in use: `sudo lsof -i :8000`
- Verify Python version: `python3 --version` (need 3.7+)
- Check dependencies: `pip list`

### Device Not Detected
- Verify physical connections
- Check if protocol is enabled: `sudo raspi-config`
- For I2C: Run `i2cdetect -y 1` to scan bus
- For SPI: Check `/dev/spidev0.0` exists
- For UART: Verify `/dev/ttyS0` exists and serial console is disabled

### Permission Issues
- Run with sudo if needed: `sudo python3 main.py`
- Add user to groups: `sudo usermod -a -G i2c,spi,gpio,dialout $USER`
- Reboot after adding to groups

### Custom Communication Not Working
- Click "Cleanup" button to reset instances
- Refresh the page
- Check if pins are used by other processes
- Verify correct bus/port selection

---

## 🔒 Security Notes

- Web app binds to `0.0.0.0` (all interfaces) by default
- No authentication implemented - use in trusted networks only
- Consider using reverse proxy (nginx) with HTTPS for production
- GPIO operations run with elevated privileges - use responsibly

---

