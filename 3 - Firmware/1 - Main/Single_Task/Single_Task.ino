//Single task
#include <Arduino_FreeRTOS.h>
#include <task.h>

#define SET_SIZE 40 // Number of sets of data for 1 sample size

// Function Declarations
void establishContact();
void readSensors();
void createMessage();

// Variable Declarations
TickType_t prevWakeTimeMain;
int x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3, pwr;
char x0Char[4], y0Char[4], z0Char[4], x1Char[4], y1Char[4], z1Char[4], x2Char[4], y2Char[4], z2Char[4], x3Char[4], y3Char[4], z3Char[4], pwrChar[4];
char messageStr[2500];

const int xpin0 = A0;
const int ypin0 = A1;
const int zpin0 = A2;

const int xpin1 = A5;
const int ypin1 = A6;
const int zpin1 = A7;

const int xpin2 = A8;
const int ypin2 = A9;
const int zpin2 = A10;

const int xpin3 = A13;
const int ypin3 = A14;
const int zpin3 = A15;

const int pwrpin = A4;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
  Serial.println("Start up");
  establishContact();
  xTaskCreate(TaskMain, "TaskMain", 2500, NULL, 2, NULL);
}

void loop()
{
}

void TaskMain(void *pvParameters)
{
  int readByte = 0;
  unsigned int frameNum = 0;
  char frameNumChar[4];
  unsigned int len;
  char checkSum = 0;
  int finalCheckSum = 0;

  prevWakeTimeMain = xTaskGetTickCount();

  while (1)
  {
    if (Serial.available()) {       // Check if message available
      readByte = Serial.read();     // Read message received
    }
    if (readByte == 'A') {          // Requesting for new set of data

      // addFrameNumber();
      itoa(frameNum, frameNumChar, 10);
      strcpy(messageStr, frameNumChar);
      strcat(messageStr, ",");

      for (int h = 0; h < SET_SIZE; h++) {
        readSensors();
        createMessage();
        vTaskDelayUntil(&prevWakeTimeMain, (4 / portTICK_PERIOD_MS)); // Ensure one set read every 4ms
      }

      // readPower(); addPowerToMessage();
      pwr = analogRead(pwrpin);
      //sensorValue = ((float) pwr * 5)/1023; // Declare sensorValue and current as float
      //current = sensorValue / (10/10.1);
      itoa(pwr, pwrChar, 10);
      strcat(messageStr, pwrChar);
      strcat(messageStr, ",");

      len = strlen(messageStr);

      for (int i = 0; i < len; i++) {
        checkSum ^= messageStr[i];
      }
      finalCheckSum = (int)checkSum;
      messageStr[len] = finalCheckSum;
      messageStr[len+1] = '\n';

      //Send message
      for (int j = 0; j < len + 2; j++) {
        Serial.write(messageStr[j]);
      }

      frameNum++;

      // Reset variables
      readByte = 0;
      checkSum = 0;
      finalCheckSum = 0;
    }
    else if (readByte == 'R') {
      //Resend message
      for (int k = 0; k < len + 2; k++) {
        Serial.write(messageStr[k]);
      }
      readByte = 0;
    } else if (readByte == 'H') { // Reset
      readByte = 0;
      frameNum = 0;
      checkSum = 0;
      finalCheckSum = 0;
      len = 0;
      establishContact();
    }
  }
}


void establishContact() {
  int flag = 0;
  int flag2 = 0;
  while (flag == 0) {
    if (Serial.available()) {
      if (Serial.read() == 'H') {
        flag = 1;
        Serial.write('A');   // send a capital A
      }
    }
  }
  while (flag2 == 0) {
    if (Serial.available()) {
      if (Serial.read() == 'A') {
        flag2 = 1;
      }
    } else {
      Serial.write('A');
    }
  }
  Serial.write('\n');   // send a capital A
}

void readSensors() {
  //Read accelerometers
  x0 = analogRead(xpin0);
  y0 = analogRead(ypin0);
  z0 = analogRead(zpin0);

  x1 = analogRead(xpin1);
  y1 = analogRead(ypin1);
  z1 = analogRead(zpin1);

  x2 = analogRead(xpin2);
  y2 = analogRead(ypin2);
  z2 = analogRead(zpin2);

  x3 = analogRead(xpin3);
  y3 = analogRead(ypin3);
  z3 = analogRead(zpin3);
}

void createMessage() {
  //Create messageStr char[]
  //A0
  itoa(x0, x0Char, 10);    //convert int to char[]
  strcat(messageStr, x0Char);
  strcat(messageStr, ",");
  itoa(y0, y0Char, 10);
  strcat(messageStr, y0Char);
  strcat(messageStr, ",");
  itoa(z0, z0Char, 10);
  strcat(messageStr, z0Char);
  strcat(messageStr, ",");

  //A1
  itoa(x1, x1Char, 10);    //convert int to char[]
  strcat(messageStr, x1Char);
  strcat(messageStr, ",");
  itoa(y1, y1Char, 10);
  strcat(messageStr, y1Char);
  strcat(messageStr, ",");
  itoa(z1, z1Char, 10);
  strcat(messageStr, z1Char);
  strcat(messageStr, ",");

  //A2
  itoa(x2, x2Char, 10);    //convert int to char[]
  strcat(messageStr, x2Char);
  strcat(messageStr, ",");
  itoa(y2, y2Char, 10);
  strcat(messageStr, y2Char);
  strcat(messageStr, ",");
  itoa(z2, z2Char, 10);
  strcat(messageStr, z2Char);
  strcat(messageStr, ",");

  //A3
  itoa(x3, x3Char, 10);    //convert int to char[]
  strcat(messageStr, x3Char);
  strcat(messageStr, ",");
  itoa(y3, y3Char, 10);
  strcat(messageStr, y3Char);
  strcat(messageStr, ",");
  itoa(z3, z3Char, 10);
  strcat(messageStr, z3Char);
  strcat(messageStr, ",");
}

