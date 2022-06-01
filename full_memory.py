file = open('testfile.txt','w')
coef = 2048
size = input("GB or MB:::")
if size == "GB":
    coef*=1024
x = input(f"How much {size} you want to full?")
print("in process...")
for i in range(int(x)*coef):
    file.write("FROMfairestcreatureswedesireincrease,Thattherebybeauty'srosemightneverdie,Butastheripershouldbytimedecease,Histenderheirmightbearhismemory:Butthou,contractedtothineownbrighteyes,Feed'stthylight'stflamewithself-substantialfuel,Makingafaminewhereabundancelies,Thyselfthyfoe,tothysweetselftoocruel.Thouthatartnowtheworld'sfreshornamentAndonlyheraldtothegaudyspring,WithinthineownbudburiestthycontentAnd,tenderchurl,makestwasteinniggarding.Pitytheworld,orelsethisgluttonbe,Toeattheworld'sdue,bythegraveandthee!!!!!!!")
print("success")
file.close()
