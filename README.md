# 2024 UW–Madison Open Source Program Office Survey

In Spring 2024, the [Open Source Program Office at UW–Madison](https://ospo.wisc.edu/) conducted a survey to:  

- Assess the use of open source tools across the university community  
- Identify open source projects currently under development  
- Gather feedback on strengthening the open source ecosystem at UW–Madison  

This repository hosts a [MyST site](https://mystmd.org) that summarizes and presents results from the survey.  

📍 **Live site:** [Survey Results on GitHub Pages](https://uw-madison-dsi.github.io/open_source_survey_results_myst/)  
📍 **Companion site (Quarto, for R users):** [Quarto site](https://uw-madison-dsi.github.io/open_source_survey_results/)

---

## Repository Overview

- **`docs/`** – Source files for the MyST site  
- **`setup.py`** – University branding and plot styling  
- **Page files (e.g., `usage.qmd`)** – Survey-specific analyses, figures, and customizations  

🔧 **Customization:**  
- Theming (colors, fonts, layout) is managed in `setup.py`.  
- Figures and highlights for open source tools are defined within the individual page files.  

---

## Technical Stack

This project is built with:  
- [MyST Markdown](https://mystmd.org/) and [Jupyter Book](https://jupyterbook.org/) for site generation  
- [Python](https://www.python.org/) for data wrangling and analysis  
- [Plotly](https://plotly.com/python/) for interactive visualizations  
- [GitHub Actions](https://docs.github.com/actions) for automated deployment to GitHub Pages  

---

## Build Locally

To build and preview the site on your machine:

```bash
# Navigate to docs folder
cd docs

# Install dependencies
pip install -U jupyter-book

# Build the site
jupyter-book build .

# Open in browser
open _build/html/index.html
# Or run a local server
python -m http.server -d _build/html
