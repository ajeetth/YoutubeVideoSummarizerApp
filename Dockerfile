# 1. Use Python 3.12 as the base image
FROM python:3.12

# 2. Set the working directory inside the container
WORKDIR /app/src

# 3. Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application source code
COPY src/ .

# 5. Expose the default Streamlit port (8501)
EXPOSE 8501

# 6. Run the Streamlit application on container startup
CMD ["streamlit", "run", "summarizer_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
