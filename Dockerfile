FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

COPY pyproject.toml uv.lock /app/

ENV UV_SYSTEM_PYTHON=true \
    UV_COMPILE_BYTECODE=1 \
    UV_CACHE_DIR=/root/.cache/uv \
    UV_LINK_MODE=copy

RUN --mount=from=ghcr.io/astral-sh/uv:0.4.19,source=/uv,target=/bin/uv \
    --mount=type=cache,target=${UV_CACHE_DIR} \
    uv export --frozen --no-dev --format requirements-txt > requirements.txt \
    && uv pip install -r requirements.txt

# 基本となるイメージを指定。Pythonがプリインストールされた公式イメージを使用
FROM python:3.12-slim-bookworm

# 必要なパッケージのインストール。無視できるエラーに対してaptを設定
# RUN apt-get update \
#     && apt-get install -y unzip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /app

# builderステージでインストールしたパッケージをコピー
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# 現在のディレクトリにあるファイルをコピー
COPY . /app

