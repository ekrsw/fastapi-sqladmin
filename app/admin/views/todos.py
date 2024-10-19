from sqladmin import ModelView

from app.models import Todo


class TodoAdminView(ModelView, model=Todo):  # type: ignore
    # 表示名
    name_plural = "Todos"
    # 一覧に表示するカラム
    column_list = [
        Todo.id,
        Todo.title,
        Todo.description,
        Todo.completed_at,
    ]
    # 検索可能なカラム
    column_searchable_list = [Todo.title, Todo.description]
    # 一覧画面でソート可能なカラム
    column_sortable_list = [Todo.id, Todo.title, Todo.description, Todo.completed_at]
    # 新規作成、更新画面で入力可能なカラム
    form_columns = [Todo.title, Todo.description, Todo.completed_at]
