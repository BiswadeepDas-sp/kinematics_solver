params = ("i_vel", "f_vel", "acc", "dis", "time")

def user_input():
    param_values = []
    for param in params:
        try:
            value = input(f"Enter {param}: ")
            if value.lower() == "unknown":
                param_values.append("unknown")
            else:
                param_values.append(float(value))
        except ValueError:
            param_values.append("unknown")
    return param_values

param_values = user_input()

def solvable(param_values):
    return param_values.count("unknown") <= 2

is_solvable = solvable(param_values)

def sort():
    to_find = []
    given = []
    for i, param_value in enumerate(param_values):
        if param_value == "unknown":
            to_find.append(params[i])
        else:
            given.append(params[i])
    return to_find, given

to_find, given = sort()

i_vel, f_vel, acc, dis, time = param_values[0], param_values[1], param_values[2], param_values[3], param_values[4]

def solve_i_vel(given):
    if "f_vel" in given and "acc" in given and "time" in given:
        return f_vel - acc * time
    elif "f_vel" in given and "acc" in given and "dis" in given:
        return ((f_vel ** 2) - 2 * acc * dis) ** 0.5 if (f_vel ** 2) - 2 * acc * dis >= 0 else "unknown"
    elif "acc" in given and "dis" in given and "time" in given:
        return (dis - 0.5 * acc * time ** 2) / time
    elif "f_vel" in given and "dis" in given and "time" in given:
        return (2 * dis - f_vel * time) / time
    else:
        raise ValueError("Cannot solve for initial velocity with the given parameters.")

def solve_f_vel(given):
    if "i_vel" in given and "acc" in given and "time" in given:
        return i_vel + acc * time
    elif "i_vel" in given and "acc" in given and "dis" in given:
        return ((i_vel ** 2) + 2 * acc * dis) ** 0.5
    elif "i_vel" in given and "dis" in given and "time" in given:
        return (2 * dis - i_vel * time) / time
    elif "acc" in given and "dis" in given and "time" in given:
        return (dis + 0.5 * acc * time ** 2) / time
    else:
        raise ValueError("Cannot solve for final velocity with the given parameters.")

def solve_acc(given):
    if "i_vel" in given and "f_vel" in given and "time" in given:
        return (f_vel - i_vel) / time
    elif "i_vel" in given and "dis" in given and "time" in given:
        return 2 * (dis - i_vel * time) / time ** 2
    elif "i_vel" in given and "f_vel" in given and "dis" in given:
        return (f_vel ** 2 - i_vel ** 2) / (2 * dis)
    elif "f_vel" in given and "dis" in given and "time" in given:
        return 2 * (f_vel * time - dis) / time ** 2
    else:
        raise ValueError("Cannot solve for acceleration with the given parameters.")

def solve_dis(given):
    if "i_vel" in given and "acc" in given and "time" in given:
        return i_vel * time + 0.5 * acc * time ** 2
    elif "i_vel" in given and "acc" in given and "f_vel" in given:
        return ((f_vel ** 2) - (i_vel ** 2)) / (2 * acc)
    elif "i_vel" in given and "f_vel" in given and "time" in given:
        return (i_vel + f_vel) / 2 * time
    elif "acc" in given and "f_vel" in given and "time" in given:
        return f_vel * time - 0.5 * acc * time ** 2
    else:
        raise ValueError("Cannot solve for displacement with the given parameters.")

def solve_time(given):
    if "i_vel" in given and "acc" in given and "f_vel" in given:
        return (f_vel - i_vel) / acc
    elif "i_vel" in given and "acc" in given and "dis" in given:
        discriminant = i_vel ** 2 + 2 * acc * dis
        return (-i_vel + discriminant ** 0.5) / acc if discriminant >= 0 else "unknown"
    elif "i_vel" in given and "f_vel" in given and "dis" in given:
        return 2 * dis / (i_vel + f_vel)
    elif "acc" in given and "f_vel" in given and "dis" in given:
        discriminant = f_vel ** 2 - 2 * acc * dis
        return (f_vel - discriminant ** 0.5) / acc if discriminant >= 0 else "unknown"
    else:
        raise ValueError("Cannot solve for time with the given parameters.")

functions = [solve_i_vel, solve_f_vel, solve_acc, solve_dis, solve_time]
operations = dict(zip(params, functions))

def solve(param_values):
    solved_param_values = []
    for i, param in enumerate(params):
        if param in to_find:
            try:
                solved_param_value = operations[param](given)
                solved_param_values.append(solved_param_value)
            except ValueError:
                solved_param_values.append("unknown")
        else:
            solved_param_values.append(param_values[params.index(param)])
    return solved_param_values

def main():
    if is_solvable:
        solved_param_values = solve(param_values)
        solution = dict(zip(params, solved_param_values))
        print(solution)
    else:
        print("Invalid response: The problem cannot be solved with the given input.")

main()







