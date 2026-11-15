# Setup (do this once, about 20 minutes)

Good news: **Python and all the libraries are already installed** inside this folder (in a hidden
folder called `.venv`, short for "virtual environment": a private copy of Python just for this
project, so it can't clash with anything else on your Mac). You only need to connect VS Code to it.

## Step 1: Open the folder in VS Code
1. Open **Visual Studio Code**.
2. Menu **File → Open Folder…**
3. Pick **Data-Science-Practice** (it's in your home folder, next to Desktop and Downloads). Click **Open**.
4. If VS Code asks "Do you trust the authors of the files in this folder?", click **Yes, I trust the authors**.

## Step 2: Install the Jupyter extension
"Jupyter" is what lets you run `.ipynb` notebooks (files with code cells you run one at a time).
1. VS Code may pop up "Do you want to install the recommended extensions?". Click **Install**. Done!
2. If it doesn't pop up: click the **Extensions** icon in the left bar (four squares), search
   **Jupyter**, and install the one by **Microsoft**. Also make sure **Python** (by Microsoft) is installed.

## Step 3: Turn off AI autocomplete while practising
If you have GitHub Copilot or another AI suggestion tool installed: click its icon in the bottom bar
and choose **Disable completions** (or disable the extension for this folder). You learn by typing,
not by pressing Tab.

## Step 4: Check that everything works
1. In VS Code, open a terminal: menu **Terminal → New Terminal**.
2. Type this and press Enter:
   ```bash
   .venv/bin/python 0-setup/check_setup.py
   ```
3. You should see **ALL GOOD** at the end. If not, copy the message and ask for help.

## Step 5: Run your first notebook cell
1. In the left file list, open `1-python-warmup/exercises.ipynb`.
2. Top right, click **Select Kernel** → **Python Environments** → choose **.venv (Python 3.13)**.
   ("Kernel" = the Python engine that runs your notebook's code.) VS Code should remember this.
3. Click the first code cell and press **Shift+Enter**. You should see:
   `Ready: Python warm-up: 30 exercises. Use hint(n) or answer(n) when you are stuck.`
4. Type `hint(1)` in any empty cell and press Shift+Enter. It shows the hint for exercise 1.

That's it. Tick Day 0 in `DAILY-PLAN.md`. Don't do the exercises yet if your exams are on!

---

## Useful keys in notebooks
| Key | What it does |
|---|---|
| **Shift+Enter** | Run this cell, move to the next |
| **Esc** then **B** | Add a new empty cell below |
| **Esc** then **D D** | Delete the cell |
| **Cmd+/** | Turn the selected lines into comments (or back) |
| **Restart** button (top) | Fresh start if things act weird. Then re-run the first cell |

## If something goes wrong
- **"ModuleNotFoundError: No module named 'pandas'"**: the wrong kernel is selected. Do Step 5.2 again.
- **"File not found ../data/..."**: you opened the notebook from somewhere else. Open it from inside the
  `Data-Science-Practice` folder in VS Code.
- **Need to reinstall the libraries** (e.g. you deleted `.venv`): in the terminal run
  ```bash
  python3.13 -m venv .venv
  .venv/bin/pip install -r 0-setup/requirements.txt
  ```
