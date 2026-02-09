## Local Development on Mac Mini

### Current Working Environment

- Operating System: macOS
- Python version: 3.12 (installed via Homebrew)
- Virtual environment: `venv/` in project root
- Main packages installed:
  - numpy
  - opencv-python (full version – GUI support enabled)
  - pyserial
  - pillow
  - matplotlib
  - scipy
  - tqdm
  - requests

### USB Camera Status

- Physical USB camera connected and visible to macOS
- OpenCV camera access tested locally
- Current focus: finding correct camera index and confirming frame capture

### Recommended commands

```bash
cd ~/projects/robot1
source venv/bin/activate
python camera_test.py          # or your current test script