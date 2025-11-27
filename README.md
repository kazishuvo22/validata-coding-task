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
#### Part_1
```bash
python part-1/main.py
```

#### Part_2

##### Windows
1. Download MSSQL Server 2019
```
https://go.microsoft.com/fwlink/?linkid=866662
```
Also install ODBC Driver 17 for SQL Server

2. Setup Custom Server Configuration
3. Go to the part-2 directory
```bash
cd part_2
```
4. Rename ```.env.example``` to ```.env``` and set the database information and secrets
5. Install Packages Inside the Virtual Environment if not installed
```bash
pip install -r requirements.txt
```
6. Run Tests
```bash
pytest -v tests/test_banks.py
```
7. Run flask app by using the following command
```bash
flask run --debug
```
8. Test using Rested Client (Must run the flask server while testing this)
```bash
python rest_client.py
```






