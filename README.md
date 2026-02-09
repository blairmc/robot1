# robot1 – Robotic Weeder

An autonomous robotic system designed to detect and mechanically remove weeds.

## Current Status (as of February 2026)

- Local development environment fully set up on Mac Mini
- Python virtual environment created (Python 3.12)
- Core dependencies installed via `requirements.txt` (numpy, opencv-python, pyserial, pillow, matplotlib, etc.)
- USB camera successfully connected and recognized by the operating system
- Initial OpenCV-based camera access scripts tested **locally** (camera opening and frame capture in progress)
- Working locally with periodic commits and pushes to GitHub

## Development Environment

- Local machine: Mac Mini
- IDE: Visual Studio Code
- Version control: Git + GitHub[](https://github.com/blairmc/robot1)
- Virtual environment: `venv/` (activated with `source venv/bin/activate`)

## Next Major Milestones

- Confirm reliable USB camera frame capture and live preview
- Implement basic plant/weed detection (color-based or simple ML)
- Establish serial communication with Arduino controller
- Design and document initial mechanical/weeding subsystem

See [docs/progress.md](docs/progress.md) for more detailed progress tracking.