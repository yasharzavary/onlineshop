password=123
username="abc"                
listInfo=[[1,2,3,4,5],["a","b","c","d","e"],[20,10,60,45,16],[56,128,452,75,156],["1401/10/2","1405/06/08","1402/03/26","1400/02/05","1399/12/28"]]
# row 1: code, row2: name, row 3:count, row 4 : price
buyer=[] #1:code 5:count 20:price 100: count*price
pas_buyers = []
Today_Date = "1401/11/2"

# group members:
#   1.sara asadi
#   2.nazli chukhaciyan
#   3.sahel arfaii
#   4.fateme nagizadeh
#   5.asra najafi

# place for change our date
# writed by : nazli chukhaciyan
def Date_Controller():
    def Date_Changer():
        # coustemer give year month and day for change the date of the program
        global Today_Date
        Date_Year = input("Say year : ")
        Date_Month = input("Say Month : ")
        Date_Day = input("Say day : ")
        Today_Date = f"{Date_Year}/{Date_Month}/{Date_Day}"
        print("""Date update!
              ----------------------------
              """)
    while True:
        print("""\t\t******  Date Menu  ******
              \t1.Show date
              \t2.Edit date
              \t3.Exit""")
        x = int(input())
        if x == 3:
            return
        elif x == 1:
            print(Today_Date)
        elif x == 2:
            Date_Changer()
        else:
            print("Wrong option")



# a func for print expired items
# writed by : nazli chukhaciyan
def exproduct():
    for i in listInfo[4]:
        if int(Today_Date[:4])>int(i[:4]):
            for j in range(len(listInfo) - 1):
                print(f"{listInfo[j][listInfo[4].index(i)]}", end="\t")
            print()
        elif int(Today_Date[:4])==int(i[:4]):
            if int(Today_Date[5:7])>int(i[5:7]):
                for j in range(len(listInfo) - 1):
                    print(f"{listInfo[j][listInfo[4].index(i)]}", end="\t")
                print()
            elif int(Today_Date[5:7])==int(i[5:7]):
                if int(Today_Date[8:])>int(i[8:]):
                    for j in range(len(listInfo) - 1):
                        print(f"{listInfo[j][listInfo[4].index(i)]}", end="\t")
                    print()
                    
                    
# place for order the listinfo by price
# writed by : asra najafi
def Order_By_Price():
    # i use bubblesort for order the infolist
    global listInfo
    for i in range(len(listInfo[3])):
        for j in range(len(listInfo[3]) - i - 1):
            if listInfo[3][j] > listInfo[3][j + 1]:
                for z in range(len(listInfo)):
                    listInfo[z][j], listInfo[z][j + 1] = listInfo[z][j + 1], listInfo[z][j]
    showAllInfoForManager()
    

# Edit part for changing information of the products
# writed by : sahel arfaii
def Edit():
    # i make it global for changing the product list
    global listInfo
    # i make one loop because it can be possible that coustemer want to add some product to the list
    while True:
        # for finding stuff we use code for name part
        # and use name for code part
        print("""\t\t******  Edit Option  ******
        1.Edit Name
        2.Edit Code
        3.Edit Price
        4.Edit Stock
        5.Exit""")        
        x = int(input())
        if x == 1:
            Code = int(input("Say Code : "))
            #  i use try/except block for control the existence of the stuff 
            try:
                listInfo[1][listInfo[0].index(Code)] = input("Say your new name : ")
                print("Name update!")
            except:
                print("It isn't such stuff...")
        elif x == 2:
            Name = input("Say stuff name : ")
            try:
                listInfo[0][listInfo[1].index(Name)] = int(input("Say your new code : "))
                print("Code update")
            except:
                print("It isn't such staff...")
        elif x == 3:
            # for finding that stuff...coustemer can choose code finding or name finding
            Search_By = int(input("""Say seaarch type:
                        1.By code
                        2.By Name
                                  """))
            if Search_By == 1:
                Code = int(input("Say Code : "))
                try:
                    listInfo[3][listInfo[0].index(Code)] = input("Say your new Price : ")
                    print("Price update")
                except:
                    print("It isn't such stuff...")
            elif Search_By == 2:
                Name = input("Say stuff name : ")
                try:
                    listInfo[3][listInfo[1].index(Name)] = int(input("Say your new Price : "))
                    print("Price update")
                except:
                    print("It isn't such staff...")
        elif x == 4:
            # buyer can choose code or name search
            Search_By = int(input("""Say seaarch type:
                            1.By code
                            2.By Name
                                  """))
            if Search_By == 1:
                Code = int(input("Say Code : "))
                try:
                    listInfo[2][listInfo[0].index(Code)] = input("Say your new stock : ")
                    print("Stock update!")
                except:
                    print("It isn't such stuff...")
            elif Search_By == 2:
                Name = input("Say stuff name : ")
                try:
                    listInfo[2][listInfo[1].index(Name)] = int(input("Say your new stock : "))
                    print("Stock update!")
                except:
                    print("It isn't such staff...")
        elif x == 5:
            return
        else:
            print("Wrong Option")

