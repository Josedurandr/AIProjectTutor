FROM python:3.11-slim

RUN mkdir -p /dependencies

COPY requirements.txt /dependencies/requirements.txt
COPY /tutorFrontend/package.json /dependencies/package.json

WORKDIR /dependencies

RUN pip install -r requirements.txt
RUN npm install

WORKDIR /AIProjectTutor

COPY . /AIProjectTutor

EXPOSE 3001
EXPOSE 3002
  
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001"]
