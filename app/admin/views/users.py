from typing import Any

from sqladmin import ModelView
from sqlalchemy import ClauseElement, Select

from app.models import User


class UserAdminView(ModelView, model=User):  # type: ignore
    name_plural = "Users"
    column_list = "__all__"
    column_searchable_list = [User.id, User.email, User.full_name, User.scopes]
    form_columns = [
        User.email,
        User.full_name,
        User.hashed_password,
        User.scopes,
        User.deleted_at,
    ]

    async def _run_query(self, stmt: ClauseElement) -> Any:
        """論理削除されたレコードも含めて出力するようにクエリを実行する

        Usersテーブルは削除時に論理削除ができるようにdeleted_atカラムを持っているため、管理画面では論理削除されたレコードも表示できるようにする
        論理削除を使用しない場合は_run_queryメソッドをオーバーライドする必要はないため、このメソッドを削除しても問題ない

        """
        if isinstance(stmt, Select):
            # include_deleted=Trueを指定することで論理削除されたレコードも含めて出力する
            stmt = stmt.execution_options(include_deleted=True)
        return await super()._run_query(stmt)
