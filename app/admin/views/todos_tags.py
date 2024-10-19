from sqladmin import ModelView

from app.models.todos_tags import TodoTag


class TodoTagAdminView(ModelView, model=TodoTag):  # type: ignore
    # 表示名
    name_plural = "TodosTags"
    # 一覧に表示するカラム
    column_list = [
        TodoTag.id,
        TodoTag.todo_id,
        TodoTag.tag_id,
    ]
    form_columns = [TodoTag.todo_id, TodoTag.tag_id]
    # PKやFKを含むカラムをフォームに含めるかどうか
    form_include_pk = True
