.PHONY: reset_db
reset_db:
	@echo "docker composeを停止します"
	@docker compose down
	@echo "DBのデータを削除します(Volumeの削除)"
	@sudo rm -rf ./docker/db_data/

.PHONY: create_all_tables
create_all_tables:
	@echo "テーブルを作成します"
	@python tools.py create_all_tables

.PHONY: start_uvicorn_local
start_uvicorn_local:
	@echo "uvicornを起動します"
	@DB_HOST=localhost DB_PORT=54321 uvicorn app.admin_main:app --reload