# hakone-geo-walker

## プロジェクト概要

東海道箱根を歴史とGISを用いて研究するミニ論文を執筆・公開するプロジェクトです。
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

- タグ付きリリース：公開・確認済みの安定版  
- `main` ブランチ：統合作業・検証中のドラフト  
- その他のブランチ：実験的または作業中（WIP）  
- 検証中のデータや文書には未確認の情報が含まれる場合があります  
- 内容は予告なく変更されることがあります

This repository is currently under active development and research.
Official public versions are provided on the [Releases page](https://github.com/susumuishigami/hakone-geo-walker/releases).

All branches, including `main`, are drafts or works in progress.

- Tagged releases: verified and published versions
- `main` branch: integrated draft under review
- other branches: experimental or work in progress (WIP)
- data and documents under review may include unverified information
- contents are subject to change without notice

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
├── code/                   # コードファイル
├── data/                   # データファイル
│   ├── public/            # 公開データ
│   └── private/           # 非公開データ（本体はGoogle Drive等に保存）
└── figs/                   # 図表ファイル
```

## セットアップ

### 必要な環境

- Python 3.14以上
- [uv](https://github.com/astral-sh/uv) 0.4.0以上（パッケージ管理）
- LaTeX（PDF生成の場合、XeLaTeXが必要）

### プロジェクトのセットアップ

uvで仮想環境作成と依存関係インストール
```console
% uv sync
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

## GitHub Actions

このリポジトリでは、GitHub ActionsによるCI/CDが設定されています：

- プッシュ時にHTMLビルドを自動実行
  - [Actions](https://github.com/susumuishigami/hakone-geo-walker/actions/workflows/build.yml) - `Build Documentation` - `build-html` - `Upload HTML artifacts`
- LaTeX/PDFのビルドについても対応予定

## ライセンス

この研究は、学びと発見を共有することを目的に **Creative Commons BY 4.0** ライセンスで公開しています。
ソースコードは **MIT License** で公開します。

- Texts, papers, and documents: [CC BY 4.0](./LICENSE-doc)
- Source code and scripts: [MIT License](./LICENSE-code)
