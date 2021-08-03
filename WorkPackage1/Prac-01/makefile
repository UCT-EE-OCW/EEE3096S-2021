.RECIPEPREFIX +=
CC = gcc
CFLAGS = -Wall -lm -lrt -lwiringPi -g

PROG = bin/*
OBJS = obj/*

default:
    mkdir -p bin obj
    $(CC) $(CFLAGS) -c src/BinClock.c -o obj/BinClock
    $(CC) $(CFLAGS) -c src/CurrentTime.c -o obj/CurrentTime
    $(CC) $(CFLAGS) obj/BinClock obj/CurrentTime -o bin/Clock

run:
    sudo ./bin/Clock

run_gdb:
    sudo gdb ./bin/Clock

clean:
    rm $(PROG) $(OBJS)
    rmdir bin obj
