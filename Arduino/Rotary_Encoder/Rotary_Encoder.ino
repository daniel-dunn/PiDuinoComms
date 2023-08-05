#define outputA 7
#define outputB 6

int counter = 0;
int aState;
int aLastState;


void setup() {
  pinMode(outputA, INPUT);
  pinMode(outputB, INPUT);

  Serial.begin(9600);

  aLastState = digitalRead(outputA);
}

void loop() {
  aState = digitalRead(outputA);
  if(aState != aLastState){
    if(digitalRead(outputB) != aState){
      counter++;
    } else{
      counter--;
    }
    Serial.print(counter);
    Serial.print("\n");
  }
  aLastState = aState;
}
