#README

The following outlines a system intended to use Balena to deploy 2 pi zeroWs:

##Pi1: Sensor node
1 container running a python script that: (1) reads a SPI ADC, (2) send that information to Pi2

##Pi2: Webserver
2 containers (uses Docker compose):
- A simple web server
- A simple TCP reciever script

These containers share a volume /data
- The tcp reciever writes to a file in /data
- The webserver reads only from this file in /data



