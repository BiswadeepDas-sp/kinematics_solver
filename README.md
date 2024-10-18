# README: Kinematic Equation Solver

## Overview
This program is designed to solve for any unknown value in the kinematic equations involving five key variables:

- Initial velocity (`i_vel`)
- Final velocity (`f_vel`)
- Acceleration (`acc`)
- Displacement (`dis`)
- Time (`time`)

It prompts the user to input known values for the kinematic parameters and determines the unknowns using appropriate kinematic equations. The solver ensures that the problem is solvable and provides solutions for the missing values.

## Features
- **User-Friendly Interface:** Prompts the user to enter the known parameters and automatically identifies the missing ones.
- **Equation Solving:** Uses the appropriate kinematic equation to solve for missing values based on the known ones.
- **Error Handling:** In case of invalid input or insufficient data, it returns an "invalid response."
- **Flexible Input:** The user can input any combination of known parameters, as long as there are at least three known values.

## Requirements
- **Python 3.x**

## How to Run the Program

### Step 1: Prepare Your Python Environment
Ensure that Python 3.x is installed on your machine. You can download it from the official website: [Python.org](https://www.python.org/).

### Step 2: Run the Program
1. Copy the provided Python code into a `.py` file (e.g., `kinematic_solver.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script by typing:

   ```bash
   python kinematic_solver.py
   ```

### Step 3: Input Known Values
When prompted, enter the known values for the following parameters:

- **Initial velocity** (`i_vel`): The velocity at the starting point (m/s).
- **Final velocity** (`f_vel`): The velocity at the end point (m/s).
- **Acceleration** (`acc`): The rate of change of velocity (m/s²).
- **Displacement** (`dis`): The distance traveled (m).
- **Time** (`time`): The duration of motion (s).

For any unknown parameter, enter `unknown` when prompted.

### Step 4: Receive Results
The program will automatically calculate the unknown parameters and display the results in a dictionary format, like so:

```python
{
  "i_vel": 10.0,
  "f_vel": 20.0,
  "acc": 5.0,
  "dis": 50.0,
  "time": 5.0
}
```

If the problem is unsolvable (i.e., fewer than three values are provided), the program will display:

```
invalid response
```

## How the Solver Works

1. **Input Handling:** The user provides values for the five parameters. Any missing value should be entered as "unknown".
2. **Validation:** The program checks whether at least three values are provided to make the problem solvable.
3. **Equation Selection:** Based on the provided values, the solver selects the appropriate kinematic equation to compute the missing parameters.
4. **Calculation:** Using the selected equations, the program computes the unknown values.
5. **Output:** The program outputs the solved values for all parameters.

### Kinematic Equations Used
The program uses the following kinematic equations to solve for the unknowns:

1. **Equation 1:** \( v_f = v_i + a \cdot t \)
2. **Equation 2:** \( v_f^2 = v_i^2 + 2 \cdot a \cdot d \)
3. **Equation 3:** \( d = v_i \cdot t + \frac{1}{2} \cdot a \cdot t^2 \)
4. **Equation 4:** \( d = \frac{(v_i + v_f)}{2} \cdot t \)
5. **Equation 5:** \( t = \frac{v_f - v_i}{a} \)

Each equation corresponds to a specific combination of known variables, and the program dynamically selects the appropriate one based on the input.

## Error Handling
- **Invalid Input:** If the user enters a non-numeric value when a numeric value is expected, the program will handle the exception and mark that parameter as "unknown."
- **Unsolvable Equations:** If fewer than three parameters are provided, the program will output "invalid response."
  
## Example
### Example 1: Solving for Final Velocity

**Input:**
```
enter i_vel: 10
enter f_vel: unknown
enter acc: 2
enter dis: 50
enter time: unknown
```

**Output:**
```
{'i_vel': 10.0, 'f_vel': 20.0, 'acc': 2.0, 'dis': 50.0, 'time': 5.0}
```

### Example 2: Insufficient Data

**Input:**
```
enter i_vel: 10
enter f_vel: unknown
enter acc: unknown
enter dis: unknown
enter time: unknown
```

**Output:**
```
invalid response
```

## Conclusion
This program simplifies solving kinematic equations by automating the process of determining the unknown values based on the given inputs. It is a useful tool for students, engineers, and anyone working with basic motion problems in physics.

## License
This program is provided under the MIT License. You can freely use, modify, and distribute it.
