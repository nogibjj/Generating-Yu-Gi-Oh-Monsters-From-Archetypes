# FROM python:3.9-slim

# RUN mkdir -p /app
# COPY . /app/
# WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# # RUN git clone https://github.com/streamlit/streamlit-example.git .

# RUN pip3 install -r requirements.txt

# EXPOSE 8501

# # HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


# Use an official Python runtime as a parent image
FROM python:3.9.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 8502 available to the world outside this container
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]