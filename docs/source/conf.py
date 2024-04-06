# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TestLocale'
copyright = '2024, Cyrogon'
author = 'Cyrogon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['../templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
locale_dirs = ['../locales']

html_context = {
  'current_version' : "latest",
  'versions' : [],
  'current_language': 'en',
  'languages': [["en", "en"], ["zh_cn", "zh_cn"]]
}