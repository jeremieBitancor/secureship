FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pipi \ 
    && pip install --no-cache-dir -r requirements.txt

RUN addgroup --system secureship \ 
    && adduser --system --ingroup secureship secureship

COPY --chown=secureship:secureship ./app ./app

USER secureship

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]