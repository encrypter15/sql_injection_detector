# SQL Injection Detector

## Overview
The SQL Injection Detector is a Python tool that identifies potential SQL injection patterns in input strings using regular expressions. It checks for common attack signatures and logs findings.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- No additional libraries beyond the Python standard library

## Usage
Run the script with the following arguments:

```bash
python3 sql_injection_detector.py --input <STRING> [--config <CONFIG_FILE>]
