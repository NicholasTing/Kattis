import math
data_list = input()

while data_list != "":
   
    data_list = data_list.split(" ")
    names = []
    digits = []
    for data in data_list:
        if(data.isalpha()):
            names.append(data)
        
        else:
            digits.append(float(data))
        
    names = ' '.join(names)
    print(str(sum(digits)/len(digits)) + " " + names)

    try:
        data_list = input()
    except:
        break