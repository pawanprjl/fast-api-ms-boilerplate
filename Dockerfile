# pull official base image
FROM python:3.9-slim

# set working directory
WORKDIR /code

# copy and install requirements
COPY /requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

# copy app in code folder
COPY /app /code/app
COPY /main.py /code/

EXPOSE 80

# run python api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]