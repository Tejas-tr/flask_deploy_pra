# file name should be exactly same as 'Dockerfile'

#docker image name from dockerhub to create docker container in local maching
FROM python:3.8-slim-buster

# create a directory in docker container which is just created by above image
WORKDIR /flask-loan-pred-app

# copy requirement to above create folder in container /flask-loan-pred-app
COPY requirement.txt /flask-loan-pred-app/

# install all the packages from requirement.txt. As image conatains only default packages and python
# packages from requirement.txt will be installed from internet
RUN pip3 install -r requirement.txt

# copy everything / every file from this location to docker containter
COPY . /flask-loan-pred-app

# execute above code in container
# syntax : python -m flask --app hello.py run --host =0.0.0.0 --port = 8000
# here host --> local ip address on whiich needs to run (address of house or web app)
# here port --> port to used (door at which we need to enter or where need to access)
# default --> host (127.0.0.1) and port (5000)
CMD {"python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"}

# next to build image from this dockerfile using below command in cmd
# docker build -t <name> .
# here dot tells Docker to use the Dockerfile in the current directory to build the image.

