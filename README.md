# Python Template

`uv` ベースの Python アプリケーション/スクリプト雛形。

## 構成

- `src/main.py` — エントリポイント（必要に応じてスクリプトを追加）
- `ruff` — format / lint
- `pyright` — 型チェック（standard モード）
- `pytest` — テスト（`src/` を pythonpath に追加済み）
- `pre-commit` — コミット時に上記を自動実行
- GitHub Actions — `main` への push / PR で lint + test を実行
- `.vscode/` — ruff を保存時フォーマッタに設定、フォルダオープン時に `uv sync` を自動実行

配布パッケージではなく、`uv run python src/main.py` で直接実行する想定です（`[tool.uv] package = false`）。

## セットアップ

```bash
uv sync
uv tool install pre-commit
pre-commit install
```

## 実行

```bash
uv run python src/main.py
```

## 開発

```bash
uv run pytest
uv run ruff check src/ tests/
uv run ruff format src/ tests/
uv run pyright
```

## VSCode

`python.defaultInterpreterPath` に `.venv/bin/python` を指定済み。Pylance / pyright がワークスペース直下の `.venv` を自動で参照します。

### `uv sync` の自動実行

`.vscode/tasks.json` でフォルダオープン時に `uv sync` を自動実行する設定が入っています。clone 直後でも VSCode で開くだけで `.venv` が作成されます。

初回は自動タスクが許可されていないため、以下のいずれかで許可してください。

- Command Palette → `Tasks: Manage Automatic Tasks` → `Allow Automatic Tasks`
- もしくは user settings に `"task.allowAutomaticTasks": "on"` を追加

許可後、フォルダを開き直すと `uv sync` が自動実行されます。
