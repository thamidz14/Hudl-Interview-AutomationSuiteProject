# Hudl Selenium Test Automation Suite

## Project Overview
This project is an automated Selenium test suite for Hudl's login and account management flows. It covers both positive (happy path) and negative scenarios, including:
- Valid login
- Password reset
- Account creation (from multiple entry points)
- Handling invalid usernames/passwords
- Weak password and missing field validation

The suite uses **pytest** for test execution, **Allure** for reporting, and supports data-driven testing with external JSON files. All sensitive data and URLs are managed via environment variables and a config file.

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/thamidz14/Hudl-Interview-AutomationSuiteProject.git
   cd Hudl-Interview-AutomationSuiteProject
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env` and fill in your real credentials:
     ```
     HUDL_TEST_PASSWORD=your_password_here
     HUDL_LOGIN_URL=https://...
     HUDL_PASSWORD_URL=https://...
     ```

5. **(Optional) Download ChromeDriver**
   - Make sure ChromeDriver is installed and matches your Chrome version. Place it in your PATH or project directory.

---

## How to Run Tests

Run all tests:
```bash
pytest
```

Run only happy path or negative path tests:
```bash
pytest tests/Happy_Path/
pytest tests/Negative_Path/
```

---

## How to Generate Allure Reports

1. **Run tests with Allure results output:**
   ```bash
   pytest --alluredir=allure-results
   ```
2. **Generate and open the Allure report:**
   ```bash
   allure serve allure-results
   ```
   (Or, to generate static HTML: `allure generate allure-results -o allure-report`)

---

## Prerequisites
- Python 3.8+
- Google Chrome browser
- ChromeDriver (version matching your Chrome)
- Allure commandline (for reports): https://docs.qameta.io/allure/

---

## File/Folder Structure

```
Hudl-Interview-AutomationSuiteProject/
├── pages/                 # Page Object Model classes
├── tests/
│   ├── Happy_Path/        # Positive flow test cases
│   └── Negative_Path/     # Negative flow test cases
├── utils/
│   ├── config.py          # Centralized URLs and config
│   ├── testdata.py        # Random data generators
│   └── *.json             # Test data files (parameterization)
├── conftest.py            # Pytest fixtures (browser setup, etc.)
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── test_cases_document.xlsx # Test case documentation (Excel)
└── README.md
```

---

## Additional Notes
- Do **not** commit your real `.env` file or credentials.
- All test data for parameterized tests is in `utils/*.json`.
- The suite is designed for maintainability and scalability—add new flows by extending the page objects and adding new test data.

---

For any questions or issues, contact the project maintainer.
