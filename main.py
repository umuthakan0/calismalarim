import time

print("lutfen saati ayarlayın")
second=int(input("saniyeyi girin: "))
minute=int(input("dakikayı girin: "))
hour=int(input("saati girin: "))
day=int(input("günü giriniz: "))
month=int(input("ayı giriniz: "))
yıl=int(input("yılı giriniz: "))

while True:
    second+=1
    time.sleep(1)
    if second==60:
        minute+=1
        second=0
    elif minute==60:
        hour+=1
        minute=0
        second=0
    elif hour==24:
        day+=1
        minute = 0
        second = 0
        hour=0
    elif day==30:
        month+=1
        minute = 0
        second = 0
        hour = 0
        day==0
    elif month==12:
        yıl+=1
        minute = 0
        second = 0
        hour = 0
        month=0
    print("tarih: ",yıl,",",month,",",day,",",hour,".",minute,".",second)
