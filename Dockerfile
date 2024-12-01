FROM python
WORKDIR /usr/src/django
COPY requirements.txt /usr/src/django/
RUN pip install -r requirements.txt
COPY yozhkindjangoproject /usr/src/django/yozhkindjangoproject
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]