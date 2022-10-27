# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

data_1 = open('file_1.txt', 'r')
for line in data_1:
    print(line)

data_2 = open('file_2.txt', 'r')
for line in data_2:
    print(line)

def addpoly(p1,p2):
    i=0
    su=0
    j=0
    c=[]
    if len(p1)==0:
        #if p1 empty
        return p2
    if len(p2)==0:
        #if p2 is empty
        return p1
    while i<len(p1) and j<len(p2):
        if int(p1[i][1])==int(p2[j][1]):
            su=p1[i][0]+p2[j][0]
            if su !=0:
                c.append((su,p1[i][1]))
            i=i+1
            j=j+1
        elif p1[i][1]>p2[j][1]:
            c.append((p1[i]))
            i=i+1
        elif p1[i][1]<p2[j][1]:
            c.append((p2[j]))
            j=j+1
    if p1[i:]!=[]:
        for k in p1[i:]:
            c.append(k)
    if p2[j:]!=[]:
        for k in p2[j:]:
            c.append(k)
    return c  

print(addpoly(data_1,data_2))

data_1.close()
data_2.close()