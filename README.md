# Playwright Python Automation Framework

A UI test automation framework built with Playwright and Python (pytest-playwright), following the Page Object Model (POM) design pattern.

## Tech Stack
- Python
- Playwright (pytest-playwright)
- Pytest

## Features
- Page Object Model (POM) for maintainable test scripts
- Reusable fixtures via conftest.py (browser setup/teardown)
- Data-driven testing using pytest parametrize
- Screenshot capture on test failure
- Playwright trace viewer for debugging
- Semantic locators (get_by_role, get_by_placeholder, data-test)

## Structure
- `pages/` - Page classes with locators and action methods
- `test_*.py` - Test cases using the page objects
- `conftest.py` - Fixtures and hooks

## Running Tests
```
pytest test_login.py -s
```
