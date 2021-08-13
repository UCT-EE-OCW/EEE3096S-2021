#ifndef BINCLOCK_H
#define BINCLOCK_H

//Some reading (if you want)
//https://stackoverflow.com/questions/1674032/static-const-vs-define-vs-enum

// Function definitions
int hFormat(int hours);
void lightHours(int units);
void lightMins(int units);
int hexCompensation(int units);
int decCompensation(int units);
void initGPIO(void);
void secPWM(int units);
void hourInc(void);
void minInc(void);
void toggleTime(void);

// define constants
const char RTCAddr = //Input RTC Address here 
const char SEC_REGISTER = 0x00; // see register table in datasheet
const char MIN_REGISTER = 0x01;
const char HOUR_REGISTER = 0x02;
const char TIMEZONE = 2; // +02H00 (RSA)

// define pins
const int LED = //CHoose your LED Pin here
const int SECS = 1;
const int BTNS[] = {5,30}; // B0, B1


#endif
