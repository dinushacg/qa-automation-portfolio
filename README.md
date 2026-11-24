@"
# QA Automation Portfolio

A professional QA automation test suite demonstrating API testing, UI browser automation, CI/CD integration, and test reporting — built with Python, Pytest, and Playwright.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Test language |
| Pytest | Test framework |
| Playwright | Browser automation |
| Requests | HTTP client for API tests |
| jsonschema | API response schema validation |
| GitHub Actions | CI/CD pipeline |
| Allure | Test reporting |

## Setup and Run Locally

### 1. Clone the repo
git clone https://github.com/dinushacg/qa-automation-portfolio.git

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt
playwright install chromium

### 4. Run tests
pytest api_tests/ -v
pytest ui_tests/ -v

## CI/CD

Tests run automatically on every push to main via GitHub Actions. Green checkmark confirms all tests pass.

## Author

Dinusha Gunathilaka
Senior QA Automation Engineer
Ontario, Canada
"@ | Out-File -FilePath "README.md" -Encoding utf8