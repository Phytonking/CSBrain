import sqlite3
import re
import data



def writing(table, columns, information):
    try:
        f = open(f"{table}.txt", "x")
    except FileExistsError:
        f = open(f"{table}.txt", "w")

    cols_row = ""
    count_tracker = 0
    for v in columns:
        for x in v:
            if count_tracker == len(columns) - 1:
                cols_row += f"{x}"
                break
            else:    
                cols_row += f"{x}<>"
                break
        count_tracker += 1
    
    f.write(f"{cols_row}\n")
    for y in information:
        count_tracker = 0 
        row = ""
        for h in y:
            if count_tracker == len(y) - 1:
                row += f"{h}"
                break
            else:    
                row += f"{h}<>"
            count_tracker += 1
        f.write(f"{row}\n")    
        
    f.close()
    return f"{table}.txt"
        
def convertsql(file, table, sqlcols=None, requirments=None):
   connection = sqlite3.connect(file)
   crsr = connection.cursor() 
   fxc = re.split(".", file)
   if sqlcols != None or requirments != None:
       if requirments != None:
           crsr.execute(f"SELECT {sqlcols} FROM {table} WHERE {requirments}")
       else:   
        crsr.execute(f"SELECT {sqlcols} FROM {table}")
   else:     
        crsr.execute(f"SELECT * FROM {table}")
   ans = crsr.fetchall()
   cols_name = connection.cursor()
   cols_name.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{table}');")
   cols = cols_name.fetchall()
   if len(ans) == 0:
       return False
   else:
      x = writing(table, cols, ans) 
      return x