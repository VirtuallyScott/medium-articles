FROM python:3.9

WORKDIR /docs

RUN pip install --no-cache-dir mkdocs mkdocs-material

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]