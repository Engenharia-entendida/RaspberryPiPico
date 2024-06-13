#include <Wire.h>
#include "ACROBOTIC_SSD1306.h"
#define PulseRead 21
#define chargePin 16
float Capacitance = 1.0e-6; 
float inductance ;
double pulse ;
double frequency ;    

void setup() {
  Wire.begin();
  oled.init();
  pinMode(chargePin, OUTPUT);
  pinMode(PulseRead, INPUT);
}
void loop() {
  digitalWrite(chargePin, HIGH);
  delay(5); 
  digitalWrite(chargePin, LOW);
  delayMicroseconds(5);
  pulse = pulseIn(PulseRead,HIGH);

  if(pulse > 0.1){
  frequency = 1.E6/(2*pulse) ;
  inductance=1./(4*Capacitance*pow(frequency , 2 )*pow(3.14159 , 2));
  inductance=inductance*1000;

  oled.clearDisplay();
  oled.setTextXY(0, 1);
  oled.putString("InductorMeter");
  oled.setTextXY(2, 1);
  oled.putString("mH");
  oled.setTextXY(4, 1);
  oled.putFloat(inductance);
  delay(1000);
  }
  else {
  oled.clearDisplay();
  oled.setTextXY(0, 1);
  oled.putString("InductorMeter");
  oled.setTextXY(2, 1);
  oled.putString("Add a inductor"); 
  delay(1000);
  }
}
