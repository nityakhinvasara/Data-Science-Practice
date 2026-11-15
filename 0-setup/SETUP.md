# Setup (do this once, about 10 minutes)

Good news: most of it is already done.
- **Python and all the libraries** are installed inside this folder (in a hidden folder called `.venv`,
  short for "virtual environment": a private copy of Python just for this project, so it can't clash
  with anything else on your Mac).
- **Jupyter knows about it.** It's registered as a kernel called **Python (Data Science Practice)**.
  ("Kernel" = the Python engine that runs your notebook's code.) Every exercise notebook already uses it.

## Step 1: Start Jupyter in this folder
**Easiest:** open Finder → your home folder → `Data-Science-Practice` → double-click **`start-jupyter.command`**.

- The first time, macOS may block it. If so, right-click it → **Open** → **Open**. This is only needed once.
- A Terminal window opens and Jupyter appears in your browser. **Keep that Terminal window open**
  while you work. Closing it stops Jupyter.

**Or from Terminal:**
```bash
cd ~/Data-Science-Practice
jupyter notebook
```

## Step 2: Check that everything works
1. In the Jupyter page, click **New → Terminal** (top right). Type this and press Enter:
   ```bash
   .venv/bin/python 0-setup/check_setup.py
   ```
2. You should see **ALL GOOD** at the end. If not, copy the message and ask for help.
3. Close that terminal tab.

## Step 3: Run your first cell
1. In Jupyter's file list, click `1-python-warmup` → `exercises.ipynb`.
2. Top right should say **Python (Data Science Practice)**. If it says something else, click it and pick that one.
3. Click the first code cell (`%run ../tools/initialise.py python`) and press **Shift+Enter**. You should see:
   `Ready: Python warm-up: 30 exercises. Use hint(n) or answer(n) when you are stuck.`
4. Type `hint(1)` in any empty cell and press Shift+Enter. It shows the hint for exercise 1.

That's it. Tick Day 0 in `DAILY-PLAN.md` (open it in Jupyter, change `- [ ]` to `- [x]`, then **File → Save**).
Don't start the exercises yet if your exams are on!

## Step 4: Turn off AI help while practising
If your Jupyter has an AI assistant or autocomplete (e.g. Jupyter AI), switch it off for practice.
You learn by typing, not by accepting suggestions.

---

## Reading the guides (`.md` files)
Jupyter opens `.md` files as plain text, which is readable but not pretty. For the nicely formatted version:
- **On GitHub** (also works on your phone): https://github.com/nityakhinvasara/Data-Science-Practice. Click a folder, then `guide.md`.
- **Or in JupyterLab** (run `jupyter lab` instead of `jupyter notebook`): right-click the file → **Open With → Markdown Preview**.

## Useful keys in notebooks
| Key | What it does |
|---|---|
| **Shift+Enter** | Run this cell, move to the next |
| **Esc** then **B** | Add a new empty cell below |
| **Esc** then **D D** | Delete the cell |
| **Esc** then **M** / **Y** | Turn a cell into text (markdown) / back into code |
| **Cmd+S** | Save (Jupyter also autosaves every few minutes) |
| **Kernel → Restart** | Fresh start if things act weird. Then re-run the first cell |

## If something goes wrong
- **"ModuleNotFoundError: No module named 'pandas'"**: the wrong kernel is selected. Click the kernel
  name (top right) and choose **Python (Data Science Practice)**.
- **"File not found ../data/..."** or **"../tools/initialise.py not found"**: you started Jupyter
  from another folder and opened a copy of the notebook. Start it with `start-jupyter.command` and open
  the notebook from inside the topic folder.
- **Kernel missing from the list**: in Terminal, run
  ```bash
  cd ~/Data-Science-Practice
  .venv/bin/python -m ipykernel install --user --name ds-practice --display-name "Python (Data Science Practice)"
  ```
- **Need to reinstall the libraries** (e.g. you deleted `.venv`):
  ```bash
  cd ~/Data-Science-Practice
  python3.13 -m venv .venv
  .venv/bin/pip install -r 0-setup/requirements.txt
  ```
  Then run the kernel command above.
