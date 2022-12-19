from functions.get_time import get_time

def log_msg(func_name, l):
    if type(func_name) != str or type(l) != str:
        return -1
    timev = get_time()
    print("### LOG > " + timev + " > " + func_name + " : " + l)
    return 0

def err_msg(func_name, l1, l2):
    if type(func_name) != str or type(l1) != str or type(l2) != str:
        return -1
    timev = get_time()
    print("### ERROR > " + timev + " > " + func_name + " : " + l1)
    print("\t\tHINT : " + l2)
    return 0