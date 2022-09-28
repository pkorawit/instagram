
# start by pulling the python image
FROM tensorflow/tensorflow

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY . .

# install the dependencies and packages in the requirements file
RUN pip install --upgrade pip
#RUN pip install tensorflow flask pillow
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]