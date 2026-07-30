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

## 開発・テスト手順

### 1. 環境構築
```bash
pip install -r requirements.txt
```

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

今後:
- AIエージェント開発
- Webアプリ作成
- Python開発
- GitHub管理

を進める。