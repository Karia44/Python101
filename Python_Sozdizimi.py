# Print fonksiyon ve formatlama
a= "18"
b= "24"
print(int(a+b))

print("Matematik : ", 85,"Türkçe :", 70)
#\n karakter
print("Merhaba,\nBu dilekçeyi mudurlugunuze yaziyorum.\nBen Hulya")

print("Ocak\tMart\tSubat")
print("Temmuz\tAgustos\tEylul")

# type() fonksiyonu
print(type(8))
print(type("Merhaba"))

# sep parametresi
print("Hülya","YILDIZ")
print("15","12","2023", sep=("/"))
print(*"Nova Academy")
print(*"Nova Academy", sep=("*"))

# format fonksiyonu
string = "{}.{}.{}.{}.".format("T","B","M","M")
print(string)

a = 5
b = 10
print("{} + {} = {}" dir. Sonucumuz {}'dir.format(a,b,a+b)')