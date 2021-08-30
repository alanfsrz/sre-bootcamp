FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000

# Working directory
WORKDIR /app


# Enviroment variables
ENV FLASK_APP=api.py
ENV FLASK_DEBUG=1

# Port activation
EXPOSE 8000

# Requirements installation
COPY . /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Application run
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
