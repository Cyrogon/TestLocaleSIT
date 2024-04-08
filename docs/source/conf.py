# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import yaml

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

html_static_path = ['static']
html_theme = 'sphinx_rtd_theme'
locale_dirs = ['../locales']
html_scaled_image_link = False

langs = ["en"]
langs += os.listdir("../locales")

# get the environment variable build_all_docs and pages_root
build_all_docs = os.environ.get("build_all_docs", str(True))
pages_root = os.environ.get("pages_root", "https://cyrogon.github.io/TestLocaleSIT")

current_language = os.environ.get("current_language")
current_version = os.environ.get("current_version")

html_context = {
  'current_language' : current_language,
  'languages' : [],
  'current_version' : current_version,
  'versions' : [],
}

if (current_version == 'latest'):
  for lang in langs:
    html_context['languages'].append([lang, "{}/{}".format(pages_root, lang)])

html_context['versions'].append(['latest', "{}/{}".format(pages_root, current_language)])


# and loop over all other versions from our yaml file
# to set versions and languages
with open("../versions.yaml", "r") as yaml_file:
  docs = yaml.safe_load(yaml_file)

if (current_version != 'latest'):
  for language in docs[current_version].get('languages', []):
    html_context['languages'].append([language, "{}/{}/{}".format(pages_root, current_version, language)])



for version, details in docs.items():
  html_context['versions'].append([version, "{}/{}/{}".format(pages_root, version, current_language)])
