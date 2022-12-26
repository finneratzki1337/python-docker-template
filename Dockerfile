FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
ENV AM_I_IN_A_DOCKER_CONTAINER Yes
#Updating on every build for security
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y python3 && apt-get install -y python3-pip

WORKDIR /code

#Adding the whole folder


#Or specifically adding requirements txt only
COPY requirements.txt .
#COPY app.py .

RUN pip3 install -r requirements.txt
#Add new user for security
RUN useradd -ms /bin/bash exec-user
ADD . /code
#If needed writeable workdir for user (e.g. files or something)
#RUN chown exec-user files

#Switching user for security reasons
USER exec-user

#Having all tests for testfolder being run
RUN pytest

CMD [ "python3", "src/app.py" ]