#a= int(input())
#b= int(input())
#c=list(range(-32000, 32000))
#if a and b in c:
#    print(a+b)
#else: print("не верные числа")

#a = int(input())
#b = a // 60
#c = a % 60
#print(b)
#print(c)

#a=int(input())
#b=int(input())
#c=int(input())
#print((b*60+c+a)//60) 
#print((b*60+c+a)%60) 

#a=int(input())
#b=int(input())
#h=int(input())
#if a<=h<b:
#    print("Это нормально")
#elif a>h:
#    print("Недосып")
#else: print("Пересып")

def is_leap_year(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

year = int(input("Введите год: "))
if is_leap_year(year):
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")