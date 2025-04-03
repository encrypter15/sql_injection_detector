#!/usr/bin/env python3
# SQL Injection Detector
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Explains detection logic. Detects SQL injection patterns.

import re
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='sql_injection_detector.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"patterns": [r"\b(union|select|drop|insert|update|delete)\b.*\b(from|where|into)\b",
                            r"[';]--", r"1=1"]}

def detect_sql_injection(input_str: str, patterns: list) -> bool:
    """Detect SQL injection patterns in input."""
    for pattern in patterns:
        if re.search(pattern, input_str, re.IGNORECASE):
            return True
    return False

def main():
    """Main function to parse args and detect SQL injection."""
    parser = argparse.ArgumentParser(description="SQL Injection Detector")
    parser.add_argument("--input", required=True, help="String to analyze")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    logging.info(f"Analyzing input: {args.input}")
    if detect_sql_injection(args.input, config["patterns"]):
        logging.warning(f"Potential SQL injection detected: {args.input}")
        print(f"Warning: Potential SQL injection detected in '{args.input}'")
    else:
        logging.info("No SQL injection patterns found")
        print("No SQL injection patterns detected")

if __name__ == "__main__":
    main()
