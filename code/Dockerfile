FROM python:3.10.0-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN python -m pip install pipenv

RUN mkdir database alembic

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile
COPY main.py .
COPY ./database/* /database/
COPY alembic.ini .
COPY ./alembic/* ./alembic/


EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
