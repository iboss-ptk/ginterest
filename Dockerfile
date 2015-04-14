FROM django:python3-onbuild

ADD . /usr/src/app
WORKDIR /usr/src/app