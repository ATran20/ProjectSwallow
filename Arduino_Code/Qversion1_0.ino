unsigned long timer = 0;
long loopTime = 5000;   // microseconds
String m_recvString = "";
double m_scaleFactor = 2;

void setup() {
  Serial.begin(9600);
  timer = micros();
}

void loop() {
  timeSync(loopTime);
  
  int val = (analogRead(0) - 512) *m_scaleFactor ;
  sendToPC(&val);
  getSerialData();
}

void timeSync(unsigned long deltaT)
{
  unsigned long currTime = micros();
  long timeToDelay = deltaT - (currTime - timer);
  if (timeToDelay > 5000)
  {
    delay(timeToDelay / 1000);
    delayMicroseconds(timeToDelay % 1000);
  }
  else if (timeToDelay > 0)
  {
    delayMicroseconds(timeToDelay);
  }
  else
  {
      // timeToDelay is negative so we start immediately
  }
  timer = currTime + timeToDelay;
}

void sendToPC(int* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 2);
}

void sendToPC(double* data)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}

void getSerialData()
{
  while (Serial.available())
  {
    char input = Serial.read();
    m_recvString += input;
    if (input == '%')   // this is the end of message marker so that the program knows when to update the g_scaleFactor variable 
    {
      int index = m_recvString.indexOf('%');
      String tmp = m_recvString.substring(0, index);  // remove the '%' sign
      m_scaleFactor = tmp.toFloat();
      m_recvString = "";
      break;
    }
  }
  m_recvString = "";  // probably redundant but just for safety
}
