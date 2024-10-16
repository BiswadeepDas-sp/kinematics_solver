def input_params():
    param_values=[]
    for param in params:
        try:
            param_value=float(input(f"enter {param} = "))
        except:
            param_value="unknown"
        param_values.append(param_value)
    return param_values

def solvable():
    if param_values.count("unknown")>2:
     not_solvable=True
     return not_solvable
    
def to_find():
     to_find=[]
     for i,param_value in enumerate(param_values):
         if param_value=="unknown":
            to_find.append(params[i])
     return to_find


def solve_i_vel():
    try:
        var=f_vel-acc*time
    except:
        try:
            var=((f_vel)**2-2*acc*dis)**0.5
        except:
            try:
                var=(dis-0.5*acc*time**2)/time
            except:
                var=(2*dis-f_vel*time)/time

    return var

def solve_f_vel():
    try:
        var=i_vel+acc*time
    except:
        try:
            var=((i_vel)**2+2*acc*dis)**0.5
        except:
            var=(2*dis-f_vel*time)/time
    
    return var

def solve_acc():
    try:
        var=(f_vel-i_vel)/time
    except:
        try:
            var=(f_vel**2-i_vel**2)/(2*dis)
        except:
            var=2*(dis-i_vel*time)/time**2
    return var

def solve_dis():
    try:
        var=(f_vel**2-i_vel**2)/(2*acc)
    except:
        try:
            var=i_vel*time+0.5*acc*time**2
        except:
            var=(i_vel+f_vel)/2*time
    return var

def solve_time():
    try:
        var=(f_vel-i_vel)/acc
    except:
        try: 
            var =((-i_vel)+((i_vel**2+2*acc*dis))**0.5)/acc
        except:
            var=2*dis/(i_vel+f_vel)
    return var

def solve(param_values):
    if "i_vel" in to_find:
        try:
             i_vel=solve_i_vel()

        except:
            i_vel=str("cannot solve")
    else:
        i_vel=param_values[0]

    if "f_vel" in to_find:
        try:
             f_vel=solve_f_vel()

        except:
            f_vel=str("cannot solve")
    else:
        f_vel=param_values[1]
    if "acc" in to_find:
        try:
             acc=solve_acc()

        except:
            acc=str("cannot solve")
    else:
        acc=param_values[2]
    if "dis" in to_find:
        try:
             dis=solve_dis()

        except:
            dis=str("cannot solve")
    else:
        dis=param_values[3]
    if "time" in to_find:
        try:
            time= solve_time()

        except:
            time=str("cannot solve")
    else:
        time=param_values[4]
    solved_param_values=[i_vel,f_vel,acc,dis,time]
    return solved_param_values
            
def main():
    if not_solvable:
        print("invalid response")
    else:
        print(f"to find {to_find}")

        print(f"we know {combined}")

        print(f"solution is {solution}")

params=["i_vel","f_vel","acc","dis","time"]
param_values=input_params()
#print(params)
#print(param_values)
not_solvable=solvable()
to_find=to_find()
i_vel,f_vel,acc,dis,time=param_values[0],param_values[1],param_values[2],param_values[3],param_values[4] #assign variables
combined=dict(zip(params,param_values))
solved_param_values=solve(param_values)
solution=dict(zip(params,solved_param_values))
main()








