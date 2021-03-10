import os
path = os.getcwd()
print("Текущая директория: ",path)
a = input("Изменить? д/н\n").lower()
while((a[0] != 'д') and (a[0] != 'н')):
    a = input("Изменить? д/н\n").lower()
    if (a[0] == 'д'):
        tmp = input()
        while(not os.path.exists(tmp)):
            tmp = input("Неправильный ввод\n")
        path = tmp     
lst = os.listdir(path)
for i in lst:
    a = i.split('.')
    if len(a) < 2:
        continue
    if a[1] == "jpg" and not os.path.exists("Picters"):
        os.mkdir('Picters')
    elif a[1] == "webm" and not os.path.exists("Videos"):
        os.mkdir('Videos')    
for i in lst:
    a = i.split('.')
    if len(a) < 2:
        continue
    if a[1] == "jpg":
        os.replace(i,'Picters/'+i)
    elif a[1] == "webm":
        os.replace(i,'Videos/'+i)
print("Все файлы были перемещены по папкам")        
