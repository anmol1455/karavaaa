FROM python:3.10-slim


WORKDIR /karvaaa

COPY ./requirements.txt /karvaaa/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /karvaaa/

EXPOSE 8000

ENTRYPOINT [ "bash" , "entrypoint.sh"]