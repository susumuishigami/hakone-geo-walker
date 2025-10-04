# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = '東海道箱根のミニ研究論文'
copyright = '2024'
author = 'Author'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinxcontrib.bibtex',
]

# MyST configuration
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
]

# BibTeX configuration
bibtex_bibfiles = ['refs.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{xeCJK}
''',
}

latex_documents = [
    ('index', 'hakone-geo-walker.tex', '東海道箱根のミニ研究論文',
     'Author', 'manual'),
]
