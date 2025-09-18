#!/usr/bin/env bash
rm -rf dist/ build/
python3 setup.py bdist_wheel
python3 -m twine upload --repository gitlab dist/*