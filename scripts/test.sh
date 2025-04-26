#!/bin/bash

echo "Running tests..."

source venv/bin/activate
pytest --junitxml=reports/test-results.xml

echo "Tests completed. Report generated at reports/test-results.xml."
