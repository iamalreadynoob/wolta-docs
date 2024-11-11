# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Wolta'
copyright = '2024, Sadık Efe Kartav'
author = 'iamalreadynoob'

release = '0.4'
version = '0.3.5'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_raw_enabled = True

# -- Options for EPUB output
epub_show_urls = 'footnote'
