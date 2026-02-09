# Setup Guide for robot1 Development

## Prerequisites
- **Hardware**: Mac Mini for local development.
- **Software**: GitHub account with access to Codespaces.
- **Repository**: Cloned from https://github.com/blairmc/robot1.

## Setting Up GitHub Codespaces
1. Navigate to the repository on GitHub: https://github.com/blairmc/robot1.
2. Click "Code" > "Open with Codespaces" > "Create new codespace".
3. Wait for the environment to initialize (includes VS Code interface).
4. Install extensions if needed (e.g., Python, Arduino).

## Local Development on Mac Mini
- Install Git: `brew install git` (if not already present via Homebrew).
- Clone the repo: `git clone https://github.com/blairmc/robot1.git`.
- Open in VS Code or preferred IDE.
- For Arduino: Download Arduino IDE from https://www.arduino.cc/en/software.

## Installing Dependencies
- Python: Ensure Python 3.x is installed (`brew install python` on Mac).
- Create a virtual environment: `python -m venv venv` and activate it.
- Install libraries: `pip install opencv-python numpy` (expand as needed).

## Hardware Connection
- Connect Arduino via USB for programming.
- Jetson Nano setup: Follow NVIDIA documentation for initial boot and Python environment.

## Testing
- Run sample Python scripts in Codespaces terminal.
- Upload Arduino sketches and monitor serial output.

## Troubleshooting
- If Codespaces fails to load: Check GitHub status or recreate the codespace.
- Dependency issues: Refer to Python documentation for platform-specific fixes on macOS.