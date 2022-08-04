FROM python

#install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#add Source code
WORKDIR /app
ADD . .

#Environment Variables

#RUN the app
CMD ["python", "manage.py", "runserver"]