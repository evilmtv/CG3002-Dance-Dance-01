//Queues, handshake, semaphore, acknowledge working, structure, resend, serializing works, scheduling can be improved but okay for nw
#include <Arduino_FreeRTOS.h>
#include <task.h>
#include <queue.h>
#include <semphr.h>

void establishContact();
QueueHandle_t xQueue0;
SemaphoreHandle_t xMutexSemaphore = NULL;
SemaphoreHandle_t xBinarySemaphore;
TickType_t prevWakeTimeRead;
TickType_t prevWakeTimeSend;

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

int readByte = 0;


// the setup function runs once when you press reset or power the board
void setup() {

  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  //Serial.println("Start up");
  establishContact();
  //Serial.println("Finish contact");
  xTaskCreate(TaskR, "TaskR", 2000, NULL, 2, NULL);
  xTaskCreate(Accel0, "Accel0", 2500, NULL, 2, NULL);
  xQueue0 = xQueueCreate(36, sizeof(int));
  xMutexSemaphore = xSemaphoreCreateMutex();
  xBinarySemaphore = xSemaphoreCreateBinary();
  xSemaphoreGive(xBinarySemaphore);
}

void loop()
{
}

void TaskR(void *pvParameters)
{
  /*
    float x0 = 0;
    float y0 = 0;
    float z0 = 0;
    float x1 = 0;
    float y1 = 0;
    float z1 = 0;
    float x2 = 0;
    float y2 = 0;
    float z2 = 0;
    float x3 = 0;
    float y3 = 0;
    float z3 = 0;
  */
  int x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3;
  //int x0Int, y0Int, z0Int, x1Int, y1Int, z1Int, x2Int, y2Int, z2Int, x3Int, y3Int, z3Int;
  prevWakeTimeRead = xTaskGetTickCount();
  while (1)
  {
    if (xSemaphoreTake(xBinarySemaphore, 0)) {
      if (xSemaphoreTake(xMutexSemaphore, 0)) {

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

        //Convert float to int
        Serial.println("Read");
        xQueueSendToBack(xQueue0, &x0, 0);
        xQueueSendToBack(xQueue0, &y0, 0);
        xQueueSendToBack(xQueue0, &z0, 0);
        xQueueSendToBack(xQueue0, &x1, 0);
        xQueueSendToBack(xQueue0, &y1, 0);
        xQueueSendToBack(xQueue0, &z1, 0);
        xQueueSendToBack(xQueue0, &x2, 0);
        xQueueSendToBack(xQueue0, &y2, 0);
        xQueueSendToBack(xQueue0, &z2, 0);
        xQueueSendToBack(xQueue0, &x3, 0);
        xQueueSendToBack(xQueue0, &y3, 0);
        xQueueSendToBack(xQueue0, &z3, 0);

        vTaskDelayUntil(&prevWakeTimeRead, (4/portTICK_PERIOD_MS ));
        xSemaphoreGive(xMutexSemaphore);
      }
    }
  }
}

void Accel0(void *pvParameters)
{
  //int readByte = 0;
  int x0Rx, y0Rx, z0Rx, x1Rx, y1Rx, z1Rx, x2Rx, y2Rx, z2Rx, x3Rx, y3Rx, z3Rx;
  char x0Char[4], y0Char[4], z0Char[4], x1Char[4], y1Char[4], z1Char[4], x2Char[4], y2Char[4], z2Char[4], x3Char[4], y3Char[4], z3Char[4];
  int frameNum = 0;
  char frameNumChar[4];
  char messageStr[256];
  unsigned int len;
  int sendFlag = 0;
  int counter = 0;
  char checkSum = 0;

  prevWakeTimeSend = xTaskGetTickCount();
  while (1)
  {
    if (xSemaphoreTake(xMutexSemaphore, 0)) {
      if (Serial.available() > 0) {
        readByte = Serial.read();
      }
      if (readByte == 'A') {
        sendFlag = 0;
        counter = 0;
        xSemaphoreGive(xBinarySemaphore);
        xSemaphoreGive(xMutexSemaphore);
        vTaskDelayUntil(&prevWakeTimeSend, (1/portTICK_PERIOD_MS ));
        xQueueReceive(xQueue0, &x0Rx, 0);
        xQueueReceive(xQueue0, &y0Rx, 0);
        xQueueReceive(xQueue0, &z0Rx, 0);
        xQueueReceive(xQueue0, &x1Rx, 0);
        xQueueReceive(xQueue0, &y1Rx, 0);
        xQueueReceive(xQueue0, &z1Rx, 0);
        xQueueReceive(xQueue0, &x2Rx, 0);
        xQueueReceive(xQueue0, &y2Rx, 0);
        xQueueReceive(xQueue0, &z2Rx, 0);
        xQueueReceive(xQueue0, &x3Rx, 0);
        xQueueReceive(xQueue0, &y3Rx, 0);
        xQueueReceive(xQueue0, &z3Rx, 0);

        //Serial.println("receive");

        //Create messageStr char[]
        itoa(frameNum, frameNumChar, 10);
        strcpy(messageStr, frameNumChar);
        strcat(messageStr, ",");
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

        len = strlen(messageStr);

        for (int i = 0; i < len; i++) {
          checkSum ^= messageStr[i];
        }
        Serial.println("Send");
        messageStr[len] = checkSum;
        messageStr[len + 1] = '\n';
        for (int j = 0; j < len + 2; j++) {
          Serial.write(messageStr[j]);
        }

        sendFlag = 1;
        frameNum++;
        readByte = 0;
        checkSum = 0;
        counter = 0;
      }
      else if (readByte == 'R') {
        //Resend message
        for (int k = 0; k < len + 2; k++) {
          Serial.write(messageStr[k]);
        }
        sendFlag = 1;
        readByte = 0;
        counter = 0;
        vTaskDelayUntil(&prevWakeTimeSend, (2/portTICK_PERIOD_MS ));
        xSemaphoreGive(xMutexSemaphore);
      }

      else if (readByte == 'H') {
        frameNum = 0;
        sendFlag = 0;
        readByte = 0;
        checkSum = 0;
        counter = 0;      
        establishContact();  
        vTaskDelayUntil(&prevWakeTimeSend, (2/portTICK_PERIOD_MS ));      
        xSemaphoreGive(xBinarySemaphore);
        xSemaphoreGive(xMutexSemaphore);
      }
      else {
        vTaskDelayUntil(&prevWakeTimeSend, (2/portTICK_PERIOD_MS ));
        xSemaphoreGive(xMutexSemaphore);
        }
//      else {
//        if (sendFlag)
//        {
//          readByte = 0;
//          counter++;
//          if (counter == 30000)
//          {
//            //Resend message
//            for (int m = 0; m < len + 2; m++) {
//              Serial.write(messageStr[m]);
//            }
//            counter = 0;
//          }
//        }
//        vTaskDelayUntil(&prevWakeTimeSend, (2/portTICK_PERIOD_MS ));
//        xSemaphoreGive(xMutexSemaphore);
//      }
    }
  }

}


void establishContact() {
  int flag = 0;
  int flag1 = 0;
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

  while (flag1 == 0) {
    Serial.write('A');   // send a capital A
    if (Serial.available())
    {
      if (Serial.read() == 'A')
      {
        flag1 = 1;
      }
    }
    delay(10);
  }
  Serial.write('\n');
  readByte = 'A';
}

