FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
ENV AM_I_IN_A_DOCKER_CONTAINER Yes
#Updating on every build for security
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y python3 && apt-get install -y python3-pip

WORKDIR /code

#Adding the whole folder
ADD . /code

RUN ls

#Or specifically adding requirements txt only
#COPY requirements.txt .
#COPY app.py .

RUN pip3 install -r requirements.txt
RUN useradd -ms /bin/bash exec-user
#Switching user for security reasons
USER exec-user

CMD [ "python3", "app.py" ]