# control that number of buyers don't go over 5  
def Buyer_Number_Checker():
    if len(buyer) == 5:
        return False
    return True
 
# give us a code for new buyer
def Give_Buyer_Code():
    return len(buyer)

# check code of old buyer
# writed by : asra najafi 
def Code_Checker(C):
    if C < 0 or C > 4:
        return False
    try:
        x = len(buyer[C])
        return True
    except:
        return False

# place that control that one buyer don't buy over 4 item
def Product_Limit_Checker(C):
    if len(buyer[C]) == 4:
        print("your list is full..please delete or pay for products...")
        return True
    
    return False

# this place show us factor of buyer
def Show_Factor(Buyer_C):
    print("\t\t  *** factor ***")
    for i in buyer[Buyer_C]:
        print(f"Code : {i[0]}\tNumber : {i[1]}\tprice_by : {i[2]}\ttotal_price : {i[3]}")
    print("--------------------------------------------------------------------------")


# place for last part...
# writed by : sara asadi
def Pay(B_Code):
    global pas_buyers
    def goodbye():
        global buyer
        buyer.remove(buyer[B_Code])
        print("Thanks for your Buy")
    Show_Factor(B_Code)
    while True:
        op = int(input("""Do you accept it?
                1.Yes
                2.No
                       """))
        if op == 1:
            temp = []
            temp.append(buyer[B_Code])
            temp.append(input("your adress : "))
            temp.append(input("what is your cellphone number : "))
            pas_buyers.append(temp)
            goodbye()    
        elif op == 2:
            return
        else:
            print("invalid operator")
            
# place for add item for buyer
# writed by fatemeh nagizadeh
def Product_Adder(B_code):
    def Adder(B_Co, A, T):
        global buyer
        # control number of stocks in market
         # writed by : nazli chukhaciyan
        def Stock_Control(C, N):
            global listInfo
            if listInfo[2][listInfo[0].index(C)] >= N:
                listInfo[2][listInfo[0].index(C)] -= N
                return True
            return False
        temp = []
        if T == 1:
            A_Code = listInfo[0][listInfo[1].index(A)] 
            temp.append(A_Code)
            Number = int(input("How many do you want : "))
            if Stock_Control(A_Code, Number):
                temp.append(Number)
            else:
                return False
            Price = listInfo[3][listInfo[0].index(A_Code)]
            temp.append(Price)
            temp.append(Number * Price)
            buyer[B_Co].append(temp)
            return True
        elif T == 2:
            temp.append(A)
            Number = int(input("How many do you want : "))
            if Stock_Control(A, Number):
                temp.append(Number)
            else:
                return False
            Price = listInfo[3][listInfo[0].index(A)]
            temp.append(Price)
            temp.append(Number * Price)
            buyer[B_Co].append(temp)
            return True
    # this part search item that buyer want
     # writed by : nazli chukhaciyan
    def Stuff_Searcher(A, T):
        if T == 1:
            if A not in listInfo[1]:
                print("We dont have this product...")
                return True
        if T == 2:
            if A not in listInfo[0]:
                print("We dont have this Code...")
                return True
        return False
    while True:
        if Product_Limit_Checker(B_code):
            return
        Search_Type = int(input("""How do you want to search product?
                        1.Name
                        2.Code
                        3.Exit
                                """))
        if Search_Type == 1:
            Name = input("Say Name of product : ")
            if Stuff_Searcher(Name, 1):
                continue
            if not Adder(B_code, Name, 1):
                print("we dont have enough stock")
        elif Search_Type == 2:
            Code = int(input("say your code : "))
            if Stuff_Searcher(Code, 2):
                continue
            if not Adder(B_code, Code, 2):
                print("we dont have enough stock")
        elif Search_Type == 3:
            return
        else:
            print("invalid search type...try again")
        # we use loop because if coustemer want to add other thing...program back to first step
        while True:
            Reorder = int(input("""Other Order?:
                        1.Yes
                        2.No
                                """))
            if Reorder == 2:
                return
            elif Reorder == 1:
                break
            else:
                print("invalid input...")
        

