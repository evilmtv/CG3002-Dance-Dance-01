
//Single task
#include <Arduino_FreeRTOS.h>
#include <task.h>

#define SET_SIZE 50 // Number of sets of data for 1 sample size

// Function Declarations
void establishContact();
void readSensors();
void createMessage();

// Variable Declarations
TickType_t prevWakeTimeMain;
int x0, y0, z0, x1, y1, z1, x2, y2, z2, volt, amp;
char x0Char[4], y0Char[4], z0Char[4], x1Char[4], y1Char[4], z1Char[4], x2Char[4], y2Char[4], z2Char[4], voltChar[4], ampChar[4];
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

const int amppin = A13;
const int voltpin = A15;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
  Serial.println("Start up");
  establishContact();
  xTaskCreate(TaskMain, "TaskMain", 3000, NULL, 2, NULL);
}

void loop()
{
}

void TaskMain(void *pvParameters)
{
  int readByte = 0;
  unsigned int frameNum = 1;
  char frameNumChar[4];
  unsigned int len;
  char checkSum = 0;
  int checkSum2;
  char finalCheckSum[4];

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

      prevWakeTimeMain = xTaskGetTickCount();
      for (int h = 0; h < SET_SIZE; h++) {
        readSensors();
        createMessage();
        vTaskDelayUntil(&prevWakeTimeMain, (10 / portTICK_PERIOD_MS)); // Ensure one set read every 10ms
      }

      // readVolt(); addVoltToMessage();
      volt = analogRead(voltpin);
      itoa(volt, voltChar, 10);
      strcat(messageStr, voltChar);
      strcat(messageStr, ",");

      // readAmp(); addAmpToMessage();
      amp = analogRead(amppin); // current = ((float) amp * 5) / 1023 / (10 / 10.1)
      itoa(amp, ampChar, 10);
      strcat(messageStr, ampChar);

      // addCheckSum();
      len = strlen(messageStr);
      for (int i = 0; i < len; i++) {
        checkSum ^= messageStr[i];
      }
      checkSum2 = (int)checkSum;
      itoa(checkSum2, finalCheckSum, 10);
      strcat(messageStr, ","); // exclude last ',' from checksum
      strcat(messageStr, finalCheckSum);
      len = strlen(messageStr);
      messageStr[len + 1] = '\n'; 
      
      //Send message
      for (int j = 0; j < len + 2; j++) {
        Serial.write(messageStr[j]);
      }

      frameNum++;

      // Reset variables
      readByte = 0;
      checkSum = 0;
    }
    else if (readByte == 'R') {
      //Resend message
      for (int k = 0; k < len + 2; k++) {
        Serial.write(messageStr[k]);
      }
      readByte = 0;
    } else if (readByte == 'H') { // Reset
      readByte = 0;
      frameNum = 1;
      checkSum = 0;
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
  Serial.write('\n');
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
}

void createMessage() {
  //Create messageStr char[]
  
  //Acc 0
  itoa(x0, x0Char, 10);    //convert int to char[]
  strcat(messageStr, x0Char);
  strcat(messageStr, ",");
  itoa(y0, y0Char, 10);
  strcat(messageStr, y0Char);
  strcat(messageStr, ",");
  itoa(z0, z0Char, 10);
  strcat(messageStr, z0Char);
  strcat(messageStr, ",");

  //Acc 1
  itoa(x1, x1Char, 10);    //convert int to char[]
  strcat(messageStr, x1Char);
  strcat(messageStr, ",");
  itoa(y1, y1Char, 10);
  strcat(messageStr, y1Char);
  strcat(messageStr, ",");
  itoa(z1, z1Char, 10);
  strcat(messageStr, z1Char);
  strcat(messageStr, ",");

  //Acc 2
  itoa(x2, x2Char, 10);    //convert int to char[]
  strcat(messageStr, x2Char);
  strcat(messageStr, ",");
  itoa(y2, y2Char, 10);
  strcat(messageStr, y2Char);
  strcat(messageStr, ",");
  itoa(z2, z2Char, 10);
  strcat(messageStr, z2Char);
  strcat(messageStr, ",");

}

