import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.settings import settings

""" app用のmain処理 """


# loggingセットアップ
logger = logging.getLogger(__name__)


# FastAPIアプリケーションの作成
app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    debug=settings.DEBUG or False,
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
    allow_origin_regex=r"^https?:\/\/([\w\-\_]{1,}\.|)example\.com",
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["info"])
def get_info() -> dict[str, str]:
    return {"title": settings.TITLE, "version": settings.VERSION}
