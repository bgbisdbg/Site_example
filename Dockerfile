FROM python:3.11
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt
WORKDIR /site
COPY . /site
VOLUME /home/ubuntu/site:/site
EXPOSE 8000
CMD ["cd","my_store"]
CMD ["python","manage.py", "runserver"]
