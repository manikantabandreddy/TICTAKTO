print("Hi Sir/Madam")
print("PLEASE WELCOME TO THE INDIAN RESTURANT ")
print("please scane the QR code in mobile and plz order the food")
print("please select the food : (1)staters ,(2)veg,(3)non_veg,(4)biriyani")

def billing():
    d = input("cash/card: ")
    if d == "cash":
        e = int(input("give amount :"))
        p = (e-amount)
        print("REMAINING AMMOUNT = " + str(p))
    else:
        k = input("enter the pin")
        if len(k) == 4:
            print("transcation was completed sucessfully")
def respons():
    print("please wait your food is ready with in 15 mins sir\madam")
    input("give the respons : ")
    print("THANKING YOU SIR VISIT AGAIN .............")

staters = ["chicken", "mutton", "fish", "chilli chicken", "chicken wings", "kababs"]
veg = ["potato", "carrot", "veg manchuria", "palak panneer", "cashew", "panner"]
non_veg = ["chicken curry", "mutton curry", "fish curry","grill chicken"]
biriyani = ["chicken biryani", "mutton biryani", "fish biryani", "veg biryani", "panner bhiryani", "mushroom biryani"]

a = input("plz select the items : ")

if a == "staters":
    print("please select items in staters : ")
    print(staters)
    x = input("enter the stater : ")
    if x in staters:
        if x == "chicken":
            print("CHICKEN : 200  gst :10% total cost = 220")
            amount=220
        elif x == "mutton":
            print("MUTTON : 250  gst :10% total cost = 275")
            amount=275
        elif x == "fish":
            print("FISH : 210  gst :10% total cost = 221")
            amount=221
        elif x == "chilli chicken":
            print("CHILLI CHICKEN : 230  gst :10% total cost = 253")
            amount=253
        elif x == "chicken wings":
            print("CHICKEN WINGS : 250  gst :10% total cost = 275")
            amount=275
        billing()
        respons()
    else:
        print("please select the staters in menu")

elif a == "veg":
    print("please select the veg :")
    print(veg)
    y = input("enter the veg : ")
    if y in veg:
            if y == "potato":
                print("potato : 130 ,gst :10% total cost =143")
                amount=143
            elif y == "carrot":
                print("CARROT : 140 ,gst :10% total cost =154")
                amount=154
            elif y == "veg manchuria":
                print("VEG MANCHURIA : 180 ,gst :10% total cost =198")
                amount=198
            elif y == "panner":
                print("PANNER : 200 ,gst :10% total cost =220")
                amount=220
            elif y == "cashew":
                print("CASHEW : 180 ,gst :10% total cost =190")
                amount=190
            elif y == "palak panneer":
                print("PALLAK PANNER: 200 ,gst :10% total cost =220")
                amount=220
            billing()
            respons()
    else:
        print("please select the veg items in menu")

elif a == "non_veg":
    print("please select the non_veg :")
    print(non_veg)
    z = input("enter the non_veg : ")
    if z in non_veg:
        if z == "chicken curry":
            print("CHICKEN  CURRY: 230  gst :10% total cost = 250")
            amount=250
        elif z == "mutton":
            print("MUTTON CURRY : 250  gst :10% total cost = 275")
            amount=275
        elif z == "fish":
            print("FISH CURRY: 200  gst :10% total cost = 220")
            amount=200
        elif z == "chilli chicken":
            print("CHILLI CHICKEN : 230  gst :10% total cost = 253")
            amount=253
        billing()
        respons()
    else:
        print("please select the non_vegitems in menu")

elif a == "biriyani":
    print("please selsct the biriyani :")
    print(biriyani)
    w = input("enter the biryani :")
    if w in biriyani:
        if w == "chicken biryani":
            print("CHICKEN BIRYANI : 250 , GST : 10% , TOTAL = 275")
            amount=275
        elif w == "mutton biryani":
            print("MUTTON : 290 , GST : 10% , TOTAL = 329")
            amount=329
        elif w == "fish biryani":
            print("MUTTON : 290 , GST : 10% , TOTAL = 329")
            amount=329
        elif w == "veg biryani":
            print("VEG BIRYANI : 160 , GST : 10% , TOTAL = 176")
            amount=176
        elif w == "panner bhiryani":
            print("PANNER BHIRYANI: 220, GST : 10% , TOTAL = 244")
            amount=244
        elif w == "mushroom biryani":
            print("MUSHROOM BURYANI : 200, GST : 10% , TOTAL = 220")
            amount=220
        billing()
        respons()
    else:
        print("please select the biriyani in menu")

else:
    print("Sorry sir that iteam is not avalible at the current time...")
    print("please go through the MENUE CARD items..")
