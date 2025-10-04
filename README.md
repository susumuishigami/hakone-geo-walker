# hakone-geo-walker

東海道箱根のミニ研究論文

## プロジェクト概要

このリポジトリは、Sphinx+MySTを使用した研究論文のテンプレートです。
6章構成の論文を作成し、HTMLおよびPDF形式で出力できます。

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

- Python 3.8以上
- LaTeX（PDF生成の場合、XeLaTeXが必要）

### インストール

```bash
pip install sphinx myst-parser sphinxcontrib-bibtex
```

## ビルド方法

### HTMLビルド

```bash
cd docs
sphinx-build -b html . _build/html
```

生成されたHTMLは `docs/_build/html/` に出力されます。

### PDFビルド

```bash
cd docs
sphinx-build -b latex . _build/latex
cd _build/latex
latexmk -pdf -xelatex hakone-geo-walker.tex
```

生成されたPDFは `docs/_build/latex/` に出力されます。

## GitHub Actions

このリポジトリでは、GitHub ActionsによるCI/CDが設定されています：
- プッシュ時にHTMLビルドを自動実行
- PDFビルドも試行（LaTeX環境により失敗する可能性があります）
