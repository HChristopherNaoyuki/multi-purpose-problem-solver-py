# Multi-Purpose Problem Solver

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Problem Types](#problem-types)
- [Code Structure](#code-structure)
- [Disclaimer](#disclaimer)

## Overview

The Multi-Purpose Problem Solver is a comprehensive Python application designed 
to solve various coding challenges and mathematical problems. This versatile 
tool provides solutions for sports calculations, game rules, health assessments, 
and basic arithmetic operations through an intuitive menu-driven interface.

## Features

- **Sports Score Calculation**: Calculate final scores based on time remaining and current score
- **Win Condition Checker**: Determine if numbers meet specific win conditions
- **Lucky Calculation**: Check mathematical combinations for lucky outcomes
- **Height Safety Assessment**: Evaluate height safety thresholds
- **Even/Odd Determination**: Simple number classification
- **Obesity Level Calculator**: Two methods for health assessment
- **Basic Arithmetic**: Simple addition operations
- **User-Friendly Interface**: Interactive menu system with clear prompts

## Installation

### Prerequisites
- Python 3.6 or higher
- Git (for cloning the repository)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HChristopherNaoyuki/multi-purpose-problem-solver-py.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd multi-purpose-problem-solver-py
   ```

3. **Run the application**:
   ```bash
   python multi_purpose_problem_solver_py.py
   ```

## Usage

### Running the Application

1. Execute the Python script:
   ```bash
   python multi_purpose_problem_solver_py.py
   ```

2. Follow the interactive menu prompts:
   - Select options 1-8 to access different problem solvers
   - Choose option 9 to exit the application
   - Follow specific input formats for each problem type

### Example Usage

```python
# Sample interaction with the sports score calculator
Enter time and score (e.g., '45 2'): 45 2
# Output: Calculated final score
```

## Problem Types

### 1. Sports Score Calculation
- **Purpose**: Calculate final scores in sports games
- **Input**: Time remaining and current score
- **Logic**: Awards points every 5 minutes with special handling for time multiples

### 2. Win Condition Checker
- **Purpose**: Determine if a number meets win conditions
- **Conditions**: 
  - Numbers between 50-70 (inclusive)
  - Numbers divisible by 6
- **Output**: "win" or "lose"

### 3. Lucky Calculation
- **Purpose**: Check if (a - b + c) is divisible by 10
- **Input**: Three integers
- **Output**: "Lucky" or "So-so"

### 4. Height Safety Check
- **Purpose**: Verify if heights meet safety standards
- **Threshold**: All heights must be above 170
- **Output**: "CRASH" or "PASS"

### 5. Even/Odd Check
- **Purpose**: Classify numbers as even or odd
- **Method**: Modulo 2 operation
- **Output**: "even" or "odd"

### 6. Simple Obesity Calculator
- **Formula**: Standard weight = (height - 100) × 0.9
- **Categories**: Normal, Overweight, Obese
- **Input**: Height and weight

### 7. Detailed Obesity Calculator
- **Multiple Formulas**: Different calculations based on height ranges
- **Height Ranges**: Under 150cm, 150-159cm, 160cm+
- **Comprehensive Assessment**

### 8. Addition Calculator
- **Purpose**: Basic two-number addition
- **Input**: Two integers
- **Output**: Sum of inputs

## Code Structure

```
multi-purpose-problem-solver-py/
├── multi_purpose_problem_solver_py.py
├── README.md
└── media/
    └── documentation/
```

### Main Components

- **ProblemSolver Class**: Core class containing all problem-solving methods
- **Menu System**: Interactive user interface
- **Input Validation**: Error handling for user inputs
- **Modular Design**: Separate methods for each problem type

### Key Methods

- `calculate_sports_score()`: Sports scoring logic
- `check_win_condition()`: Win/lose determination
- `check_lucky_calculation()`: Mathematical luck assessment
- `check_height_safety()`: Height threshold checking
- `calculate_obesity_level_simple()`: Basic health assessment
- `calculate_obesity_level_detailed()`: Advanced health assessment

## Disclaimer

### Software Usage
UNDER NO CIRCUMSTANCES SHOULD IMAGES OR EMOJIS BE INCLUDED DIRECTLY 
IN THE README FILE. ALL VISUAL MEDIA, INCLUDING SCREENSHOTS AND IMAGES 
OF THE APPLICATION, MUST BE STORED IN A DEDICATED FOLDER WITHIN THE 
PROJECT DIRECTORY. THIS FOLDER SHOULD BE CLEARLY STRUCTURED AND NAMED 
ACCORDINGLY TO INDICATE THAT IT CONTAINS ALL VISUAL CONTENT RELATED TO 
THE APPLICATION (FOR EXAMPLE, A FOLDER NAMED IMAGES, SCREENSHOTS, OR MEDIA).

### Liability Notice
I AM NOT LIABLE OR RESPONSIBLE FOR ANY MALFUNCTIONS, DEFECTS, OR ISSUES THAT 
MAY OCCUR AS A RESULT OF COPYING, MODIFYING, OR USING THIS SOFTWARE. IF YOU 
ENCOUNTER ANY PROBLEMS OR ERRORS, PLEASE DO NOT ATTEMPT TO FIX THEM SILENTLY 
OR OUTSIDE THE PROJECT. INSTEAD, KINDLY SUBMIT A PULL REQUEST OR OPEN AN ISSUE 
ON THE CORRESPONDING GITHUB REPOSITORY, SO THAT IT CAN BE ADDRESSED APPROPRIATELY 
BY THE MAINTAINERS OR CONTRIBUTORS.

### Important Notes
- This software is provided "as is" without warranty of any kind
- Users assume all responsibility for testing and validation
- Always backup your data before using new software
- The maintainers are not responsible for data loss or system issues
- Commercial use requires additional verification and testing

---
