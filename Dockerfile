# Use a base image with PySpark and Jupyter pre-installed
FROM jupyter/pyspark-notebook:latest

# Set the working directory inside the container
WORKDIR /home/divij/work

# Copy your local requirements.txt into the container (if you have one)
# This allows you to install additional Python packages for your project
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Expose Jupyter port (already exposed by base image, but good practice)
EXPOSE 8888

# Expose Spark UI port
EXPOSE 4040

# Default command when the container starts (Jupyter Notebook)
CMD ["start-notebook.sh", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]