# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY random_int.py .

# install dependencies
RUN pip install numpy tensorflow

# command to run on container start
CMD [ "python", "random_int.py" ]