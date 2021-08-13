#ifndef Prac2_threadded_h
#define Prac2_threadded_h
//------------------------------------------------------------------------------

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
//------------------------------------------------------------------------------

#include "Timer.h"
#include "globals.h"
//------------------------------------------------------------------------------

#define Thread_Count 1
//------------------------------------------------------------------------------

pthread_mutex_t Mutex; // One mutex

//------------------------------------------------------------------------------

// The thread "main" function.  Receives a unique thread ID as parameter
void* Thread_Main(void* Parameter);
//------------------------------------------------------------------------------

#endif
