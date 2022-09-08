FROM python:3.10.0-slim

RUN python -m pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
COPY main.py .
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
