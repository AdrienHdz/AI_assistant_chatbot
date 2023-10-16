ARG BASE_IMAGE=python:3.10.0-slim
FROM ${BASE_IMAGE} as pythoninstalled

WORKDIR /app

RUN groupadd app \
    && useradd -r -s /bin/false -N -g app app

RUN chown app:app /app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt upgrade -y && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements/requirements.txt /tmp/requirements.txt

ENV PIP_CACHE_DIR=/var/cache/pip XDG_CACHE_HOME=/var/cache/
RUN --mount=type=cache,target=/var/cache/pip python -m venv .venv \
    && pip install --upgrade pip \
    && PIP_CACHE_DIR=/var/cache/pip XDG_CACHE_HOME=/var/cache pip --cache-dir /var/cache/pip install -r /tmp/requirements.txt

COPY ./ /app/

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]