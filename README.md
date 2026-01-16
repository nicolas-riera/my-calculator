# Python calculator

## Description

This is a Python calculator that can handle multiple calculations at once while respecting priorities.


## Installation (Windows only)

Download the latest release of the executable here: https://github.com/nicolas-riera/my-calculator/releases/latest

After downloading, simply run `my-calculator_[version].exe` to start the application.

## Usage

Launch the executable and use your keyboard to enter numbers and operators via the interactive menu. You can navigate through options and perform calculations step by step.

## Features

- Handles multiple calculations simultaneously
- Respects operator precedence
- Includes a calculation history to track past operations
- Allows continuing a calculation using a previous result

## Run from source (Python)

### Prerequisites

Make sure you have installed:

- Python 3.10+
- Required packages:
  - colored : `pip install colored`
  - pyinstaller : `pip install pyinstaller`

### Clone the repository:

```
git clone https://github.com/nicolas-riera/my-calculator.git
cd my-calculator
```

### Run the program

Run the main script to start the calculator:

```
python main.py
```

## Build the executable

To create a standalone .exe file using PyInstaller, run:

```
pyinstaller main.py --onefile
```

The generated executable will be located in the dist/ folder.

## Authors

This project was created by [Nicolas](https://github.com/nicolas-riera), [Angelo](https://github.com/Angelo-Njarasoa) and [Axel](https://github.com/Axel-RODRIGUEZ).
