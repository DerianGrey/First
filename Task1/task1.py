k = 273
c = int(input("Введите градусы Цельсия: "))
result_k = c + k
result_f = c * 9/5 +32
print ("Кельвины: ", result_k)
print ("Фаренгейты: ", result_f)

import json
filename = "data.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

temp = {
    'K': result_k,
    'F': result_f
    }
json.dump(temp, myfile)
myfile.close()

