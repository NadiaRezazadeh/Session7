from prettytable import PrettyTable
Products = []
def read_text_from_file():
    f = open('Database.txt','r')
    for line in f:
       result = line.split(',')
       my_dict = {'ID':result[0],'Name':result[1],'Price':result[2],'Count':result[3]}
       Products.append(my_dict)

def Add():
    ID = input("Enter ID : ")
    Name = input("Enter Name : ")
    Price = input("Enter Price : ")
    Count = input("Enter Count : ") 

    new_product = {'ID':ID,'Name':Name,'Price':Price,'Count':Count}
    Products.append(new_product)
    print("Your product has been successfully added")

def Delete():
    ID = input("Enter ID :")
    for product in Products:
        if product["ID"] == ID:
            Products.remove(product)
            print("Your product has been successfully deleted")
   
def Edit():
    ID = input("Enter ID :")
    for product in Products:
        if product["ID"] == ID:
           print("1.Name")
           print("2.Price")
           print("3.Count")
           a = int(input("Which part would you want to edit ?"))
           
           if a == 1:
                e = input("Enter the new name :")
                product["Name"] = e
                print("Name has been successfully edited ")

           elif a == 2:
                e = input("Enter the new price :")
                product["Price"] = e
                print("Price has been successfully edited")
           
           elif a == 3:
                e = input("Enter the new count :")
                product["Count"] = e 
                print("Count has been successfully edited ")
        
   

def Search():
    user_choice = input("Enter your keyword : ")
    for product in Products:
        if product['ID'] == user_choice or product['Name'] == user_choice :
            print(product)
            break
    else:
        print(" Product not found !! ")


def Show_list():
    t = PrettyTable(['ID','Name','Price','Count'])
    for product in Products:
        t.add_row([product['ID'],product['Name'],product['Price'],product['Count']])
    print(t)

def Buy():
    while True:
        Bill = []
        print("1.Yes")
        print("2.No")
        c = int(input("Whould you want to make a purchase?"))
        if c == 1:
            ID = input("Enter ID :")
            for product in Products:
                if product["ID"] == ID:
                    a = int(input("How many of this product do you want ?"))
                    if int(product["Count"]) >= a:
                        purchasedproduct ={'ID':product['ID'],'Name':product['Name'],'Price':product['Price'],'Count':a}
                        Bill.append(purchasedproduct)
                        product["Count"] = str(int(product["Count"]) - a)
                        break
                    elif int(product['Count']) < a:
                        print("Unfortunately,this quantity of this product is not available!")
                        break
            else :
               print("Unfortunately,this product is not in stock!!")
               
        elif c == 2:
            print("Thanks for your shopping, here is your purchase invoice :")
            t = PrettyTable(['ID','Name','Price','Count'])
            for product2 in Bill:
                t.add_row([product2['ID'],product2['Name'],product2['Price'],product2['Count']])
            print(t)
            break    


def Write_text_to_file():
    f = open('Database.txt','w')
    for product in Products:
        x = ", ".join([product["ID"],product["Name"],product["Price"],product["Count"]])
        f.write(x)

def show_menu():
    print("1.Add")
    print("2.Delete")
    print("3.Edit")
    print("4.Search")
    print("5.Show list")
    print("6.Buy")
    
read_text_from_file()
while True:
    a = input("Enter 's' to display menu or 'e' to exit :" )
    if a == 's':
        show_menu()
        choice = int(input("Enter your choice:"))

        if choice == 1:
            Add()

        elif choice == 2:
            Delete()    

        elif choice == 3:
            Edit()

        elif choice == 4:
            Search()

        elif choice == 5:
            Show_list()

        elif choice == 6:
            Buy()

    elif a == 'e':
        Write_text_to_file()
        print("Goodbye!!")
        break