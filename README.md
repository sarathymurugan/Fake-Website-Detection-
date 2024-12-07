# Fake Website Detection

## Overview

The **Fake Website Detection** project is a Python-based tool designed to help identify potentially fake websites by analyzing the provided URL. The tool checks for common indicators such as the use of HTTPS, suspicious keywords in the domain name, and general URL validity. This project is aimed at providing a simple mechanism to detect fraudulent or phishing websites.

## Features

- **URL Validation**: Ensures the URL is properly formatted.
- **HTTPS Check**: Validates whether the website uses HTTPS, a common security feature.
- **Suspicious Keyword Detection**: Identifies common suspicious keywords (e.g., "login", "secure", "paypal") in the URL that could indicate a fake or phishing website.
- **User-friendly Output**: Provides clear feedback on whether the website seems safe or potentially fake.

## Installation

### Prerequisites

Before running the script, you need to have Python installed on your system. Additionally, the following Python libraries are required:

- `requests`: To handle HTTP requests (although it's not used in the current version, you may extend functionality later).
- `validators`: To validate URL format.

### Install the Required Libraries

To install the necessary libraries, run the following command in your terminal:

```bash
pip install requests validators
