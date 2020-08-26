const int mic = A0; //microphone
const int xpin = A1; // x-axis of the accelerometer
const int ypin = A2; // y-axis
const int zpin = A3; // z-axis


void setup(){
  Serial.begin(9600);
}
 
void loop()
{
  int x = analogRead(xpin); //- 331.5)/65*9.8)-28.12; //read from xpin
  delay(1); //
  int y = analogRead(ypin); //)- 329.5)/68.5*9.8)-26.68; //read from ypin
  delay(1); 
  int z = analogRead(zpin); //- 340)/68*9.8)-39.20; //read from zpin
  delay(1);
  int m = analogRead(mic); // read from microphone
  float zero_G = 512.0; //ADC is 0~1023 the zero g output equal to Vs/2
  float scale = 102.3; //ADXL335330 Sensitivity is 330mv/g


  
  Serial.println((((float)x - 331.5)/65*9.8)-28.12); //print x value on serial monitor
  Serial.println((((float)y - 329.5)/68.5*9.8)-26.68); //print y value on serial monitor
  Serial.println((((float)z - 340.0)/68*9.8)-39.20); //print z value on serial monitor
  Serial.println((float)m); // print microphone values on serial monitor
  
  
  delay(600); //wait for 1 second 
}
