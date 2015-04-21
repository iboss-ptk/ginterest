FROM django:1.8-python3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000