FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

COPY 01-agentic-rag-and-02-vector-search/pyproject.toml ./
COPY 01-agentic-rag-and-02-vector-search/uv.lock ./
COPY 01-agentic-rag-and-02-vector-search/.python-version ./

RUN uv sync --locked

COPY 05-monitoring/ ./

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]