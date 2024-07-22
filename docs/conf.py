import os
import sys
import django

# Fügen Sie den Pfad zu Ihrem Projekt hinzu
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../taskapp'))

# Django-Einstellungen initialisieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'join_backend.settings'
django.setup()

project = 'SCRUM Backend'
copyright = '2024, jad'
author = 'jad'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
