# SQLAdmin を使って管理画面を作成するサンプル(with FastAPI)

アプリ側と管理画面側のコードをモノレポとして管理しつつ、アプリと管理画面は別々のプロセスで動作するようにしたサンプルです。

詳細は以下の記事を参照してください。

## 初期セットアップ

### 必要な環境

- Docker
- Docker Compose
- make

### セットアップ手順

1. 環境変数の設定

```bash
# .envファイルを作成し、必要な環境変数を設定
cp .env.example .env
# .envファイルを編集して必要な値を設定
```

2. アプリケーションの起動とテーブル作成

```bash
# Dockerコンテナをビルドして起動
docker-compose up -d

# テーブルを作成（コンテナ内で実行）
docker-compose exec app python tools.py create_all_tables
```

3. 動作確認

- 管理画面: http://localhost:18081/admin
- API: http://localhost:18080

## アプリの起動方法

### Docker を使用した起動（本番環境に近い構成）

以下コマンドでアプリを起動し、`http://localhost:18081/admin` にアクセスすると管理画面が表示されます。

```bash
docker compose up -d
```

### 開発用コマンド

プロジェクトには以下の開発用コマンドが用意されています：

#### データベース関連

```bash
# データベースの完全リセット
make reset_db
```

**使用シーン**:

- データベースを完全にクリーンな状態に戻したい場合
- テストデータをリセットしたい場合
- データベースの不整合が発生した場合

**動作**:

- Docker Compose を停止
- データベースのボリュームを削除
- 次回起動時に新しいデータベースが作成される

```bash
# データベーステーブルの作成（非推奨: 代わりにdocker compose execを使用）
make create_all_tables
```

**使用シーン**:

- プロジェクトの初期セットアップ時
- データベースをリセットした後
- モデルの定義を変更した後にテーブルを再作成する場合

**動作**:

- SQLAlchemy のモデル定義に基づいてテーブルを作成
- 既存のテーブルがある場合は影響なし

**推奨される実行方法**:

```bash
docker compose exec app python tools.py create_all_tables
```

#### ローカル開発サーバー

```bash
# ローカル開発用サーバーの起動
make start_uvicorn_local
```

**使用シーン**:

- ローカルでの開発作業時
- デバッグが必要な場合
- コードの変更を即座に確認したい場合

**動作**:

- ホットリロード機能付きで uvicorn サーバーを起動
- データベースは Docker コンテナ（ポート 54321）に接続
- コードの変更を検知して自動的に再起動

### 開発時の一般的なワークフロー

1. データベースの準備

```bash
# 全てのコンテナを起動
docker compose up -d

# 必要に応じてDBをリセット
make reset_db

# テーブルを作成（コンテナ内で実行）
docker compose exec app python tools.py create_all_tables
```

2. 開発サーバーの起動

```bash
# ホットリロード付きで開発サーバーを起動
make start_uvicorn_local
```

これにより、以下の URL でアプリケーションにアクセスできます：

- 管理画面: http://localhost:8000/admin （ローカル開発サーバー）
- API: http://localhost:8000 （ローカル開発サーバー）
