# 2024 UW–Madison Open Source Program Office Survey

[![Deploy to GitHub Pages](https://github.com/UW-Madison-DSI/open_source_survey_results_myst/actions/workflows/publish.yml/badge.svg)](https://github.com/UW-Madison-DSI/open_source_survey_results_myst/actions/workflows/publish.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17379408.svg)](https://doi.org/10.5281/zenodo.17379408)

In Spring 2024, the [Open Source Program Office at UW–Madison](https://ospo.wisc.edu/) conducted a survey to:

- Assess the use of open source tools across the university community  
- Identify open source projects currently under development  
- Gather feedback on strengthening the open source ecosystem at UW–Madison  

This repository hosts a [MyST site](https://mystmd.org) that summarizes and presents results from the survey.

📍 **Live MyST site:** [Survey Results (MyST)](https://uw-madison-dsi.github.io/open_source_survey_results_myst/)  
📍 **R-based Quarto site:** [Survey Results (Quarto)](https://uw-madison-dsi.github.io/open_source_survey_results/)

---

## 📌 Table of Contents

- [Two Ways to Use This Repository](#-two-ways-to-use-this-repository)
- [Repository Overview](#repository-overview)
- [Technical Stack](#technical-stack)
- [Build Locally](#build-locally)
- [Project Structure](#-project-structure)
- [Citation](#citation)
- [Survey Resources](#-survey-resources)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)

---

## 🎯 Two Ways to Use This Repository

### 1️⃣ View UW–Madison's Survey Results (Branch: `main`)

Explore our findings on open source usage, campus culture, and community needs at UW–Madison.

To build and preview the site on your machine:

```commandline
# Navigate to docs folder
cd survey_results_docs/docs

# Install dependencies
pip install -U jupyter-book

# Build the site
jupyter-book clean .
jupyter-book build .

# Open in browser
open _build/html/index.html
# Or run a local server
python -m http.server -d _build/html
```

### 2️⃣ Create Your Own Survey Site (Branch: `cookiecutter-template`)

**Conducting a similar survey at your institution?** Use our Cookiecutter template to generate a fully customized version:

```bash
pip install cookiecutter

cookiecutter gh:UW-Madison-DSI/open_source_survey_results_myst --checkout cookiecutter-template
```


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

Maria Oros, Data Scientist