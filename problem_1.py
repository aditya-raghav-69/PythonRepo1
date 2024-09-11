# printing tables from 2 to 20 in a separate file

# printing tables from 2 to 20 in a separate file

path = "C:/Users/pc/Desktop/GitDemo/PythonRepo1/tables.txt"

with open(path, "a+", encoding="utf-8") as f:
    for i in range(2,21):
        for  j in range(1,11):
            s = f"          {i}X{j}    =    {i*j}  \n "
            f.write(s)
        f.write('\n')
