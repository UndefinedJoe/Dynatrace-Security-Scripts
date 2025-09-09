# Prerequisites

## Required Software

Python 3.6 or higher
requests library (pip install requests)
A Dynatrace environment with API access
Required Permissions

Your Dynatrace API token must have the following permissions:
Read entities (entities.read)
Write settings (settings.write)
Read settings (settings.read)
Creating an API Token

Log into your Dynatrace environment
Navigate to Personal Access Tokens

Select the required scopes:
entities.read
settings.write
settings.read

Name your token (e.g., "Code Module Enabler")
Click Generate token and copy the token value


## Installation

1. Download the Script

Save the script as enable_codemodules.py on your system.
2. Install Dependencies

pip install requests
Configuration

Linux/macOS

# Set environment variables for current session
export DT_API_TOKEN='your-api-token-here'
export DT_ENV_URL='https://<tenantID>.live.dynatrace.com'

# Run the script
python enable_codemodules.py
Windows PowerShell

$env:DT_API_TOKEN='your-api-token-here'
$env:DT_ENV_URL='https://<tenantID>.live.dynatrace.com'
python enable_codemodules.py
Usage

## Basic Execution

Once configured, simply run:
python enable_codemodules.py
Expected Output

Using Dynatrace environment: https://<tenantID>.live.dynatrace.com
API Token: **********XXXX
--------------------------------------------------
Found 2 hosts in DISCOVERY or FOUNDATION mode.
Enabled CodeModule injection on host: HOST-<ID>
Enabled CodeModule injection on host: HOST-<ID>
