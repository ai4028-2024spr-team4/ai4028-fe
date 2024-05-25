FROM python:3.10

WORKDIR /app

COPY . .
RUN pip install poetry

RUN poetry install --no-root
EXPOSE 8501
ENTRYPOINT [ "poetry" ,"run", "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0" ]