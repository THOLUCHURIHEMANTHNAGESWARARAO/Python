from datetime import datetime
name=input("Enter your name:")
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 80/liter
Paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 85/kg
'''
# declaration
price=0
price_list=[]
total_price=0
final_price=0
ilist=[]
qlist=[]
plist=[]

# Rates for items
items={'Rice':20,'Sugar':30,'Salt':20,'Oil':80,'Paneer':110,'Maggi':50,'Boost':90,'Colgate':85}
option=int(input("Enter the List of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    elif inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            price_list.append((item,quantity,price))
            total_price+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(total_price*5)/100
            final_amount=gst+total_price
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered wrong number")
    inp=input("Can i bill the items yes or no:")
    if inp=='yes':
        pass
        if final_amount!=0:
            print(25*"=","Hemanth super market",25*"=")
            print(28*" ","Wanaparthy")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',8*" ",'price')
            for i in range(len(price_list)):
                print(i,10*' ',ilist[i],10*' ',qlist[i],15*" ",plist[i])
            print(75*"-")
            print(50*" ",'total_amount:','Rs',total_price)
            print("gst_amount:",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'final_amount:','Rs',final_amount)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(75*"-")
   
                   
        
    
