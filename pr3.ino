const int rightLEDpin = 2;
const int rightButtonPin = 3;
const int leftButtonPin = 9;
const int leftLEDpin = 10;

int leftButtonState = 0;
int rightButtonState = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(rightLEDpin, OUTPUT);
  pinMode(rightButtonPin, INPUT);
  pinMode(leftButtonPin, INPUT);
  pinMode(leftLEDpin, OUTPUT);
}

void loop()
{
  leftButtonState = digitalRead(leftButtonPin);
  rightButtonState = digitalRead(rightButtonPin);
  
  if (leftButtonState == HIGH) {
    digitalWrite(leftLEDpin, HIGH);
    
    Serial.print("Left\n");
    delay(1000);
  }
  else{
    digitalWrite(leftLEDpin, LOW);
  }
  
  if (rightButtonState == HIGH) {
    digitalWrite(rightLEDpin, HIGH);
    
    Serial.print("Right\n");
    delay(1000);
  }
  else {
    digitalWrite(rightLEDpin, LOW);
  }
  
}
