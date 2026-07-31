# AI_Test

ローカルAI開発環境のテストプロジェクトです。

## 開発環境

- Windows 11
- VS Code
- Python
- Git / GitHub
- Ollama
- Gemma 4 31B
- Cline

## 作成したアプリ

### Python Calculator

`calculator.py`

機能:
- 加算
- 減算
- 乗算
- 除算
- エラー処理

### Todo App

`todo_app/index.html`

機能:
- タスク追加
- 完了管理
- 削除
- ブラウザ保存

## 開発ルールと運用方針

### ブランチ運用ルール
- **mainブランチへの直接変更禁止**: すべての変更は feature ブランチで実施してください。
- **事前確認**: 変更前に必ず `git diff` を確認し、意図しない変更が含まれていないか把握してください。
- **レビュープロセス**: Pull Request を作成し、レビューを経てから main ブランチへ反映してください。
- **CIの必須化**: GitHub Actions の CI（pytest）が成功したことがマージの条件となります。

## 開発・テスト手順

### 1. 環境構築
```bash
pip install .
```
（または `pip install pytest pytest-cov`）

### 2. テストの実行
```bash
pytest
```

### 3. カバレッジの確認
```bash
pytest --cov=src
```

### 4. Todoアプリの起動
`apps/todo_app/index.html` をブラウザで開いてください。

## 目的

ローカルLLMを利用したAI開発環境の構築・検証。

### AIエージェント向け最適化
AIエージェントによる効率的な開発を支援するため、以下の設定を導入しています：
- **`.clinerules`**: エージェント向けのコード編集方針やエラー報告ルールを定義。
- **近代的なパッケージ管理**: `pyproject.toml` を導入し、CI/CD（GitHub Actions）およびローカル環境での構築を簡略化。
- **リポジトリ管理の最適化**: `.github/CODEOWNERS` による所有権の明確化と、厳格なブランチ運用ルールの策定。

今後:
- AIエージェント開発
- Webアプリ作成
- Python開発
- GitHub管理

を進める。
