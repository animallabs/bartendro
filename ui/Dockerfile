FROM ubuntu

RUN apt-get update
RUN apt-get -y install nginx
RUN apt-get -y install uwsgi python-werkzeug python-jinja2 python-setuptools python-wtforms python-serial python-smbus python-sqlite python-sqlalchemy memcached python-memcache python-flask sqlite3
RUN apt-get -y install uwsgi-plugin-python
RUN apt-get -y install python-pip
RUN apt-get -y install git


RUN git clone https://github.com/animallabs/bartendro.git
RUN pip install -r bartendro/ui/requirements.txt





