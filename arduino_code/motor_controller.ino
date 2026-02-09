/*
 * Four-Wheel Robot Motor Controller
 * 
 * Controls four electric motors for a robot weed detector.
 * Communicates with Python via serial using JSON protocol.
 * 
 * Hardware connections:
 * - Motor Driver Pins (L298N or similar):
 *   Front Left:  PWM=3, IN1=4, IN2=5
 *   Front Right: PWM=6, IN1=7, IN2=8
 *   Rear Left:   PWM=9, IN1=10, IN2=11
 *   Rear Right:  PWM=12, IN1=A0, IN2=A1
 * 
 * - Battery Monitor:
 *   Voltage Divider: A2 (24V -> 5V using voltage divider)
 *   Current Sensor: A3 (ACS712 or similar)
 */

#include <ArduinoJson.h>

// Motor driver pins
struct Motor {
  int pwm;
  int in1;
  int in2;
};

Motor frontLeft = {3, 4, 5};
Motor frontRight = {6, 7, 8};
Motor rearLeft = {9, 10, 11};
Motor rearRight = {12, A0, A1};

// Battery monitoring pins
const int VOLTAGE_PIN = A2;
const int CURRENT_PIN = A3;

// Voltage divider ratio (24V to 5V)
// Using 38kΩ and 10kΩ resistors: (38kΩ + 10kΩ) / 10kΩ = 4.8
const float VOLTAGE_DIVIDER_RATIO = 4.8;

void setup() {
  Serial.begin(115200);
  
  // Initialize motor pins
  initMotor(frontLeft);
  initMotor(frontRight);
  initMotor(rearLeft);
  initMotor(rearRight);
  
  // Stop all motors initially
  stopAllMotors();
  
  Serial.println("{\"status\":\"ready\"}");
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    processCommand(input);
  }
}

void initMotor(Motor motor) {
  pinMode(motor.pwm, OUTPUT);
  pinMode(motor.in1, OUTPUT);
  pinMode(motor.in2, OUTPUT);
}

void processCommand(String json) {
  StaticJsonDocument<200> doc;
  DeserializationError error = deserializeJson(doc, json);
  
  if (error) {
    sendError("Invalid JSON");
    return;
  }
  
  const char* cmd = doc["cmd"];
  
  if (strcmp(cmd, "motor") == 0) {
    int fl = doc["fl"];
    int fr = doc["fr"];
    int rl = doc["rl"];
    int rr = doc["rr"];
    
    setMotorSpeed(frontLeft, fl);
    setMotorSpeed(frontRight, fr);
    setMotorSpeed(rearLeft, rl);
    setMotorSpeed(rearRight, rr);
    
    sendSuccess();
  }
  else if (strcmp(cmd, "status") == 0) {
    sendStatus();
  }
  else {
    sendError("Unknown command");
  }
}

void setMotorSpeed(Motor motor, int speed) {
  // Constrain speed to -100 to 100
  speed = constrain(speed, -100, 100);
  
  // Map to PWM range (0-255)
  int pwmValue = map(abs(speed), 0, 100, 0, 255);
  
  // Set direction
  if (speed > 0) {
    digitalWrite(motor.in1, HIGH);
    digitalWrite(motor.in2, LOW);
  } else if (speed < 0) {
    digitalWrite(motor.in1, LOW);
    digitalWrite(motor.in2, HIGH);
  } else {
    digitalWrite(motor.in1, LOW);
    digitalWrite(motor.in2, LOW);
  }
  
  // Set speed
  analogWrite(motor.pwm, pwmValue);
}

void stopAllMotors() {
  setMotorSpeed(frontLeft, 0);
  setMotorSpeed(frontRight, 0);
  setMotorSpeed(rearLeft, 0);
  setMotorSpeed(rearRight, 0);
}

float readBatteryVoltage() {
  int raw = analogRead(VOLTAGE_PIN);
  float voltage = (raw / 1023.0) * 5.0 * VOLTAGE_DIVIDER_RATIO;
  return voltage;
}

float readBatteryCurrent() {
  int raw = analogRead(CURRENT_PIN);
  // ACS712 20A: 2.5V = 0A, 185mV/A
  float voltage = (raw / 1023.0) * 5.0;
  float current = (voltage - 2.5) / 0.185;
  return current;
}

void sendStatus() {
  StaticJsonDocument<200> doc;
  doc["status"] = "ok";
  
  JsonObject battery = doc.createNestedObject("battery");
  battery["voltage"] = readBatteryVoltage();
  battery["current"] = readBatteryCurrent();
  
  serializeJson(doc, Serial);
  Serial.println();
}

void sendSuccess() {
  Serial.println("{\"status\":\"ok\"}");
}

void sendError(const char* message) {
  StaticJsonDocument<100> doc;
  doc["status"] = "error";
  doc["message"] = message;
  
  serializeJson(doc, Serial);
  Serial.println();
}
