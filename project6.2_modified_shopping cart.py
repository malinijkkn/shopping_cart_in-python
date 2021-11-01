###S.MALINI
###27.11.2021
###Modified Shopping Cart project  in Python


items=['carrot','beans','onion','spinach']
quantity=['20kg','10kg','15kg','20']
price=['30','35','25','15']
total_payment=['0']
shop_item=[]
while True:
    print("------------------WELCOME TO SJMS SHOPPING MALL---------------------")
    user=['1.admin','2.user','3.exit']
    print(user[0])
    print(user[1])
    print(user[2])
    user=input("Enter the user type : ")
    if user=="1":
        print("you choice:")
        print("\n 1.Add item   2.Delete item "     "3.Update"         "4.Exit")
        choice=input("Enter the choice : ")
        if choice=="1":
            print( "Available Items ")
            print("1."+items[0].title())
            print("2."+items[1].title())
            print("3."+items[2].title())
            print("4."+items[3].title())
            print("\n")

            add_item=input("Enter the adding item : ")
            if add_item not in items or add_item in items:
                items.append(add_item)
                print(items)
                #insert_item = items.insert(add_item)
                #print(items)

            
            add_quantity=input("Enter the adding quantity of item : ")
            if add_quantity not in quantity or add_quantity in quantity:
                quantity.append(add_quantity)
                print(quantity)
                #print(quantity)

            add_price=input("Enter the adding price of  item : ")
            if add_price not in price or  add_price in price:
                price.append(add_price)
                print(price)    
                            
            else:
                print("The item is already exits.")

        if choice=='2':
            del_item=input("Enter the item to delete:")
            a=items.index(del_item)
            del items[a]
            del quantity[a]
            del price[a]
            print(items)
            print(quantity)
            print(price)

                

        else:
                print("Item is not in List")
        
        if choice =='3':
             print("\n 1.update quantity  2.update price  3.update quantity and price  4.Exit")
             Option=input("Enter the Option : ")
             if Option=="1":
                    item_update=input("Enter the Item Name : ")
                    quantity_update=input("Enter the quantity : ")
                    s=items.index(item_update)
                    quantity[s]=quantity_update
                    print(items)
                    print(quantity)
             if Option=="2":
                    item_update=input("Enter the Item Name : ")
                    price_update=input("Enter the price : ")
                    t=items.index(item_update)
                    price[t]=price_update
                    print(items)
                    print(price)
             if Option=="3":
                    item_update=input("Enter the Item Name : ")
                    quantity_update=input("Enter the quantity : ")
                    price_update=input("Enter the price : ")
                    s=items.index(str(item_update))
                    t=items.index(item_update)
                    quantity[s]=quantity_update
                    price[t]=price_update
                    print(items)
                    print(quantity)
                    print(price)
        if choice=='4':
            exit()        
  
    if user=="2":
        print("""
                    a.Purchase The Items
                    b.Delete From The List
                    c.Exit""")
        choose_option=input('Enter your option:')
        if choose_option=='a':
            print("\nAvailable items:")
            print("\n")
            print( "Available Items ")
            print("1."+items[0].title())
            print("2."+items[1].title())
            print("3."+items[2].title())
            print("4."+items[3].title())
            print("")
            print("\n")
            total_amount=0
            while True:
                item=input("Enter the item : ")
                if item =="1":
                    print("Quantity =" +quantity[0])
                    print("1kg price is ="+price[0])
                    Quantity=int(input("Enter the quantity : "))
                    price = 30* Quantity  
                    print(str(price)+ " for buying item")
                    Quantity1= 30 - Quantity
                    print("The Rest of quantity is  " +str(Quantity1)+"kg")
                    print("\n")
                #continue
                if item == "2" :
                    print("Quantity ="+quantity[1])
                    print("1kg price is ="+price[1])
                    Quantity=int(input("Enter the quantity : "))
                    price = 35* Quantity  
                    print("You will pay " +str(price)+ " for buying item")
                    Quantity1= 35- Quantity
                    print("The Rest of quantity is  " +str(Quantity1)+"kg")
                    print("\n")
                    #continue
                if item == "3" :
                    print("Quantity = "+quantity[2])
                    print("1kg price is ="+price[2])
                    Quantity=int(input("Enter the quantity : "))
                    price = 25 * Quantity  
                    print("You will pay " +str(price)+ " for buying item")
                    Quantity1 = 25 - Quantity
                    print("The Rest of  quantity is  " +str(Quantity1)+"kg")
                    print("\n")
                    #continue

                if item == "4" :
                    print("Quantity ="+quantity[3])
                    print(" 1 piece price is ="+price[3])
                    Quantity=int(input("Enter the quantity : "))
                    price = 15 * Quantity  
                    print("You will pay " +str(price)+ " for buying item")
                    Quantity1= 15 - Quantity
                    print("The Rest of  quantity is  " +str(Quantity1)+"kg")
                    total_amount=str(price)
                    print("\n")
                    continue
                if item =='Q' or 'q':
                    break
                #exit()
                #continue
                else:
                    exit()    
        if choose_option=='b':
            print("Your shopping  cart list is:",shop_item)
            delete_shop=input("Enter the delete item in your shopping cart:")
            if delete_shop in shop_item:
                m=shop_item.index(delete_shop)
                del shop_item[m]
                print(shop_item[m]+"is deleted")
        if choose_option=='c':
            exit()

           
           
                
        
    
    if user=='3':
      Option = 'Q' or 'q'
      exit()




