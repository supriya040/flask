FROM 192.168.0.10:5000/python
RUN pip install flask
WORKDIR /src
COPY . .
EXPOSE 4010
CMD python server.py
