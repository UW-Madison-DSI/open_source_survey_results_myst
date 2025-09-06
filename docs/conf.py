# Configuration file for MyST
extensions = [
    'myst_nb',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

html_theme = 'sphinx_book_theme'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.github']

# MyST configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# Execute notebooks
nb_execution_mode = "auto"

# Project information
project = 'Open Source Survey Results'