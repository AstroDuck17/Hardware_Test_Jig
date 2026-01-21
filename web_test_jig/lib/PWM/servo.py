import RPi.GPIO as GPIO
import time
import sys

class ServoMotor:
    def __init__(self):
        self.servo_pwm = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.SERVO_PIN = 25
    
    def init_servo(self):
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.SERVO_PIN, 50)  # 50 Hz (20 ms period)
        self.servo_pwm.start(0)
    
    def set_angle(self, angle):
        if self.servo_pwm:
            duty = angle / 18 + 2
            GPIO.output(self.SERVO_PIN, True)
            self.servo_pwm.ChangeDutyCycle(duty)
            time.sleep(1)
            GPIO.output(self.SERVO_PIN, False)
            self.servo_pwm.ChangeDutyCycle(0)
    
    def rotate_180(self):
        try:
            # Rotate 180 degrees clockwise
            print("Rotating to 0 degrees")
            self.set_angle(0)
            time.sleep(1)
            
            # Rotate 180 degrees counterclockwise
            print("Rotating to 180 degrees")
            self.set_angle(180)
            time.sleep(1)
                
        except KeyboardInterrupt:
            print("Interrupted by user")
            self.cleanup_servo()
    
    def rotate_to_angle(self, angle):
        try:
            print(f"Rotating to {angle} degrees")
            self.set_angle(angle)
            time.sleep(1)  # Wait for the servo to move
        except KeyboardInterrupt:
            print("Interrupted by user")
            self.cleanup_servo()
    
    def cleanup_servo(self):
        if self.servo_pwm:
            self.servo_pwm.stop()
        self.servo_pwm = None
        GPIO.cleanup(self.SERVO_PIN)
        
    def check_connection(self):
        try:
            self.init_servo()
            # Set to neutral duty (approx 90°) to test the servo.
            self.servo_pwm.ChangeDutyCycle(7)
            time.sleep(0.1)
            self.cleanup_servo()
            return True
        except Exception:
            return False

    def activate_gui(self):
        try:
            self.init_servo()
            yield "Rotating to 0 degrees"
            self.set_angle(0)
            time.sleep(1)
            
            yield "Rotating to 180 degrees"
            self.set_angle(180)
            time.sleep(1)
            
            yield "Servo motor test completed."
            self.cleanup_servo()
            time.sleep(0.5)
        except KeyboardInterrupt:
            yield "Measurement stopped by User"
        except Exception as e:
            yield f"Error: {e}"
        finally:
            self.cleanup_servo()


    def activate_cli(self):
        try:
            self.init_servo()
            self.rotate_180()
            self.cleanup_servo()
            time.sleep(0.5)  # Add a short delay between iterations if needed
        except KeyboardInterrupt:
            print("\nMeasurement stopped by User")
        finally:
            self.cleanup_servo()

if __name__ == "__main__":
    servo_motor = ServoMotor()
    # servo_motor.activate()
    
    # Example of setting a specific angle
    specific_angle = 90
    servo_motor.rotate_to_angle(specific_angle)
