const int ena = 9;
const int in1 = 8;
const int in2 = 7;

const int enb = 3;
const int in3 = 5;
const int in4 = 4;

const int trig = 11;
const int echo = 10;

void setup() {
  pinMode(ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  
  pinMode(enb, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  long duration, cm;

  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duration = pulseIn(echo, HIGH);
  cm = duration * 0.034 / 2;

  if (cm < 20) {
    motor(-200, -200);
    delay(500);
    motor(200, 0);
    delay(500);
  } 
  else {
    motor(200, 200);
  }
}

void motor(int motorL, int motorR) {
  bool dirL = motorL > 0;
  bool dirR = motorR > 0;
  
  if (dirL) {
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }
  else {
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  }

  if (dirR) {
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else {
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  analogWrite(ena, abs(motorL));
  analogWrite(enb, abs(motorR));
}