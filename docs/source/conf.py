import os
import sys
import time

sys.path.append(os.path.abspath("tools/extensions"))
sys.path.append(os.path.abspath("includes"))

project = "Defilepsie"
copyright = f'2024-{time.strftime("%Y")}, Laurent Jouron'
author = "Laurent Jouron"

extensions = [
    "notfound.extension",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinxext.opengraph",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "venv*",
    "env*",
    "README.rst",
    ".github",
]

language = "fr"

nitpicky = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_logo = "_static/defilepsie-logo.png"
html_favicon = "_static/defilepsie.png"
html_title = "Défilepsie"
html_theme_options = {
    "source_repository": "https://github.com/LaurentJouron/defilepsie",
    "source_directory": "docs/",
    "source_branch": "master/source",
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "top_of_page_button": None,
    "light_css_variables": {
        "color-brand-primary": "#bf1e2e",
        "color-brand-content": "#bf1e2e",
        "font-stack": "Verdana, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3C65AF",
        "color-brand-content": "#3C65AF",
        "font-stack": "Verdana, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/LaurentJouron/defilepsie",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

html_css_files = [
    "devguide_overrides.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_js_files = [
    "activate_tab.js",
]

pygments_style = "sphinx"
pygments_dark_style = "monokai"

todo_include_todos = True

# sphinx-notfound-page
notfound_urls_prefix = "/"

# sphinx.ext.extlinks
extlinks = {
    "github": ("https://github.com/%s/", "%s"),
}

# sphinxext-opengraph config
ogp_site_url = "https://laurentjouron.github.io/"
ogp_site_name = "Defilepsie"
ogp_image = "_static/defilepsie-logo.png"
ogp_custom_meta_tags = [
    '<meta property="og:image:width" content="200">',
    '<meta property="og:image:height" content="200">',
    '<meta name="theme-color" content="#3776ab">',
]

# Strip the dollar prompt when copying code
copybutton_prompt_text = "$ "
copybutton_line_continuation_character = "\\"
