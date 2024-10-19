class Cafe:
    def __init__(self):
        # self.order = order
        pass
    
    def details(self):
        
        bill = 0  
        menu = {
            "Pizza" : 1000,
            "Drink" : 200,
            "Tea" : 150,
            "Coffee" : 250,
            "Water" : 50
        }
        

        while True:
            
            customer= input("\nPlace your order with order name or press Q to complete your order: ")
            
            # if customer in menu:
            #     bill += menu[customer]
            # else:
            #     print("Please Take a look on our menu and Order again if you want")
            
            if customer == "Pizza" or customer == "pizza":
                bill += menu["Pizza"]
            elif customer == "Drink" or customer == "drink":
                bill += menu["Drink"]
            elif customer == "Tea" or customer == "tea":
                bill += menu["Tea"]
            elif customer == "Coffee" or customer == "coffee":
                bill += menu["Coffee"]
            elif customer == "Water" or customer == "water":
                bill += menu["Water"]
            elif customer == "Q" or customer == "q":
                break
            elif customer.isdigit():
                print(f"Sorry we dont have {customer} in our menu")
            else:
                print("Please Take a look on our menu and Order again if you want")
        print(bill)
        self.print_bill(bill)
    
    def print_bill(self,bill):

        print("\n********** Welcome To Pathan Cafe **********")
        print("\n********** Thanks For Coming here **********")
        print(f"\nTotal Bill = {bill}")




print("\n********** Welcome To Pathan Cafe **********")
print("Our Menu List is:\nPizza : 1000\nDrink : 200\nTea : 150\nCoffee : 250\nWater : 50")
customer1 = Cafe()
customer1.details()
