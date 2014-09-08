FROM ubuntu:trusty
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install python-dev
RUN apt-get -y install python-setuptools
RUN easy_install -U pip

RUN apt-get -y install libpq-dev

ADD . /src/{{cookiecutter.app_name}}
WORKDIR /src/{{cookiecutter.app_name}}

RUN pip install -r /src/{{cookiecutter.app_name}}/requirements.txt
RUN python setup.py install

CMD ["gunicorn", "wsgi:app"]
