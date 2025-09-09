
# Research Project Starter

Easy workflow for mixed-experience teams:
- Data in OneDrive (not in Git)
- Code and notebooks in this GitHub repo
- Click the badge to open key notebooks in Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LGislason/SDSMT-nano/blob/main/notebooks/00_template.ipynb)

## Quick start
1. Click the Colab badge to open the starter notebook.
2. Put raw data in your OneDrive folder, for example `OneDrive/ProjectName/data/raw`.
3. Update the `DATA_DIR` path in the notebook if needed.
4. Commit changes with GitHub Desktop or the website.

## Repo layout
```
project/
  README.md
  requirements.txt
  .gitignore
  .gitattributes
  .pre-commit-config.yaml
  notebooks/
    00_template.ipynb
  src/
    project_name/
      __init__.py
      utils.py
  notes/
    meeting_template.md
  reports/
    figures/
  data/            # ignored by Git
    raw/
    processed/
  .github/
    workflows/
      execute-notebooks.yml
```

## Conventions
- Work in `notebooks/`
- Keep reusable code in `src/project_name/`
- Save figures to `reports/figures/`
- Large data stays in OneDrive, not in Git
- Use short, frequent commits
