#README

The following outlines a system intended to use Balena to deploy 2 pi zeroWs.  Core code has been removed and replaced with #TODO statements but the outline, supporting docker files, and TODO instructions should make the prac much easier:

##Pi1: Sensor node
1 container running a python script that: (1) reads a SPI ADC, (2) send that information to Pi2
Note:  The adafruit libraries used to interact with the ADC take 15-20min to install the 1st time, they will be cached thereafter for more rapid dev

##Pi2: Webserver
2 containers (uses Docker compose):
- A simple web server
- A simple TCP reciever script

These containers share a volume /data
- The tcp reciever writes to a file in /data
- The webserver reads only from this file in /data
Note: for rapid and easier dev, put both pis in [local mode](https://www.balena.io/docs/learn/develop/local-mode/) and use the local IP addresses.  For good reason BalenaOS by deafult blocks most ports and uses a complex VPN structure.  However, for the sake of this prac it's more pragmatic to just use local mode to get it functioning.




