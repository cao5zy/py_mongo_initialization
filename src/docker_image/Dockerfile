FROM python:3.6.5
RUN mkdir /app
COPY ./*.py /app/
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ['bash']