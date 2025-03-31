# 🧠 NLP Project

This is an NLP (Natural Language Processing) project developed using **Python 3.9.2**.  
It is recommended to set up your environment with the same Python version to avoid compatibility issues.

---

## 🚀 Project Setup

### 🐍 Python Version
This project uses **Python 3.9.2**. Please ensure you're using this version before installing dependencies.

---

### 🔧 Option 1: Use `pyenv` or `pyenv-win` (Recommended)

#### 👉 Step-by-step:

1. Install `pyenv`:
   - macOS/Linux: https://github.com/pyenv/pyenv
   - Windows: https://github.com/pyenv-win/pyenv-win

2. After installing, run:
   ```bash
   pyenv install 3.9.2
   pyenv local 3.9.2
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   - On **Windows (CMD)**:
     ```cmd
     venv\Scripts\activate.bat
     ```

   - On **Windows (PowerShell)**:
     ```powershell
     venv\Scripts\Activate.ps1
     ```

5. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

### 🐍 Option 2: Use `conda` (For Anaconda/Miniconda Users)

#### 👉 Step-by-step:

1. Make sure Conda is installed:
   - https://www.anaconda.com/download
   - or https://docs.conda.io/en/latest/miniconda.html

2. Create a new environment:
   ```bash
   conda create -n nlp-env python=3.9.2
   ```

3. Activate the environment:
   ```bash
   conda activate nlp-env
   ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📁 Project Structure

```
NLP PROJECT/
│
├── data/                  # 📊 All generated CSV files go here
│   ├── train.csv
│   ├── test.csv
│   ├── train_urls.csv
│   ├── test_urls.csv
│   ├── vocab.csv
│   └── embedding_scores.csv
│
├── documents/             # 📄 Project documentation and info
│   ├── naming_conventions.docx
│   ├── project_outline.md
│   └── dataset_info.md
│
├── myenv/                 # 🐍 Python virtual environment
│
├── notebooks/             # 📒 Jupyter notebooks for EDA/modeling
│   └── imdb_sentiment_analysis.ipynb
│
├── outputs/               # 📈 Model results, plots, logs
│
├── src/                   # 🧠 Python source files
│   └── generate_csv.py    # Script to convert dataset to CSVs
│
├── .gitignore             # 🧼 Ignore virtualenv, pycache, etc.
├── README.md              # 📘 Project overview and setup
├── requirements.txt       # 📦 Required Python packages
```

---

## 🏷️ Label Meaning

In all CSV files generated from the dataset:

- `1` → **Positive review**
- `0` → **Negative review**
- `-1` → **Unlabeled review** (from the `unsup` folder)

---

## 🤝 Contributing

If you'd like to contribute, please fork the repository and submit a pull request.  
Collaborators can be added directly via GitHub repo settings.

---
