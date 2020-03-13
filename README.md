# python-socket-docker-hello-world
A Hello World Python script using TCP sockets while contained in Docker

## About
This is project is a simple example of how to containerize a python script and communicate with it using sockets. The hello world server script creates a socket and waits for connections. The server can be built into a docker image using the included dockerfile. When the container is ran using the below command, port 2222 is exposed. The hello world client script (which can be ran on a remote computer) makes a connection to the server and recieves the hello world message.

## Building the server image from docker file
```bash
docker build -t python-socket-docker-hello-world .
```

## Running the server image
```bash
docker run -p 2222:2222 python-socket-docker-hello-world
```
