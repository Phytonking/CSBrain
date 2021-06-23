import numpy

def mean(list_of_values):
    for x in list_of_values:
        if x == str:
            return False

    y = 0
    numbers = 0
    for add in list_of_values:
        y += int(add)
        numbers += 1

    return y / numbers    



def median(list_of_values):
    return numpy.median(list_of_values)     


def range(list_of_values):
    highestvalue = 0
    lowestvalue = 0
    for k in list_of_values:
        if highestvalue == 0:
            highestvalue = k
        if lowestvalue == 0:
            lowestvalue = k    
        elif k > highestvalue:
            highestvalue = k
        elif k < lowestvalue:
            lowestvalue = k

    return float(highestvalue) - float(lowestvalue)            


def mode(list_of_values):
    numbers = []

    for k in list_of_values: 
        numberfound = False
        for j in numbers:
            if j.get("number") == k:
                j.update({"count": int(j.get("count")+ 1)})
                numberfound = True
                break
                    
        if numberfound == False:
            numbers.append({"number": k, "count": 0})    

    mode = None
    for x in numbers:
        if mode == None:
            mode = x
        if x.get("count") > mode.get("count"):
           mode = x
    
    return mode.get("number")