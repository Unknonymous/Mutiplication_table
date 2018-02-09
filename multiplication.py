def multi(y):  
    a = y
    row = []
    i = 0
    for i in range (0, 12):
        row.append(i)
        row[i] = a
        a += y
    return row
# multi(), above,  sets the values of each row and returns the list for use in ply()

# ply(), below, increments the value passed into multi and prints each line as a tuple to build the table
def ply(x):    
    w = 0
    line = []
    for w in range (0, 13):
        if w == 0 :
            line = multi(x)
        else:
            line = multi(w * x) 
        print (w, line)


ply(1)  

#passing a 1 into ply() returns a printed standard multiplication table
#passing a different number (x) has the effect of using that number as a multiplier for the values of the table.
#this results in a table ranging from x to 144 * x