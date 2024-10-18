params=("i_vel","f_vel","acc","dis","time")

def user_input():
    param_values=[]
    for param in params:
       try:
          param_values.append(float(input(f"enter {param} ")))
       except ValueError:
          param_values.append("unknown")
    return param_values

param_values=user_input()

def solvable(param_values):
  return param_values.count("unknown")<=2



solvable=solvable(param_values)
def sort():
   to_find=[]
   given=[]
   for i,param_value in enumerate(param_values):
      if param_value=="unknown":
         to_find.append(params[i])
      else:
         given.append(params[i])
   return to_find,given
to_find,given=sort()

i_vel,f_vel,acc,dis,time=param_values[0],param_values[1],param_values[2],param_values[3],param_values[4]

def solve_i_vel(given):
    if "f_vel" and "acc" and "time" in given:
         var=f_vel-acc*time
    elif "f_vel" and "acc" and "dis" in given:
         var=((f_vel)**2-2*acc*dis)**0.5
    elif "acc" and "dis" and "time" in given:
         var=(dis-0.5*acc*time**2)/time
    elif "f_vel" and "dis" and "time" in given:
         var=(2*dis-f_vel*time)/time 
    else:
        raise ValueError("cannot solve")
    return var

def solve_f_vel(given):
    if "i_vel" and "acc" and "time"in given:
         var=i_vel+acc*time
    elif "i_vel" and "acc" and "dis" in given:
         var=((i_vel)**2+2*acc*dis)**0.5
    elif "i_vel"and "dis" and "time" in given:
         var=(2*dis-i_vel*time)/time
    elif "acc" and "dis" and "time" in given:
         var=(dis+0.5*acc*time**2)/time
    else:
        raise ValueError("cannot solve")
    return var

def solve_acc(given):
    if "i_vel" and "f_vel" and "time" in given:
         var=(f_vel-i_vel)/time
    elif "i_vel" and "dis" and "time" in given:
         var=2*(dis-i_vel*time)/time**2
    elif "i_vel" and "f_vel" and "dis" in given:
         var=(f_vel**2-i_vel**2)/(2*dis)
    elif "f_vel" and "dis" and "time" in given:
         var=2*(f_vel*time-dis)/time**2
    else:
        raise ValueError("cannot solve")
    return var

def solve_dis(given):
    if "i_vel" and "acc" and "time" in given:
         var=i_vel*time+0.5*acc*time**2
    elif "i_vel" and "acc" and "f_vel" in given:
         var=((f_vel)**2-(i_vel)**2)/(2*acc)
    elif "i_vel" and "f_vel" and "time" in given:
         var=(i_vel+f_vel)/2*time
    elif "acc" and "f_vel" and "time" in given:
         var=f_vel*time-0.5*acc*time**2
    else:
        raise ValueError("cannot solve")
    return var

def solve_time(given):
    if "i_vel" and "acc" and "f_vel" in given:
         var=(f_vel-i_vel)/acc
    elif "i_vel" and "acc" and "dis" in given:
         var=(-i_vel+(i_vel**2-2*acc*dis)**0.5)/acc
    elif "i_vel" and "f_vel" and "dis" in given:
         var=2*dis/(i_vel+f_vel)
    elif "acc" and "f_vel" and "dis" in given:
         var=(f_vel-(f_vel**2-2*acc*dis)**0.5)/acc
    else:
        raise ValueError("cannot solve")
    return var

functions=[solve_i_vel,solve_f_vel,solve_acc,solve_dis,solve_time]
operations=dict(zip(params,functions))


def solve(param_values):
    solved_param_values=[]
    for i,param in enumerate(params):
        if param in to_find:
            try:
                solved_param_value=operations[param](given)
                solved_param_values.append(solved_param_value)
            except ValueError:
                solved_param_values.append("unknown")
        else:
            solved_param_values.append(param_values[params.index(param)])
    return solved_param_values

         

def main():
   if solvable:
      solved_param_values=solve(param_values)
      solution=dict(zip(params,solved_param_values))
      print(solution)
   else:
      print("invalid response")

main()







