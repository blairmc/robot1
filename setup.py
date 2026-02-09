"""
Setup script for robot_controller package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="robot_controller",
    version="0.1.0",
    author="Blair",
    description="Four-wheel robotic weed detector with GPS mapping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blairmc/robot1",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Robotics",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "robot-control=examples.manual_control:main",
            "robot-operate=examples.basic_operation:main",
            "robot-gps=examples.gps_mapping:main",
        ],
    },
)
