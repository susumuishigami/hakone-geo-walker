# Configuration file for the Sphinx documentation builder.

import pathlib
import tomllib

# -- Project information -----------------------------------------------------
project = "東海道箱根のミニ研究論文"
copyright = "2025–2026, Susumu ISHIGAMI（本文 CC BY 4.0）"
author = "Susumu ISHIGAMI"

# バージョンの正は pyproject.toml。
_pyproject = pathlib.Path(__file__).resolve().parent.parent / "pyproject.toml"
release = tomllib.loads(_pyproject.read_text(encoding="utf-8"))["project"]["version"]

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinxcontrib.bibtex",
]

# MyST configuration
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
]

# BibTeX configuration
bibtex_bibfiles = ["refs.bib"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# XeLaTeXを使う場合は日本語設定を無効化してフォントで対応
# language = "ja"  # コメントアウト

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for LaTeX output ------------------------------------------------
latex_engine = "xelatex"
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    # fontawesome は使わない。TeX Live では texlive-fonts-extra にしか
    # 無く、展開後 1.7GB になる。アイコン数個のために釣り合わない。
    # 代わりに、既に入っているフォントの字形を title-icon に直接指定する。
    # 追加のパッケージは要らない。
    #   ⓘ (U+24D8) : Harano Aji
    #   \ding{...}  : pifont / ZapfDingbats（psnfss と zapfding。どちらも
    #                 PDF ビルドで既に導入している）
    # iconpackage=none を明示しないと、Sphinx が環境にある fontawesome を
    # 拾って出力が変わる。
    "sphinxsetup": "iconpackage=none,div.note_title-icon=ⓘ",
    # Sphinx の既定の fontpkg は欧文に FreeSerif / FreeSans / FreeMono を
    # 指定する。MacTeX には同梱されるが Ubuntu では別パッケージのため、
    # 上書きするだけでは「読み込めるが使わないフォント」への依存が残る。
    # 既定を差し替えて、実際に使うフォントだけを参照する。
    "fontpkg": r"""
\setmainfont[BoldFont=texgyretermes-bold.otf,ItalicFont=texgyretermes-italic.otf]{texgyretermes-regular.otf}
\setsansfont[BoldFont=texgyreheros-bold.otf]{texgyreheros-regular.otf}
\setmonofont[BoldFont=texgyrecursor-bold.otf]{texgyrecursor-regular.otf}
""",
    "preamble": r"""
\usepackage{xeCJK}
\setCJKmainfont[BoldFont=HaranoAjiMincho-Bold.otf]{HaranoAjiMincho-Regular.otf}
\setCJKsansfont[BoldFont=HaranoAjiGothic-Bold.otf]{HaranoAjiGothic-Regular.otf}
\setCJKmonofont{HaranoAjiGothic-Regular.otf}
% 和文で全角として組む記号を CJK 側に回す。欧文フォントには字形が無い。
%   2460-24FF 囲み英数字（①、注釈アイコンの ⓘ）
%   2500-257F 罫線素片（和文中でダーシとして使われる）
%   25A0-25FF 幾何学模様（■ ● ▲）
%   2600-26FF その他の記号（★ ⚠）
\xeCJKDeclareCharClass{CJK}{"2460->"24FF, "2500->"257F, "25A0->"25FF, "2600->"26FF}
\xeCJKsetup{CJKmath=true}
""",
    "fncychap": "",
    "babel": "",
    "polyglossia": "",
    # 言語選択を無効化
    "passoptionstopackages": r"\PassOptionsToPackage{english}{babel}",
    # XeLaTeXで日本語を使う場合、jsclassesを無効化
    "extraclassoptions": "openany,oneside",
}

# XeLaTeX使用時は日本語用のクラスファイル使用を無効化
latex_use_latex_multicolumn = True
latex_use_xindy = False

# 言語設定を完全に無効化
latex_elements["babel"] = ""
latex_elements["polyglossia"] = ""

latex_documents = [
    (
        "index",
        "hakone-geo-walker.tex",
        "東海道箱根のミニ研究論文",
        "Susumu ISHIGAMI",
        "manual",
    ),
]
