[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)  

[![formatter:docformatter](https://img.shields.io/badge/formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

---

# pre-commit

> 1. **pip install pre-commit**
>2. *create file* **.pre-commit-config.yaml**

>[Supported hooks](https://pre-commit.com/hooks.html)

>3. **pre-commit install** - *git hook scripts*
>4. *git add files !!!*
>5. **pre-commit run --all-files** *or just commit...*  (-a)


>6. **pre-commit autoupdate** - update repos

---

# pipreqs

>1. **pip install pipreqs**

>2. *run* **pipreqs --encoding utf-8 --force --ignore .\tests\ .** *-  
    make requirements.txt for all .py files in current directory, force option to overwrite existing file,* **--print** *- to see only in terminal*