#!/bin/bash
set -eo pipefail

pip install --upgrade pip
pip install .
python -m pugsebot.cli --no-dev
