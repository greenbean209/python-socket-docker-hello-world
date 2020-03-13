# python-socket-docker-hello-world
A Hello World Python script using TCP sockets while contained in Docker

## Building the server image from docker file
```bash
docker build -t python-socket-docker-hello-world .
```

## Running the server image
```bash
docker run -p 2222 python-socket-docker-hello-world
```
