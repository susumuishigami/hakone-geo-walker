# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = "東海道箱根のミニ研究論文"
copyright = "2024"
author = "Author"
release = "0.1"

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
    "preamble": r"""
\usepackage{xeCJK}
\usepackage{fontspec}
% macOSの標準的な日本語フォントを使用
\setCJKmainfont[BoldFont=Hiragino Mincho ProN]{Hiragino Mincho ProN}
\setCJKsansfont[BoldFont=Hiragino Kaku Gothic ProN]{Hiragino Kaku Gothic ProN}
\setCJKmonofont{Menlo}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Menlo}
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
    ("index", "hakone-geo-walker.tex", "東海道箱根のミニ研究論文", "Author", "manual"),
]
