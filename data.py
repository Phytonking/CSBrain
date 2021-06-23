import csv
import re
import os

def read_file(file):
    if ".csv" in file:
        with open(file, newline='') as csvfile:
            spamreader = csv.DictReader(csvfile)
        return spamreader    
    elif ".tsv" in file:
        with open(file, newline='\t') as tsvfile:
            spamreader = csv.reader(tsvfile, delimiter=' ', quotechar='|')
        return spamreader




def store_knowledge(class_name, information):
    try:
        f = open(f"{class_name}.brain", "w")
    except FileNotFoundError:
        f = open(f"{class_name}.brain", "x")

    string = f"<{class_name}>\n"
    for v in information:
        string += f"\t{v}\n"

    string += f"</{class_name}>\n"
    f.write(string)
    f.close()

    return True

    






def search(file, action):
    f = read_file(file)
    if action == "":
        if ".csv" in file:
            return csv.reader(file)
        if ".txt" in file:
            t = open(file, "rt")
            tx = re.split("\n", t.read())
            return tx        
    kh = re.split(";", action) 
    if len(kh) == 2 and kh[1] == '':
        khs = re.split(":", kh[0])
    if len(kh) > 2:
       kh.pop(len(kh) - 1) 
       num_pos = 0
       temp = [] 
       for j in kh:  
           info = re.split(":", j)
           for k in info:
               temp.append(k)
       khs = temp         
    khs_count = len(khs)
    if ".csv" in file:
       data_rows = []
       product = {}
       rows_to_be_returned = []
       if khs_count == 2: 
            with open(file, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    rows = []
                    for row in reader:
                        data_rows = row
                        break
                    for row in reader:
                        rows.append(row)
                    data_row_num = 0
                    for obj in data_rows:
                        if khs[0] != obj:
                            data_row_num += 1
                        else:
                            for x in rows:
                                if x[data_row_num] == khs[1]:
                                    product = {}
                                    length = len(data_rows)
                                    for kj in range(length):
                                        product.update({f"{data_rows[kj]}": f"{x[kj]}"})
                                    rows_to_be_returned.append(product)
                                continue 
                        
       return rows_to_be_returned
                  

    elif ".txt" in file:
        f = open(file, "r")
        content = f.read()
        lines = len(re.split("\n", content))
        line = f.readlines()
        line_list = re.split("\n", content)
        data_rows = []
        rows_to_be_returned = []
        short_list = []
        for row in range(lines):
            data = re.split("<>", line_list[row])
            if data == '':
                continue
            if row == 0:
                #column names
                for x in data:
                    data_rows.append(x)
                continue
            if khs_count == 2:
                data_row_num = 0 # data row position
                for obj in data_rows:
                    if khs[0] != obj:
                        data_row_num += 1
                    else:
                        break 
                if data[data_row_num] == khs[1]:
                    product = {}
                    for kj in range(len(data_rows)):
                        product.update({f"{data_rows[kj]}": f"{data[kj]}"})
                    rows_to_be_returned.append(product)
                    continue 
                else:
                    continue                  

        return rows_to_be_returned             










    
        