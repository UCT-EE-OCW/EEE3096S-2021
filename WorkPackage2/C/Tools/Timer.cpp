//==============================================================================
// Copyright (C) John-Philip Taylor
// tyljoh010@myuct.ac.za
//
// This file is part of the EEE4084F Course
//
// This file is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>
//==============================================================================

#include "Timer.h"
//------------------------------------------------------------------------------

#ifdef __WIN32__
 #include <windows.h>
#else
 #include <time.h>
#endif
//------------------------------------------------------------------------------

static double Frequency;
static double Start;
//------------------------------------------------------------------------------

void tic(){
 static bool First = true;

 #ifdef __WIN32__
  LARGE_INTEGER Time;
  if(First){
   QueryPerformanceFrequency(&Time);
   Frequency = Time.QuadPart;
   printf("Clock resolution: %lg ns\n", 1e9/Frequency);
   First = false;
  }
  QueryPerformanceCounter(&Time);
  Start = (double)Time.QuadPart / Frequency;

 #else
  // This is an alternative, using <sys/time.h>.  It is not as accurate though.
  // timeval Time;
  // gettimeofday(&Time, 0);
  // Start = (double)(Time.tv_sec) + (double)(Time.tv_usec)*1e-6;

  timespec Time;
  if(First){
   clock_getres(CLOCK_MONOTONIC, &Time);
   Start = (double)(Time.tv_sec) + (double)(Time.tv_nsec)*1e-9;
   printf("Clock resolution: %lg ns\n", Start*1e9);
   First = false;
  }
  clock_gettime(CLOCK_MONOTONIC, &Time);
  Start = (double)(Time.tv_sec) + (double)(Time.tv_nsec)*1e-9;
 #endif
}
//------------------------------------------------------------------------------

double toc(){
 double End;

 #ifdef __WIN32__
  LARGE_INTEGER Time;
  QueryPerformanceCounter(&Time);
  End = (double)Time.QuadPart / Frequency;
  return End - Start;

 #else
  //timeval Time;
  //gettimeofday(&Time, 0);
  //End = (double)(Time.tv_sec) + (double)(Time.tv_usec)*1e-6;

  timespec Time;
  clock_gettime(CLOCK_MONOTONIC, &Time);
  End = (double)(Time.tv_sec) + (double)(Time.tv_nsec)*1e-9;
  return End - Start;
 #endif
}
//------------------------------------------------------------------------------


