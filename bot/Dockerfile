FROM python:3.8

COPY ./requirements.txt ./

RUN apt-get update
RUN python -m pip install -U pip
RUN pip install -r ./requirements.txt

COPY *.py ./

ENTRYPOINT [ "python", "bot.py"]