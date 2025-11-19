# 2024 UW–Madison Open Source Program Office Survey

[![Deploy to GitHub Pages](https://github.com/UW-Madison-DSI/open_source_survey_results_myst/actions/workflows/publish.yml/badge.svg)](https://github.com/UW-Madison-DSI/open_source_survey_results_myst/actions/workflows/publish.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17379408.svg)](https://doi.org/10.5281/zenodo.17379408)

In Spring 2024, the [Open Source Program Office at UW–Madison](https://ospo.wisc.edu/) conducted a survey to:

- Assess the use of open source tools across the university community
- Identify open source projects currently under development
- Gather feedback on strengthening the open source ecosystem at UW–Madison

This repository hosts a [MyST site](https://mystmd.org) that summarizes and presents results from the survey.

📍 **Live site:** [Survey Results on GitHub Pages](https://uw-madison-dsi.github.io/open_source_survey_results_myst/)  
📍 **Companion site (Quarto, for R users):** [Quarto site](https://uw-madison-dsi.github.io/open_source_survey_results/)

---

## 🎯 Two Ways to Use This Repository

### 1️⃣ View UW-Madison's Survey Results (Current Branch: `main`)

Explore our findings on open source usage, campus culture, and community needs at UW-Madison.

### 2️⃣ Create Your Own Survey Site (Branch: `cookiecutter-template`)

**Conducting a similar survey at your institution?** Use our Cookiecutter template to generate a fully customized version!
```bash
# Install cookiecutter
pip install cookiecutter

# Generate your own survey site
cookiecutter gh:UW-Madison-DSI/open_source_survey_results_myst --checkout cookiecutter-template
```

**The template will prompt you for:**
- Institution name and branding
- Primary color (hex code)
- Contact information
- Survey year
- GitHub organization

**What you get:**
- ✅ Customized MyST site with your institution's branding
- ✅ All analysis code and structure from our survey
- ✅ GitHub Actions workflow for automatic deployment
- ✅ Interactive Plotly visualizations
- ✅ Responsive design with custom footer

[**→ Learn more about the template**](https://github.com/UW-Madison-DSI/open_source_survey_results_myst/tree/cookiecutter-template)

---

## Repository Overview

- **`survey_results_docs/docs/`** – Source files for the MyST site
  - **`setup.py`** – University branding and plot styling
  - **`_config.yml`** – Site configuration
  - **Page files (e.g., `usage.md`, `campus.md`)** – Survey-specific analyses and visualizations
  - **`data/`** – Anonymized survey data
  - **`_static/`** – Custom CSS, logos, and assets

🔧 **Customization:**
- Theming (colors, fonts, layout) is managed in `setup.py` and `_config.yml`
- Figures and highlights for open source tools are defined within the individual page files

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
cd survey_results_docs/docs

# Install dependencies
pip install 'jupyter-book<2.0' pandas plotly matplotlib

# Build the site
jupyter-book clean .
jupyter-book build .

# Open in browser
open _build/html/index.html

# Or run a local server
python -m http.server -d _build/html
```

---

## 📁 Project Structure
```
open_source_survey_results_myst/
├── .github/workflows/
│   └── publish.yml              # GitHub Actions deployment
├── survey_results_docs/docs/
│   ├── _config.yml              # Jupyter Book configuration
│   ├── _toc.yml                 # Table of contents
│   ├── _static/                 # CSS, images, logos
│   ├── data/                    # Survey data (anonymized CSV)
│   ├── setup.py                 # Python utilities and theming
│   ├── index.md                 # Home page
│   ├── sample.md                # Demographics analysis
│   ├── usage.md                 # Tool usage patterns
│   ├── sentiments.md            # Perceptions and value
│   ├── campus.md                # Campus culture
│   └── reproduction.md          # Reproduction guide
└── README.md
```

---

## Citation

If you use this work or reproduce the survey at your institution, please cite:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17379408.svg)](https://doi.org/10.5281/zenodo.17379408)
```bibtex
@misc{uw_madison_ospo_2024,
  title={UW-Madison Open Source Program Office Survey Results},
  author={UW-Madison Data Science Institute},
  year={2024},
  doi={10.5281/zenodo.17379408},
  url={https://uw-madison-dsi.github.io/open_source_survey_results_myst/}
}
```

---

## 📊 Survey Resources

- **Survey instrument (Qualtrics .qsf):** [Download](https://github.com/UW-Madison-DSI/open_source_survey_results/blob/main/Open_Source_Program_Office_Survey.qsf)
- **Anonymized data:** Available in `survey_results_docs/docs/data/`
- **Reproduction guide:** See [reproduction.md](https://uw-madison-dsi.github.io/open_source_survey_results_myst/reproduction.html)

This project was inspired by the [NYU DS3 Needs Assessment Survey](https://github.com/ds3-nyu/Needs-Assessment-Survey).

---

## 🤝 Contributing

Contributions are welcome! Whether you're:
- Fixing bugs or typos
- Improving documentation
- Enhancing visualizations
- Sharing feedback on the survey methodology

Please open an issue or submit a pull request.

---

## 📧 Contact

**Data Science Institute**
- Email: maria.oros@wisc.edu
**UW-Madison Open Source Program Office**
- Email: ospo@datascience.wisc.edu
- Website: https://ospo.wisc.edu
- Twitter: [@datascience_uw](https://x.com/datascience_uw)
- Join our community: [OSPO Google Group](https://groups.google.com/g/ospo-uw)

---

## 🌟 Acknowledgments

This project was made possible by a grant from the [Alfred P. Sloan Foundation](https://sloan.org/).

Special thanks to:
- UW-Madison Data Science Institute
- UW-Madison Libraries
- All survey participants who shared their experiences
- The MyST, Jupyter Book, and Plotly communities

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ by the UW-Madison Open Source Program Office</sub>
</div>
