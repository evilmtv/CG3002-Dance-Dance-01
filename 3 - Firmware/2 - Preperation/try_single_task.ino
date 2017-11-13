//Single task
#include <Arduino_FreeRTOS.h>
#include <task.h>

void establishContact();
void readSensors();
void createMessage();

TickType_t prevWakeTimeMain;
TickType_t prevWakeTimeRead;

int x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3;
int x0Rx, y0Rx, z0Rx, x1Rx, y1Rx, z1Rx, x2Rx, y2Rx, z2Rx, x3Rx, y3Rx, z3Rx;
char x0Char[4], y0Char[4], z0Char[4], x1Char[4], y1Char[4], z1Char[4], x2Char[4], y2Char[4], z2Char[4], x3Char[4], y3Char[4], z3Char[4];
char messageStr[1024];

#define SET_SIZE 40

const int xpin0 = A0;
const int ypin0 = A1;
const int zpin0 = A2;

const int xpin1 = A3;
const int ypin1 = A4;
const int zpin1 = A5;

const int xpin2 = A6;
const int ypin2 = A8;
const int zpin2 = A9;

const int xpin3 = A10;
const int ypin3 = A11;
const int zpin3 = A12;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Serial.println("Start up");
  establishContact();
  //Serial.println("Finish contact");
  xTaskCreate(TaskMain, "TaskMain", 2500, NULL, 2, NULL);
}

void loop()
{
}

void TaskMain(void *pvParameters)
{
  int readByte = 0;
  int frameNum = 0;
  char frameNumChar[4];
  unsigned int len;
  int sendFlag = 0;
  int counter = 0;
  char checkSum = 0;

  prevWakeTimeMain = xTaskGetTickCount();
  prevWakeTimeRead = xTaskGetTickCount();

  while (1)
  {
    if (Serial.available()) {
      readByte = Serial.read();
    }
    if (readByte == 'A') {
      sendFlag = 0;
      counter = 0;

      itoa(frameNum, frameNumChar, 10);
      strcpy(messageStr, frameNumChar);
      strcat(messageStr, ",");

      for (int h = 0; h < SET_SIZE; h++) {
        readSensors();
        createMessage();
        vTaskDelayUntil(&prevWakeTimeMain, (4 / portTICK_PERIOD_MS));
      }

      len = strlen(messageStr);

      for (int i = 0; i < len; i++) {
        checkSum ^= messageStr[i];
      }
      messageStr[len] = checkSum;
      messageStr[len + 1] = '\n';

      //Send message
      for (int j = 0; j < len + 2; j++) {
        Serial.write(messageStr[j]);
      }

      sendFlag = 1;
      frameNum++;
      readByte = 0;
    }
    else if (readByte == 'R') {
      //Resend message
      for (int k = 0; k < len + 2; k++) {
        Serial.write(messageStr[k]);
      }
      readByte = 0;
    }
    else {
      if (sendFlag)
      {
        counter++;
        if (counter == 30000)
        {
          //Resend message
          for (int m = 0; m < len + 2; m++) {
            Serial.write(messageStr[m]);
          }
          counter = 0;
        }
      }
    }
  }
  vTaskDelayUntil(&prevWakeTimeMain, (500 / portTICK_PERIOD_MS));
}


void establishContact() {
  int flag = 0;
  while (flag == 0)
  {
    if (Serial.available())
    {
      if (Serial.read() == 'H')
      {
        flag = 1;
      }
    }
  }
  Serial.write('A');   // send a capital A
}

void readSensors() {
  //Reads accelerometers
  x0 = analogRead(xpin0);
  delay(1);
  y0 = analogRead(ypin0);
  delay(1);
  z0 = analogRead(zpin0);
  delay(1);

  x1 = analogRead(xpin1);
  delay(1);
  y1 = analogRead(ypin1);
  delay(1);
  z1 = analogRead(zpin1);
  delay(1);

  x2 = analogRead(xpin2);
  delay(1);
  y2 = analogRead(ypin2);
  delay(1);
  z2 = analogRead(zpin2);
  delay(1);

  x3 = analogRead(xpin3);
  delay(1);
  y3 = analogRead(ypin3);
  delay(1);
  z3 = analogRead(zpin3);
}

void createMessage() {
  //Create messageStr char[]
  //A0
  itoa(x0Rx, x0Char, 10);    //convert int to char[]
  strcat(messageStr, x0Char);
  strcat(messageStr, ",");
  itoa(y0Rx, y0Char, 10);
  strcat(messageStr, y0Char);
  strcat(messageStr, ",");
  itoa(z0Rx, z0Char, 10);
  strcat(messageStr, z0Char);
  strcat(messageStr, ",");

  //A1
  itoa(x1Rx, x1Char, 10);    //convert int to char[]
  strcat(messageStr, x1Char);
  strcat(messageStr, ",");
  itoa(y1Rx, y1Char, 10);
  strcat(messageStr, y1Char);
  strcat(messageStr, ",");
  itoa(z1Rx, z1Char, 10);
  strcat(messageStr, z1Char);
  strcat(messageStr, ",");

  //A2
  itoa(x2Rx, x2Char, 10);    //convert int to char[]
  strcat(messageStr, x2Char);
  strcat(messageStr, ",");
  itoa(y2Rx, y2Char, 10);
  strcat(messageStr, y2Char);
  strcat(messageStr, ",");
  itoa(z2Rx, z2Char, 10);
  strcat(messageStr, z2Char);
  strcat(messageStr, ",");

  //A3
  itoa(x3Rx, x3Char, 10);    //convert int to char[]
  strcat(messageStr, x3Char);
  strcat(messageStr, ",");
  itoa(y3Rx, y3Char, 10);
  strcat(messageStr, y3Char);
  strcat(messageStr, ",");
  itoa(z3Rx, z3Char, 10);
  strcat(messageStr, z3Char);
  strcat(messageStr, ",");
}