def seperate():
    print("---------------------------")
    print("---------------------------")
def checkManageInfo(un,pa):
    if un==username and pa==password:
        return True
    else:
        return False
    
def showAllInfoForManager():
    for i in range(len(listInfo[0])):
      print(f"code is : {listInfo[0][i]}"
            f" and name is :{listInfo[1][i]}"
            f" and count is :{listInfo[2][i]}"
            f" and price is :{listInfo[3][i]}")
    print("-------------------------------------------------")
def showAllInfoForBuyer():
    j=0
    for i in range(len(listInfo[0])):
        if listInfo[2][i]>0:
           j=j+1
           print(f"code is : {listInfo[0][i]}"
                 f" and name is :{listInfo[1][i]}"
                 f" and price is :{listInfo[3][i]}")
    if j==0:
        print("not found")

#for manager          
def searchByCode(code):
    for i in range(len(listInfo[0])):
        if listInfo[0][i]==code:
            print(f"code is : {listInfo[0][i]}"
                  f" and name is :{listInfo[1][i]}"
                  f" and count is :{listInfo[2][i]}"
                  f" and price is :{listInfo[3][i]}")
            break
        elif i== len(listInfo[0])-1:
            print("not found")

#for buyer
def searchByCodeBuyer(code):
    for i in range(len(listInfo[0])):
        if listInfo[0][i]==code:
            return listInfo[3][i] #return price
        elif i== len(listInfo[0])-1:
            return -1
            
def mainMenu():
    
    print('''welcome to this app,choose your role:
          1. manager
          2. buyer
          0.exit   ''')


def manageMenu():
    print('''welcome to manege panel,choose one option from follow options:
          1.view all information
          2.Edit Option
          3.search 
          4.Edit date
          5.Ordered Show by Price
          6.expired products
          0.exit
          ''')

def buyMenu():
    print('''welcome to buy panel,choose one option from follow options:
          1.view all information
          2.add
          3.Show factor
          4.Show factor and pay
          10.Save and exit 
          0.exit
          ''')


while True:
    print("             *****      MAIN MENU    *****       ")
    mainMenu()
    mainAccount=int(input())
    if mainAccount==0:
        print("thank you for using this app!")
        break

    elif mainAccount==1:
        print("             ******      MANAGE MENU      *****     ")
        userUsername=input("enter username:\t")
        userPassword=int(input("enter password:\t:"))
        if checkManageInfo(userUsername,userPassword):
         while True:
             manageMenu()
             option=int(input())
             if option==0:
                 seperate()
                 break
             elif option == 1:
                 showAllInfoForManager()
                 seperate()
             elif option == 2:
                #  print("edit option")
                 Edit()
                 seperate()
             elif option == 3:
                 codeSearch=int(input("enter code for search:\t"))
                 searchByCode(codeSearch)
                 seperate()
             elif option == 4:
                 Date_Controller()
             elif option == 5:
                 Order_By_Price()
             elif option == 6:
                 exproduct()
             else:
                print("wrong option")
                seperate()

            
        else:
            print("wrong username or password")
            seperate()

    # we use old and new coustemer for can handle the buyers in list..
    # we give list empty index for new coustemer...
    # and want list index from who is past buyer
    # writed by : asra najafi
    elif mainAccount==2:
        New_Or_Old = int(input("""Are you a new buyer?
                    1.Yes
                    2.No
                               """))
        if New_Or_Old == 1:
            if Buyer_Number_Checker():
                Buyer_Code = Give_Buyer_Code()
                buyer.append(list())
                print(f"Your code is {Buyer_Code}")
            else:
                print("We dont have space for new buyer...")
                continue
        elif New_Or_Old == 2:
            Buyer_Code = int(input("Say your code : "))
            if not Code_Checker(Buyer_Code):
                print("Invalid buyer code...")
                continue
            
        print("             ******      BUY MENU      *****     ")

        while True:
            buyMenu()
            option=int(input())
            if option==0:
                buyer.remove(buyer[Buyer_Code])
                seperate()
                break
            elif option == 1:
                showAllInfoForBuyer()
                seperate()
            elif option == 2:
                Product_Adder(Buyer_Code)
                seperate()
            elif option == 3:
                Show_Factor(Buyer_Code)
            elif option == 4:
                Pay(Buyer_Code)
            elif option == 10:
                break
            else:
              print("wrong option")
              seperate()
          
        
    else:
        print("wrong option")
        seperate()
    
