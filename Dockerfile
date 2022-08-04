FROM python

#install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#add source code
WORKDIR ./app
ADD ./src .

#Run the app
CMD ["python", "hello-world.py"]