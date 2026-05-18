#!/bin/bash
set -e

if command -v pipx &> /dev/null; then
    pipx install hoocl
elif command -v pip3 &> /dev/null; then
    pip3 install hoocl
elif command -v pip &> /dev/null; then
    pip install hoocl
else
    echo "Error: pip, pip3, or pipx not found. Please install Python first: https://python.org"
    exit 1
fi