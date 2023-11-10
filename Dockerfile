FROM python:3.11
WORKDIR /site
COPY . /site
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt
VOLUME /home/ubuntu/site:/site
EXPOSE 8000
CMD ["cd", "my_store", "\\", "&&python","manage.py", "runserver"]
