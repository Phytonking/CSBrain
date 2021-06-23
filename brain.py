import sys
import math
import re
import data
import brain_math

def think(file=None,search=None):
    #checks if file exsists
    if file == None or search == None:
        return False
    
    #seperates the search parts
    search_div = re.split(";", search)
    extra_search = re.split(":",search_div[0])
    search_div.remove('')
    #print(search_div)   
    #searches the data
    x = data.search(file=file, action=search)
    if x == None or x == bool:
        return None
    data_rows = []
    for k in range(1):
        #print(x[k])
        for kn in x[k]:
            data_rows.append(kn)     
    #print(data_rows)
    
    features = []
    for row in data_rows:
        value = []
        for yn in x:
            value.append(yn[row])
        previous_val = None
        value_stays_the_same = False
        value_changes = False
        min_value = None
        max_value = None
        for v in value:
            if previous_val == None:
                previous_val = v
                min_value = v
                continue
            elif previous_val == v:
                value_stays_the_same = True
            elif v > previous_val and max_value == None:
                value_changes = True
                max_value = v
                #continue
            elif v < previous_val and min_value == None:
                value_changes = True
                min_value = v
                #continue
            elif v > previous_val and v > max_value:
                value_changes = True
                max_value = v
                #continue
            elif v < previous_val and v < min_value:
                min_value = v  
                #continue
        if extra_search[0] in row:
            continue    
        if value_stays_the_same == True:
            features.append(f"{row}:{v}")
        elif value_changes:
            try:
                int(min_value)
            except ValueError:
                features.append(f"{row}_minimum: VDOO")
            try:
                int(max_value)
            except ValueError:
                features.append(f"{row}_maximum: VDOO")
                continue
            if row != 'id' or row != 'Id':
                features.append(f"{row}_minimum:{min_value}")
                features.append(f"{row}_maximum:{max_value}")
                features.append(f"{row}_range:{brain_math.range([min_value,max_value])}")
                features.append(f"{row}_average: {brain_math.mean(value)}")
                features.append(f"{row}_most_frequent: {brain_math.mode(value)}")
                
    
    data.store_knowledge(re.sub('"', "", extra_search[1]), features)  
    return True     



    