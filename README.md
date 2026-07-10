# Project Login

A Flask login application with a landing page.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

## Important

`users.xlsx` is intentionally excluded from Git because it contains local user credentials. Create and keep that file only in your deployment environment; it must contain `Username` and `Password` columns.
