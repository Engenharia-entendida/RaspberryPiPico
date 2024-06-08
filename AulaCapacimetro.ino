#include <Wire.h>
#include "ACROBOTIC_SSD1306.h"
#define CapacitorRead 26
#define Carga 18
#define Descarga 16

int ResistorValue = 10000; // Value of the resistor in ohms (10k ohms)
unsigned long StartTime;
unsigned long EndTime;
unsigned long Time;
float Capacitance;

void setup() {
//Display============================//
  Wire.begin();
  oled.init();
  oled.clearDisplay();
  oled.setTextXY(0, 0);
  oled.putString("CapacitanceMeter");
//Pinos==============================//
  pinMode(Carga, OUTPUT);
  digitalWrite(Carga, LOW);
}

void loop() {
  digitalWrite(Carga,HIGH);
  StartTime = millis();
  while(analogRead(CapacitorRead) < 648)
    { 
     //Até que a tensão chegue em 63% de 3.3V. 
    } 

  EndTime = millis();
  Time = EndTime - StartTime;
  Capacitance = ((float)Time/ResistorValue)*1000;

 if (Capacitance > 1)
 {
  oled.clearDisplay();
  oled.setTextXY(0, 0);
  oled.putString("CapacitanceMeter");
  oled.setTextXY(2, 1);
  oled.putString("uF");
  oled.setTextXY(4, 1);
  oled.putNumber(Capacitance);
  delay(2000);
 }

 else
 {
  Capacitance = Capacitance*1000;
  oled.clearDisplay();
  oled.setTextXY(0, 0);
  oled.putString("CapacitanceMeter");
  oled.setTextXY(2, 1);
  oled.putString("nF");
  oled.setTextXY(4, 1);
  oled.putNumber(Capacitance);
  delay(2000);
 }

  digitalWrite(Carga,LOW);          
  pinMode(Descarga,OUTPUT);       
  digitalWrite(Descarga,LOW);      
  while(analogRead(CapacitorRead) > 0)
    {
      //Espera o capacitor descarregar
    } 
  pinMode(Descarga, INPUT);       
  delay(500); 
}
