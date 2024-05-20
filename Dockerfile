FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /hackerfake
WORKDIR /hackerfake
COPY requirements.txt /hackerfake/
RUN pip install -r requirements.txt
COPY . /hackerfake/
CMD python manage.py runserver 0.0.0.0:8080
