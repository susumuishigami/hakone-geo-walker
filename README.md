# hakone-geo-walker

東海道箱根のミニ研究論文

## プロジェクト概要

東海道箱根のミニ研究論文を執筆・公開するプロジェクトです。
Sphinx+MySTを使用して研究論文をビルドし、HTMLおよびPDF形式で出力します。

## ディレクトリ構成

```
hakone-geo-walker/
├── README.md           # このファイル
├── docs/               # Sphinxドキュメントソース
│   ├── conf.py         # Sphinx設定ファイル
│   ├── index.md        # 目次ページ
│   ├── 01-intro.md     # 第1章：はじめに
│   ├── 02-background.md # 第2章：背景
│   ├── 03-methodology.md # 第3章：方法論
│   ├── 04-results.md   # 第4章：結果
│   ├── 05-discussion.md # 第5章：考察
│   ├── 06-conclusion.md # 第6章：結論
│   └── refs.bib        # 参考文献データベース
├── code/               # コードファイル
├── data/               # データファイル
└── figs/               # 図表ファイル
```

## セットアップ

### 必要な環境

- Python 3.14以上（3.14.0rc3）
- [uv](https://github.com/astral-sh/uv) 0.4.0以上（パッケージ管理）
- LaTeX（PDF生成の場合、XeLaTeXが必要）

### プロジェクトのセットアップ

uvで仮想環境作成と依存関係インストール
```console
uv sync
```

#### 開発用依存関係も含める場合
```console
uv sync --extra dev
```

## ビルド方法

### HTMLビルド

```console
% make html
```

生成されたHTMLは `docs/_build/html/` に出力されます。

### PDFビルド

```console
% make latexpdf
```

生成されたPDFは `docs/_build/latex/` に出力されます。

## 開発

### 依存関係の管理

新しいパッケージを追加
```console
% uv add package-name
```

開発用パッケージを追加
```console
% uv add --dev package-name
```

依存関係を更新
```console
% uv sync
```

### 開発補助コマンド

HTMLドキュメントをビルド
```console
% make html
```

PDFドキュメントをビルド
```console
% make latexpdf
```

ビルドファイルをクリーン
```console
% make clean
```

コードフォーマット（ruff）
```console
% uv run ruff format
```

コードリント（ruff）
```console
% uv run ruff check
```

型チェック（mypy）
```console
% uv run mypy .
```

テスト実行
```console
% uv run pytest
```

## GitHub Actions

このリポジトリでは、GitHub ActionsによるCI/CDが設定されています：
- プッシュ時にHTMLビルドを自動実行
- PDFビルドも試行（LaTeX環境により失敗する可能性があります）
