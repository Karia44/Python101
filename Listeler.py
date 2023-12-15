# Listeler mutable
# Stringle immutable
# 1. Lİste Oluşturma
liste1=[1,2,3,4,5]
print(liste1)
print(type(liste1))
liste2 = [1,"Hülya",True,2.4567,[1,2,3,4]]
print(liste2)
liste = []
print(liste)
liste = [1,23,45,6,7,3,4]
print(liste[len(liste)-1])
print(liste[2:4])
print(len(liste))
s="Merhaba"
lst=list(s)
print(lst)

liste1 = [0,1,2,3]
liste1 = liste1+["Nova"]
print(liste1)

liste1= [1,2,3]
liste1.append(4)
print(liste1)

#pop metodu
liste1= ["Hülya","Mehmet","Ahmet","Sude"]
# print(liste1.pop())
# print(liste1)

#sort metodu
# liste1.sort()
# print(liste1)

liste2 = [5,2,6,3,8,2,9]
liste2.sort(reverse=True)
print(liste2)
# 2. Indexleme ve Parçalama