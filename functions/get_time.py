import time

def get_time(dateb=True, timeb=True):
    if (type(dateb) != type(timeb) or type(timeb) != bool):
        return "#Err"
    timecur = time.localtime()
    finalstr = ""
    if (dateb == True):
        finalstr += str(timecur.tm_mday) + "/" + \
            str(timecur.tm_mon) + "/" + str(timecur.tm_year)
    if (dateb == timeb):
        finalstr += " "
    if (timeb == True):
        finalstr += str(timecur.tm_hour) + ":" + str(timecur.tm_min)
    return finalstr
