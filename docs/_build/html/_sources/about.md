# About This Project

## Project Overview

The Open Source Survey 2024 was conducted by the **University of Wisconsin-Madison Data Science Institute** as part of our ongoing research into software ecosystems and their impact on research and development practices.

### Mission Statement

Our mission is to provide the open source community with data-driven insights that support better decision-making, improve tool adoption, and strengthen community collaboration.

## Research Team

### Principal Investigators

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Dr. Sarah Chen
:class-header: bg-primary text-white

**Associate Professor, Computer Sciences**  
*University of Wisconsin-Madison*

Research interests: Software ecosystems, developer productivity, open source governance

📧 schen@cs.wisc.edu  
🔗 [Personal website](https://pages.cs.wisc.edu/~schen)
:::

:::{grid-item-card} Dr. Michael Rodriguez
:class-header: bg-info text-white

**Senior Research Scientist**  
*UW-Madison Data Science Institute*

Research interests: Community dynamics, network analysis, digital collaboration

📧 mrodriguez@datascience.wisc.edu  
🔗 [Research profile](https://datascience.wisc.edu/staff/rodriguez)
:::
::::

### Research Team Members

- **Dr. Lisa Park** - Postdoctoral Researcher, Survey Design & Statistical Analysis
- **James Wilson** - Graduate Research Assistant, Data Collection & Processing  
- **Maria Gonzalez** - Graduate Research Assistant, Qualitative Analysis
- **Alex Thompson** - Undergraduate Research Assistant, Data Visualization
- **Dr. Kevin Liu** - Consultant, Methodology Review

## Institutional Partners

### Primary Sponsor

**University of Wisconsin-Madison Data Science Institute**  
The DSI advances data science research and education across the UW-Madison campus, fostering interdisciplinary collaboration and innovation.

🌐 [datascience.wisc.edu](https://datascience.wisc.edu)

### Collaborating Organizations

- **NumFOCUS** - Open source scientific computing community
- **Python Software Foundation** - Python programming language development
- **R Consortium** - R statistical computing ecosystem
- **Linux Foundation** - Open source software, standards, and data initiatives
- **Mozilla Foundation** - Internet health and digital literacy

## Funding & Support

This research was supported by:

```{admonition} Funding Sources
:class: note

- **National Science Foundation** Grant #DMS-2023847 - "Understanding Open Source Software Ecosystems"
- **UW-Madison Graduate School** - Fall Competition Award 2024
- **Data Science Institute** - Internal Research Grant Program
- **Industry Partners** - In-kind support for survey infrastructure and outreach
```

## Data Availability & Access

### Open Data Commitment

In line with open science principles, we provide multiple levels of data access:

::::{tab-set}
:::{tab-item} Public Dataset
:sync: public

**Aggregate Summary Data**
- Publicly available without restrictions
- Summary statistics and cross-tabulations
- No individual response data
- Available formats: CSV, JSON, Excel

📁 [Download aggregate data](https://github.com/UW-Madison-DSI/open_source_survey_results/tree/main/data/public)
:::

:::{tab-item} Research Dataset
:sync: research

**Anonymized Individual Responses**
- Available for academic research purposes
- IRB approval and data use agreement required
- Individual responses with PII removed
- Geographic data aggregated to country level

📋 [Request research access](https://github.com/UW-Madison-DSI/open_source_survey_results/blob/main/data/research_access.md)
:::

:::{tab-item} Full Dataset
:sync: full

**Complete Raw Data**
- Available only to approved collaborators
- Requires institutional IRB approval
- Contains all collected data with identifiers removed
- Subject to additional security requirements

✉️ Contact research team for collaboration opportunities
:::
::::

### Data Use Guidelines

```{admonition} Responsible Data Use
:class: important

When using this data, please:

1. **Cite this work** using the provided citation format
2. **Respect participant privacy** - never attempt to re-identify respondents  
3. **Share derivatives** - make your analysis code and results available
4. **Follow ethical guidelines** - use data only for beneficial purposes
5. **Report issues** - notify us of any data quality concerns
```

## Reproducibility

### Open Science Practices

All aspects of this research follow open science principles:

- **Preregistration**: Study protocol registered before data collection
- **Open methodology**: Complete survey instruments and procedures documented
- **Open analysis**: All analysis code available with version control
- **Open peer review**: Manuscript reviews conducted transparently

### Code Repository

**GitHub Repository**: [UW-Madison-DSI/open_source_survey_results](https://github.com/UW-Madison-DSI/open_source_survey_results)

```{myst-md}
Repository contents:
- **Survey instruments** (`/instruments/`) - Complete questionnaire and logic
- **Data processing scripts** (`/processing/`) - Cleaning and validation code
- **Analysis notebooks** (`/analysis/`) - Statistical analysis and visualizations  
- **Report generation** (`/docs/`) - MyST Markdown source for this report
- **Supplementary materials** (`/supplements/`) - Additional tables and figures
```

### Computing Environment

**Reproducible Environment**: We provide complete computational environment specifications:

- **Python environment**: `requirements.txt` and `environment.yml`
- **R environment**: `renv.lock` with package versions
- **Docker containers**: Pre-configured analysis environment
- **Binder integration**: One-click reproducible analysis

## Publication & Dissemination

### Academic Publications

**Peer-reviewed publications** (in preparation/review):

1. "Open Source Software Adoption Patterns: A Large-Scale Survey Analysis" - *Journal of Open Source Software* (under review)
2. "Community Engagement in Open Source Projects: Barriers and Facilitators" - *ACM Transactions on Software Engineering* (in preparation)
3. "Geographic and Cultural Factors in Open Source Tool Selection" - *Information & Management* (in preparation)

### Conference Presentations

**Upcoming presentations**:

- **SciPy 2024** - Austin, TX (July 2024)
- **useR! 2024** - Salzburg, Austria (July 2024)  
- **Open Source Summit** - Seattle, WA (September 2024)
- **ACM Symposium on Computing Systems** - New York, NY (October 2024)

### Community Outreach

We actively share findings with the broader community through:

- **Blog posts** on the Data Science Institute website
- **Podcast appearances** discussing key findings
- **Webinar series** for tool maintainers and users
- **Social media** regular updates on findings

## How to Cite This Work

### Academic Citation

```
Chen, S., Rodriguez, M., Park, L., Wilson, J., Gonzalez, M., & Thompson, A. (2024). 
Open Source Survey Results 2024: Usage Patterns and Community Engagement. 
University of Wisconsin-Madison Data Science Institute. 
https://doi.org/10.5281/zenodo.8234567
```

### Bibtex Entry

```bibtex
@techreport{chen2024opensource,
  title={Open Source Survey Results 2024: Usage Patterns and Community Engagement},
  author={Chen, Sarah and Rodriguez, Michael and Park, Lisa and Wilson, James and Gonzalez, Maria and Thompson, Alex},
  institution={University of Wisconsin-Madison Data Science Institute},
  year={2024},
  doi={10.5281/zenodo.8234567},
  url={https://github.com/UW-Madison-DSI/open_source_survey_results}
}
```

## Contact Information

### Research Inquiries

For questions about methodology, data access, or collaboration opportunities:

📧 **opensourcesurvey@datascience.wisc.edu**

### Media & Press

For interviews, press releases, or media inquiries:

📧 **media@datascience.wisc.edu**  
📞 (608) 262-1234

### Technical Support

For issues with data downloads, code repositories, or technical questions:

🐛 [GitHub Issues](https://github.com/UW-Madison-DSI/open_source_survey_results/issues)

## Acknowledgments

### Survey Participants

We extend our deepest gratitude to the 1,247 individuals who took time to complete our survey and share their experiences with the open source community.

### Community Partners

Special thanks to the organizations and communities that helped promote the survey:

- **GitHub** - Survey promotion through developer newsletters
- **Stack Overflow** - Community outreach and promotion
- **Reddit communities** - r/opensource, r/programming, r/MachineLearning moderators
- **Academic conferences** - Survey promotion at SciPy, useR!, and PyData events
- **Professional associations** - ACM, IEEE Computer Society member outreach

### Technical Infrastructure

- **Qualtrics** - Survey platform and data collection tools
- **GitHub** - Code repository and collaboration platform
- **Zenodo** - Long-term data archiving and DOI assignment
- **Jupyter Book** - Documentation and report generation
- **UW-Madison IT** - Computing resources and data security

### Feedback & Review

We thank the following individuals for their valuable feedback on survey design and analysis:

- Dr. Amanda Johnson (Carnegie Mellon University)
- Prof. David Kim (UC Berkeley)  
- Dr. Rachel Thompson (MIT)
- The NumFOCUS Research Committee
- Open source maintainers who participated in pilot testing

## License & Terms

### Content License

This report and associated materials are licensed under:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

You are free to:
- Share, copy and redistribute the material
- Adapt, remix, transform, and build upon the material
- Use for any purpose, including commercially

Under the following terms:
- **Attribution**: You must give appropriate credit and indicate if changes were made

### Code License

Analysis code and software are licensed under:

**MIT License**

Permission is hereby granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to copyright notice and permission notice inclusion.

### Data License

Survey data is provided under:

**ODC Open Database License (ODbL)**

Data is freely available for any purpose, provided you:
- Attribute the original dataset
- Share any enhanced or derivative datasets under the same license
- Keep the data open

## Version History

- **v1.0.0** (June 2024) - Initial report release
- **v1.1.0** (July 2024) - Added geographic analysis and updated visualizations  
- **v1.2.0** (August 2024) - Included qualitative analysis and trend predictions
- **v2.0.0** (September 2024) - Major revision with peer review integration

---

*This project embodies our commitment to open, reproducible, and community-driven research. We welcome feedback, collaboration, and contributions from the global open source community.*