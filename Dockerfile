FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3" ,"src/main.py"]

#docker run -p 3000:3000 -v $(pwd)/U:/app/U -v $(pwd)/P:/app/P -v $(pwd)/C:/app/C -v $(pwd)/H:/app/H -d flask