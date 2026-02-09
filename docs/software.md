# Software Architecture for robot1

## Overview
The software stack emphasizes simplicity and scalability, using Python for core logic and integrating visual processing libraries with AI capabilities.

## Programming Environment
- **Languages and Frameworks**:
  - Plain Python for primary development.
  - Visual libraries: OpenCV (for image processing), Pillow (for basic image handling), and potentially TensorFlow or PyTorch for ML models.
- **Development Tools**:
  - GitHub Codespaces for cloud-based editing and testing on Mac Mini.
  - Arduino IDE or PlatformIO for firmware on Arduino controllers.

## Key Modules
- **Low-Level Control**:
  - Arduino sketches for motor control (stepper motor stepping sequences) and sensor data acquisition.
- **High-Level Control**:
  - Python scripts on Jetson Nano for:
    - Camera input processing (USB camera and OpenMV integration).
    - Weed detection algorithms using computer vision.
    - Path planning and navigation.
- **AI Integration**:
  - LLM AI (e.g., via APIs like OpenAI or local models) for decision-making, such as classifying weeds or optimizing routes.

## Dependencies
- Python libraries: `opencv-python`, `numpy`, `requests` (for AI APIs), and others as needed.
- Install via `requirements.txt` (to be created in the root directory).

## Architecture Diagram
(To be added: A high-level diagram illustrating data flow from sensors to actuators.)

## Next Steps
- Initialize source code in `src/` directory.
- Develop initial prototypes for motor control and camera capture.