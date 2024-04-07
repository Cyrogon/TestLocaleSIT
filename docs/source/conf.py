# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import yaml
import os

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

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
locale_dirs = ['../locales']

html_context = {
  'current_version' : "latest",
  'versions' : [],
  'current_language': 'en',
  'languages': [["en", "en"], ["zh_CN", "zh_CN"], ["de", "de"], ["fr", "fr"], ["es", "es"]]
}

# get the environment variable build_all_docs and pages_root
build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")

# if not there, we dont call this
if build_all_docs is not None:
  # we get the current language and version
  current_language = os.environ.get("current_language")
  current_version = os.environ.get("current_version")

  # we set the html_context wit current language and version 
  # and empty languages and versions for now
  html_context = {
    'current_language' : current_language,
    'languages' : [],
    'current_version' : current_version,
    'versions' : [],
  }

  # and we append all versions and langauges accordingly 
  # we treat the main branch as latest 
  if (current_version == 'latest'):
    html_context['languages'].append(['en', pages_root+'/en'])
    html_context['languages'].append(['zh_CN', pages_root+'/zh_CN'])
    html_context['languages'].append(['de', pages_root+'/de'])
    html_context['languages'].append(['fr', pages_root+'/fr'])
    html_context['languages'].append(['es', pages_root+'/es'])

  if (current_language == 'en'):
    html_context['versions'].append(['latest', pages_root+'/en'])
  if (current_language == 'zh_CN'):
    html_context['versions'].append(['latest', pages_root+'/zh_CN'])
  if (current_language == 'de'):
    html_context['versions'].append(['latest', pages_root+'/de'])
  if (current_language == 'fr'):
    html_context['versions'].append(['latest', pages_root+'/fr'])
  if (current_language == 'es'):
    html_context['versions'].append(['latest', pages_root+'/es'])

  # and loop over all other versions from our yaml file
  # to set versions and languages
  with open("../versions.yaml", "r") as yaml_file:
    docs = yaml.safe_load(yaml_file)

  if (current_version != 'latest'):
    for language in docs[current_version].get('languages', []):
      html_context['languages'].append([language, pages_root+'/'+current_version+'/'+language])

  for version, details in docs.items():
    html_context['versions'].append([version, pages_root+'/'+version+'/'+current_language])