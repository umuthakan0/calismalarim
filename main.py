
uyeler = {"üye":["ali","fatma","ayse"]}
uyeler["üye"].append("turgut")
print(uyeler["üye"])
uyeler["üye"].remove("turgut")
print(uyeler["üye"])
import time

print("lutfen saati ayarlayın")
second=int(input("saniyeyi girin: "))
minute=int(input("dakikayı girin: "))
hour=int(input("saati girin: "))

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
    print("saat:",hour,".",minute,".",second)

