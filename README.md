# py-env-inspector

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-env-inspector/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency environment variable schema auditor and validator against `.env.example` templates.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library.
- 🔍 **Audit & Compare**: Detects missing variables, empty values, and undeclared extras.
- 🚨 **CI/CD & Startup Checks**: Halt server boot before runtime crashes due to unconfigured keys.

---

## 📦 Installation

```bash
pip install py-env-inspector
```

---

## 🛠️ Quickstart

```python
from py_env_inspector import audit_env

# Audit environment against .env.example
report = audit_env(example_path=".env.example")
if not report.is_valid:
    print("Missing environment variables:", report.missing_keys)
    raise SystemExit(1)
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this auditor prevented production outages due to missing env variables, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [buymeacoffee.com/kcidi4148](https://buymeacoffee.com/kcidi4148)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
