FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY config/requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
COPY . /code/