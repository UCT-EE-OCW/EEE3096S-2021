# Prac 2 
Working with benchmarking and architecture specific optimisations.
Special thanks to [KaliumPuceon](https://github.com/KaliumPuceon) for their contributions to the Threaded C implementation.

## Folder Contents
#### Python
- PythonHeterodyning.py  - Source code for python
- Timing.py - Module that handles timing of the critical section
- data.py - Contains source data
- olddata.py - Original source data. Not relevant for the practical

#### C
- Tools/ - Contains the Timing library used
- bin/ - Contains the compiled files
- obj/ - Contains object files
- src/ - The source code (header files, etc)
  - globals.h - The source data
  - CHeterodyning.c and CHeterodyning.h are source for non-parallel version
  - CHeterodyning_threaded.c and CHeterodyning_threaded.h are source for the threaded version
- makefile

## Running the Prac
#### Python
To run the Python benchamrk, enter into the Python directory, and run
```./PythonHeterodyning.py```
You may need to give it permission to execute. To do so, you can run
```chmod +x PythonHeterodyning.py```

#### C
All running of the C code is done through ```make``` commands. 
- ```make``` will compile CHeterodyning.c
- ```make run``` will run CHeterodyning
- ```make threaded``` will compile the threaded version of CHeterodyning
- ```make run_threaded``` will run the threaded version
- ```make clean``` will clean the object and binary files that have been compiled

## Editing configurations
To run some experiments for C, you need to make edits to certain files and then recompile the relevant practical (threaded/unthreaded).
#### Editing bit widths
To edit bit withs, you need to make edits to
- globals.h
  - This is a large file, so editing it will be laggy. Just be patient :)
- CHeterodyning.c (if you're working on the unthreaded version)
- CHeterodyning_threaded.c (if you're working on the threaded version)
- makefile (if you need to run at 16 bits)
Possible bit widths include:
- ```double``` - 64 bit floating point
- ```float``` - 32 bit floating point
- ```__fp16``` - 16 bit floating point
  - You need to add ```-mfp16-format=ieee``` to ```$(CFLAGS)``` to use 16 bit floating point
#### Editing compiler flags
To edit compiler flags, changes need to be made in the makefile. Read the practical for further instruction.
