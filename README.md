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

## 🤝 Contributing

If you'd like to contribute, please fork the repository and submit a pull request.  
Collaborators can be added directly via GitHub repo settings.

---
