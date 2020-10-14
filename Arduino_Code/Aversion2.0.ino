#include <Wire.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>

const int mic1 = A0; //microphone

Adafruit_MMA8451 mma = Adafruit_MMA8451(); //accelerometer

void setup(void) {
  Serial.begin(9600);

  /*Initialise the accelerometer*/
  if (! mma.begin()) {
    Serial.println("Couldnt start");
    while (1);
  }

  /*Set the accelerometer range*/
  mma.setRange(MMA8451_RANGE_2_G);
  
}

void loop() {
  // Read the 'raw' data in 14-bit counts
  mma.read();
  
  /* Get a new sensor event */ 
  sensors_event_t event; 
  mma.getEvent(&event);

  /*Read from microphone*/
  int m1 = analogRead(mic1);
  
  /* Display the results (acceleration is measured in m/s^2) */
  Serial.println(event.acceleration.x); 
  Serial.println(event.acceleration.y); 
  Serial.println(event.acceleration.z);
  Serial.println(float(m1));  
  delay(20);
  
}
