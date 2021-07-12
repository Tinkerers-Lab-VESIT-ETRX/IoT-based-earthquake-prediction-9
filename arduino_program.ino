#define A_X A2
#define A_Y A1
#define A_Z A0
#define G_X1 A5
#define G_Y1 A4
#define G_Z1 A3



// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {  
 
 
  float A_Xval = analogRead(A_X);
  float A_Yval = analogRead(A_Y);
  float A_Zval = analogRead(A_Z);
  float G_X1val = analogRead(G_X1);
  float G_Y1val = analogRead(G_Y1);
  float G_Z1val = analogRead(G_Z1);

  Serial.println("A_X = "+ String(A_Xval)+ ", A_Y= " + String(A_Yval)+  ", A_Z = " +String(A_Zval)+ ", G_X1 = " +String(G_X1val)+ ", G_Y1 = " +String(G_Y1val)+ ", G_Z1 = " +String(G_Z1val));
  delay(1000);
}
