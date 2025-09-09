
# How to Use Colab with Our Repo

## Opening a notebook
1. Go to our GitHub repo page.
2. Click the Colab badge in the README or open any notebook inside `/notebooks`.
3. The notebook will launch in Google Colab in your browser.

## Editing and running
- Run code cells by pressing **Shift+Enter**.
- Add new cells with the `+ Code` or `+ Text` buttons.
- Change text in Markdown cells (headings, notes, summaries).

## Saving your work
### Option 1 — Save directly to GitHub (recommended)
1. In Colab: File → Save a copy in GitHub.
2. Pick our repo and the `notebooks/` folder.
3. Commit message: write a short description (e.g. "Experiment on thin Si membranes").

### Option 2 — Download and commit
1. File → Download → Download `.ipynb`.
2. Drop it into the local `notebooks/` folder in your cloned repo.
3. Use GitHub Desktop to commit + push.

## Exporting a polished version
- If your notebook is finished or needs to be shared outside the repo:
  - File → Download → PDF or HTML.
  - Save the file into `/reports/` with today’s date in the filename:
    - Example: `reports/2025-09-09_light_transmission_results.pdf`.

## Rules of thumb
- Always keep `.ipynb` notebooks in `/notebooks/`.
- Use descriptive filenames: `2025-09-09_topic_author.ipynb`.
- Do **not** upload raw data here — all data stays in OneDrive.
- End each notebook with a short summary in Markdown.
