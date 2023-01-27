[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)  

[![formatter:docformatter](https://img.shields.io/badge/formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

---

# pre-commit

1. **pip install pre-commit**
2. *create file* **.pre-commit-config.yaml**


```yaml
repos:
-   repo: https://github.com/PyCQA/docformatter.git
    rev: v1.5.1
    hooks:
    -   id: docformatter
-   repo: https://github.com/hadialqattan/pycln.git
    rev: v2.1.3
    hooks:
    -   id: pycln
-   repo: https://github.com/PyCQA/flake8.git
    rev: 6.0.0
    hooks:
    -   id: flake8
-   repo: https://github.com/PyCQA/pylint.git
    rev: v2.16.0b0
    hooks:
    -   id : pylint
        args: ["--ignored-modules=yaml,dotenv,PyYAML"]
-   repo: https://github.com/charliermarsh/ruff-pre-commit.git
    rev: v0.0.236
    hooks:
    -   id: ruff
-   repo: https://github.com/psf/black
    rev: 22.12.0
    hooks:
    -   id: black
-   repo: https://github.com/pre-commit/mirrors-mypy.git
    rev: v0.991
    hooks:
    -   id: mypy
        additional_dependencies: [types-PyYAML==6.0.12.3]
-   repo: https://github.com/PyCQA/bandit.git
    rev: 1.7.4
    hooks:
    -   id: bandit
```
[Supported hooks](https://pre-commit.com/hooks.html)

3. **pre-commit install** - *git hook scripts*
4. *git add files !!!*
5. **pre-commit run --all-files** *or just commit...*

---

# pipreqs

1. **pip install pipreqs**
2. *run* **pipreqs --force .** *- make requirements.txt for all .py files in current directory, force option to overwrite existing file,* **--print** *- to see only in terminal*