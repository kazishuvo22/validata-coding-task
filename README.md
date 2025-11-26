# validata-coding-task

## Python Virtual Environment Setup Guide
### 1. Install Python
Download Python from the official website:
https://www.python.org/downloads/

Verify installation:
```bash
python --version
```
or on some systems:
```bash
python3 --version
```

N.B: I used python 3.13.3

### 2. Create a Virtual Environment

#### Navigate to the project folder:
```bash
cd validata-coding-task
```

#### Create the virtual environment:
```bash
python -m venv venv
```
or if python3,
```bash
python3 -m venv venv
```

This creates a folder named venv containing the isolated environment.

### 3. Activate the Virtual Environment
#### Windows (PowerShell / CMD)
```bash
venv\Scripts\activate
```

#### macOS / Linux
```bash
source venv/bin/activate
```

### 4. Install Packages Inside the Virtual Environment
```bash
pip install -r requirements.txt
```

### 5. Run
#### Part-1
```bash
python part-1/main.py
```