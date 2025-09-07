# 2024 UW-Madison Open Source Program Office Survey

In Spring 2024 the Open Source Program Office at UW-Madison distributed an open source survey to gauge the usage of open source tools among members of the university community, identify open source projects under development, and to collect feedback on improving the open source environment at UW-Madison. This repo is for a site for summarizing and presenting results from the survey using Myst Markdown.

Run locally 
```aiignore
cd docs
pip install -U jupyter-book
jupyter-book build .
# open the site:
open _build/html/index.html   # or: python -m http.server inside _build/html

```