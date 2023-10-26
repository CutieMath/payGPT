FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install langchain Flask Flask-CORS requests beautifulsoup4 openai unstructured chromadb tiktoken
EXPOSE 5000
CMD ["python", "app.py"]