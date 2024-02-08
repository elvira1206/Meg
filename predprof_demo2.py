f=open('students.csv')
z1,z2,z3,z4,z5=f.readline().split(',') #считываем строку с заголовками
tab=[] #это будет двухмерный список со всеми данными
fio=[] #ФИО через пробел, а удобно работать по отдельности

#создаем двухмерный список данных из файла:
for i in range(500):
    d1,d2,d3,d4,d5=f.readline().split(',') #прочитали строку из файла, разбили
    fio=d2.split() # разбили ФИО на фамилию, имя, отчество отдельно
    if d5=='None\n': #обрабатываем строки с ошибкой 
        d5='0' 
    # создаем двухмерный список с исходными данными
    tab.append([d1,fio[0],fio[1],fio[2],d3,d4,int(d5)]) 

#Сортируем список методом вставки (по убыванию)
for i in range(1,500):
    j=i
    while j>0 and float(tab[j][6])>float(tab[j-1][6]):
        tab[j],tab[j-1]=tab[j-1],tab[j]
        j=j-1
#выводим первые 3 элемента списка, если они из 10 класса
n=0
for i in range(500):
    if '10' in tab[i][5]:
        n+=1
        print(f'{n} место: {tab[i][2][0]}.{tab[i][1]}')
        if n==3: break
