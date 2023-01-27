"""Dummy file for pipreqs to add PyYAML to requirements.txt."""
import PyYAML  # to read by pipreqs

_ = PyYAML.load()  # to suppress unused module errors in pre-commit
