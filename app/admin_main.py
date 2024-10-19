import logging

from fastapi import FastAPI
from sqladmin import Admin

from app.admin.core.auth import AdminAuth
from app.admin.views.tags import TagAdminView
from app.admin.views.todos import TodoAdminView
from app.admin.views.todos_tags import TodoTagAdminView
from app.admin.views.user_csv_import import UserCsvImportAdminView
from app.admin.views.users import UserAdminView
from app.database import async_session_factory
from app.settings import settings

""" 管理画面用のmain処理 """

# loggingセットアップ
logger = logging.getLogger(__name__)


# 管理画面用のFastAPIアプリケーションの作成
app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    debug=settings.DEBUG or False,
)

# 管理画面用
admin_manager = Admin(
    app,
    title="管理画面",
    session_maker=async_session_factory,  # SQLAlchemyのセッションを作成する関数
    templates_dir="app/admin/templates",  # Jinja2テンプレートのディレクトリ
    # 認証用のクラスを指定
    authentication_backend=AdminAuth(secret_key=settings.SECRET_KEY),
)


# 管理画面のviewを追加する
admin_manager.add_view(UserAdminView)
admin_manager.add_view(TodoAdminView)
admin_manager.add_view(TagAdminView)
admin_manager.add_view(TodoTagAdminView)
admin_manager.add_view(UserCsvImportAdminView)
