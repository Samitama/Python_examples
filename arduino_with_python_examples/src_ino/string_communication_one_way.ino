int pot_values[2];
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  pot_values[0]=analogRead(A0);
  pot_values[1]= analogRead(A1);
  String msg = String("#") + "|" + String(pot_values[0]) + "|" + String(pot_values[1]) + "|";
  Serial.println(msg);   
  delay(250);   
}
