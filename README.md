# OverTheWire: Bandit Level Scripts

This repository contains scripts developed while solving specific levels of the OverTheWire Bandit wargame. Each script is tailored to overcome a unique challenge presented in the game, demonstrating practical applications of bash scripting and Python programming in security contexts.

## Scripts Overview

- **Level 23 - level23_script.sh**: A bash script designed to automate the retrieval of the password for the next level by exploiting a scheduled cron job's behavior.

- **Level 24 - level24_bash_script.sh**: Facilitates the discovery of a 4-digit PIN by brute-forcing a network service listening on localhost. It sequentially submits PIN guesses and interprets responses to identify the correct PIN.

- **Level 24 - level24_python_script.py**: An alternative approach to the Level 24 Bash Script, implemented in Python. It serves the same purpose but showcases how similar tasks can be accomplished using different programming languages and paradigms.

## Usage

### Level 23 Script

1. Ensure you have write permissions to `/tmp/tmp.5ZrLHlTNTB/`.
2. Execute the script: `./level23_script.sh`

### Level 24 Bash Script

1. Replace `BANDIT24_PASS` with the actual password for bandit24.
2. Run the script: `./level24_bash_script.sh`

### Level 24 Python Script

1. Ensure Python 3 is installed on your system.
2. Replace `bandit24_password` with the actual password for bandit24.
3. Execute the script: `python3 level24_python_script.py`

## Dependencies

- Bash interpreter (for bash scripts)
- Python 3.x (for Python scripts)

## Disclaimer

The scripts are provided for educational purposes only. Do not use them on any system without explicit permission from the system owner.

## Acknowledgments

Thanks to the OverTheWire community for creating engaging and educational security challenges.
