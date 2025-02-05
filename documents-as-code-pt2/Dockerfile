FROM python:3.9-slim

# Create a non-root user
RUN useradd -m docsuser
WORKDIR /home/docsuser/docs

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies with pinned versions
RUN pip install --no-cache-dir \
    mkdocs==1.6.1 \
    mkdocs-material==9.6.2 \
    mkdocs-material-extensions==1.3.1 \
    pymdown-extensions==10.14.3 \
    mkdocs-toc-plugin

# Copy docs and change ownership
COPY . .
RUN chown -R docsuser:docsuser /home/docsuser

USER docsuser

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
