FROM python:3.8

COPY ./requirements.txt .

COPY ./StirlitzJokeOnRuGPT2_Medium/* .

RUN apt-get update
RUN python -m pip install -U pip
RUN pip install -r ./requirements.txt

COPY *.py .

ENTRYPOINT [ "python", "server.py"] 