FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY project/ project/

RUN apt-get update & apt-get install -y g++

RUN cd project/cpp_lib && make

CMD ["python", "project/manage.py", "runserver", "0.0.0.0:8000"]
