FROM debian:12

ENV HOME /home/app

RUN export LC_ALL=es_ES.UTF-8
ENV PATH $HOME/.local/bin:$PATH

ADD requirements.txt ${HOME}/requirements.txt

RUN apt update
RUN apt install python3 python3-pip python3-dotenv -y

WORKDIR ${HOME}

RUN pip3 install --break-system-packages -r requirements.txt
