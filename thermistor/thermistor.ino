void setup() {
  Serial.begin(115200);
}

unsigned long sum=0;
int measurements = 10000;

void loop() {
  sum = 0L;
  for (int i=0; i<measurements; i++) {
    sum += analogRead(A0);
  }
  Serial.println("X" + String(float(sum)/float(measurements)) + "Y");
}
