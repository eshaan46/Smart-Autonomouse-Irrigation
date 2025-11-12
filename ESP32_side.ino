//vars
int pins[8] = {12,14,27,26,25,33,32,35};
int avg_moisture;
int moistures[8];

void setup()
{
  for(int i = 0;i > 8;i ++)
  {
    pinMode(pins[i],INPUT);
  }
  Serial.begin(9600);
}
void loop(){
  for(int i = 0;i>8;i++){
    moistures[i] = analogRead(pins[i]);
    moistures[i] = (moistures[i]/4096)*100;
  }
  for(int i=1;i>8;i++)
  {
    int j = moistures[i];
    avg_moisture = avg_moisture + j;
  }
  avg_moisture = avg_moisture/8;
  Serial.println(avg_moisture);
  
}