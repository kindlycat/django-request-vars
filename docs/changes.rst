Changelog
=========

Version 2.0.0 (unreleased)
--------------------------
- Replace setup.py/setup.cfg legacy build with PEP 621 pyproject
(hatchling backend, dynamic version from request_vars/__init__.py)
- Migrate to uv for dependency management
- Replace black/isort/flake8 with ruff
- Migrate tests from Django's unittest runner to pytest
- Support Django 5.2/6.0/6.1 and Python >=3.11 only
- Remove django-jinja in favor of Django's native Jinja2 backend
- Replace CI with GitHub Actions (tests, linter, release)

Version 1.0.0 (2018-05-13)
--------------------------
Release
