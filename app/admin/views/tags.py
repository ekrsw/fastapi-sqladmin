from sqladmin import ModelView

from app.models import Tag


class TagAdminView(ModelView, model=Tag):  # type: ignore
    name_plural = "Tags"
    column_list = "__all__"
    column_searchable_list = [Tag.name]
    form_columns = [Tag.name]
