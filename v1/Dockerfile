# Use the official image as a parent image.
FROM python:3

# Set the working directory.
WORKDIR /app

# Copy the file from your host to your current location.
COPY . /app

# Run the command inside your image filesystem.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8090

# Run the specified command within the container.
CMD ["python", "AccesoLocal.py"]

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .