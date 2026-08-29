# hakone-geo-walker

## プロジェクト概要

東海道箱根を歴史とGISを用いて研究し、ミニ論文を執筆・公開するプロジェクトです。
Sphinx+MySTを使用して研究論文をビルドし、HTMLおよびPDF形式で出力します。

## 研究概要

- テーマ:
  - 旧東海道・箱根越えに見る「歩行文化と地理的要素」の関係
- 目的:
  - 歴史的街道を「単なる交通路」ではなく、人々の営み・文化・知の移動空間として再解釈
- 手法:
  - GISによる地形・距離・傾斜などの可視化  
  - 江戸期文献（『東海道中膝栗毛』など）の記述分析  
  - 現地踏査による空間的・文化的比較

## プロフィール

Susumu ISHIGAMI

ITエンジニアとして培ったデータ分析とシステム構築の経験をもとに、歴史的街道を歩き、GIS、文献、現地調査を通して人が歩く空間にどのような文化が生まれるかを探る、ひとりの研究者。

Exploring Japan's historical highways through culture, geography, and GIS.

Geo walker / 地理情報行路者

## リポジトリポリシー / Repository Policy

このリポジトリは現在、研究および開発の進行中段階にあります。
正式な公開版は、[リリースページ](https://github.com/susumuishigami/hakone-geo-walker/releases) で公開されます。

`main` を含むすべてのブランチは作業中（WIP）です。

- タグ付きリリース：その時点の内容を固定した公開スナップショット（確定度はリリースノートに記載）  
- `main` ブランチ：統合作業・検証中のドラフト  
- その他のブランチ：実験的または作業中（WIP）  
- 検証中のデータや文書には未確認の情報が含まれる場合があります  
- 内容は予告なく変更されることがあります

採番規約とリリースの扱いは [Wiki](https://github.com/susumuishigami/hakone-geo-walker/wiki) を参照してください。

This repository is currently under active development and research.
Official public versions are provided on the [Releases page](https://github.com/susumuishigami/hakone-geo-walker/releases).

All branches, including `main`, are drafts or works in progress.

- Tagged releases: published snapshots of the repository at that point
  (see the release notes for what is settled and what is not)
- `main` branch: integrated draft under review
- Other branches: experimental or works in progress (WIP)
- Data and documents under review may include unverified information
- Contents are subject to change without notice

See the [Wiki](https://github.com/susumuishigami/hakone-geo-walker/wiki) for the versioning scheme and how releases are handled.

## ディレクトリ構成

```
hakone-geo-walker/
├── README.md               # このファイル
├── docs/                   # Sphinxドキュメントソース
│   ├── conf.py            # Sphinx設定ファイル
│   ├── index.md           # 目次ページ
│   ├── 01-intro.md        # 第1章：はじめに
│   ├──     :              # 以降本文
│   └── refs.bib           # 参考文献データベース
├── analysis/               # データ分析・GIS・図版生成コード
├── data/                   # データファイル
│   ├── public/            # 公開データ
│   └── private/           # 非公開データ（本体はGoogle Drive等に保存）
└── figs/                   # 図表ファイル
```

## セットアップ

### 必要な環境

- Python 3.14以上
- [uv](https://github.com/astral-sh/uv) 0.4.0以上（パッケージ管理）
- LaTeX（PDF生成の場合のみ。XeLaTeX と latexmk が必要）

PDFをビルドする場合は、あわせてLaTeX環境を用意してください。日本語の組版には
Harano Aji、欧文にはTeX Gyreを使います。いずれもTeX Liveに同梱されています。

macOS:

```console
% brew install --cask mactex
```

Ubuntu / Debian:

```console
% sudo apt-get install texlive-xetex texlive-lang-japanese texlive-latex-extra fonts-texgyre latexmk
```

### プロジェクトのセットアップ

uvで仮想環境作成と依存関係インストール
```console
% uv sync
```

`uv sync` は論文（Sphinx）のビルドと開発ツールに必要な依存だけを入れます。
`analysis/` のGIS解析を動かす場合は `analysis` グループも指定してください。

```console
% uv sync --group analysis
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

## ライセンス / License

この研究は「オープンサイエンス」の理念に基づき、学びと発見を共有することを目的に公開しています。

- Texts, papers, and documents: [CC BY 4.0](./LICENSE-doc)
- Source code and scripts: [MIT License](./LICENSE-code)

