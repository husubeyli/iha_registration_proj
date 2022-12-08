FROM python:3.8.6
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
WORKDIR /code

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
gettext 

COPY . .


# CMD ["uwsgi", "--ini", "/code/uwsgi.ini"]

# CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "baykar_iha_main.wsgi" ]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]