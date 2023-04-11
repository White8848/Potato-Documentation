# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Potato'
copyright = '2023, 北京智慧土豆科技有限公司'
author = '北京智慧土豆科技有限公司'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
# html_static_path = ['_static']
html_theme_options = {
        # 'canonical_url': '',
        # 'analytics_id': 'G-EVD5Z6G6NH',
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'None',
        # Toc options
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4,
    }

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
