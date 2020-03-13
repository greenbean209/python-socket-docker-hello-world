FROM python:3
ADD hello_world_server.py /
EXPOSE 2222:2222
CMD [ "python", "./hello_world_server.py" ]