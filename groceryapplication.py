#grocery application
from datetime import datetime
class ItemsData:
    fruits=[]
    nuts=[]
    beverages=[]
    def __init__(self,item_id,item_name,price):
        self.item_id=item_id
        self.item_name=item_name
        self.price=price
class Itemfunctionality:
    def display_item_info(self):
        print("------------------------------------------------\n")
        print("Grocery items avilable...\n")
        print(" 1.Fruits\n 2.Nuts\n 3.Beverages")
        choice=int(input("Enter your choice : "))
        if(choice==1):
            for item in ItemsData.fruits:
                print(item.item_id,'\t',item.item_name,'\t',item.price)
        elif(choice==2):
            for item in ItemsData.nuts:
                print(item.item_id,'\t',item.item_name,'\t',item.price)
        elif(choice==3):
            for item in ItemsData.beverages:
                print(item.item_id,'\t',item.item_name,'\t',item.price)

    def select_item(self):
        choice=int(input("Select the item that you wanna order : "))
        if(choice==1):
            lis=[]
            inp=int(input("Select the fruit that you wanna order : "))
            inp1=int(input("Enter the quantity per kg the price is mentioned : "))
            lis.append(inp1)
            for item in ItemsData.fruits:
                if item.item_id==inp:
                    lis.append(item.item_name)
                    lis.append(item.price)
                return lis
        elif(choice==2):
            lis=[]
            inp=int(input("Select the nut that you wanna order : "))
            inp1=int(input("Enter the quantity per kg the price is mentioned : "))
            lis.append(inp1)
            for item in ItemsData.nuts:
                if item.item_id==inp:
                    lis.append(item.item_name)
                    lis.append(item.price)
                return lis
        elif(choice==3):
            lis=[]
            inp=int(input("Select the beverages that you wanna order : "))
            inp1=int(input("Enter the quantity per kg the price is mentioned : "))
            lis.append(inp1)
            for item in ItemsData.beverages:
                if item.item_id==inp:
                    lis.append(item.item_name)
                    lis.append(item.price)
                return lis        
    
class OrdersData:
    orders=[]
    def __init__(self,selected_item,price,payment_mode,ordered_time):
        self.selected_item=selected_item
        self.total_price=price
        self.payment_mode=payment_mode
        self.ordered_time=ordered_time

class Orderfunctionality:
    def orderpreview(self,selected_item,price):#multiple inheritance
        print("--------------------------------------------------------\n")
        print("Booking Preview:\n")
        print(f'Ordered item: {selected_item}')
        print(f'Total amount: {price}')
        print("--------------------------------------------------------\n")
        print("Payment Options:\n1. Card\n2. UPI")
        payment_choice=int(input("\nchoose a payment option:\n"))
        if payment_choice!=1 and payment_choice!=2:
            print("Enter a valid payment method")
            return False
        else:
            if payment_choice == 1:
                payment_mode = "Card"
                print("Ordered Successfully")
            elif payment_choice == 2:
                payment_mode = "UPI"
                print("Ordered Successfully")
            ordered_time=datetime.now().strftime("%y/%m/%d,%H:%M:%S")
            new_order=OrdersData(selected_item,price,payment_mode,ordered_time)
            OrdersData.orders.append(new_order)
            return True
    def display_history(self):
        if len(OrdersData.orders)==0:
            print("No orders made yet!")
        else:
            print("--------------------------------------------------------\n")
            for order in OrdersData.orders:
                print(order.selected_item,'\t',order.total_price,'\t',order.payment_mode,'\t',order.ordered_time)

    def delete_history(self):
        if len(OrdersData.orders)==0:
            print("Orders history is empty")
        else:
            choice=int(input("1.Delete the entire history\n2.Delete the last order history : "))
            if choice==1:
                OrdersData.orders.clear()
                print("Order history deleted entirely....")
            else:
                del(OrdersData.orders[-1])
                print("Your last history is deleted")
                
                

class Groceryapplication(Itemfunctionality,Orderfunctionality):
    def run(self):
        while True:
            print("--------------------------------------------------------\n")
            print("Menu:")
            print("1. Order items")
            print("2. Display order history")
            print("3. Delete order history")
            print("4. Quit")
            choice = int(input("\nEnter your choice:\n"))
            if choice == 1:
                self.order_item()
            elif choice == 2:
                self.display_history()
            elif choice == 3:
                self.delete_history()
            elif choice == 4:
                quit()
            else:
                print("Invalid Choice")
    def order_item(self):
        self.display_item_info()
        selected=self.select_item()
        item_quantity=selected[0]
        selected_item=selected[1]
        item_price=selected[2]
        total_price=item_quantity*item_price
        self.orderpreview(selected_item,total_price)
        

if __name__=='__main__':
    fruit1=ItemsData(1,"Apple    ",200)
    fruit2=ItemsData(2,"Orange",50)
    fruit3=ItemsData(3,"Grapes",100)
    ItemsData.fruits.append(fruit1)
    ItemsData.fruits.append(fruit2)
    ItemsData.fruits.append(fruit3)

    nut1=ItemsData(1,"Almond     ",200)
    nut2=ItemsData(2,"Pista      ",50)
    nut3=ItemsData(3,"Dry Grapes",100)
    ItemsData.nuts.append(nut1)
    ItemsData.nuts.append(nut2)
    ItemsData.nuts.append(nut3)

    beverage1=ItemsData(1,"Coffee",40)
    beverage2=ItemsData(2,"Tea    ",50)
    beverage3=ItemsData(3,"Juice  ",100)
    ItemsData.beverages.append(beverage1)
    ItemsData.beverages.append(beverage2)
    ItemsData.beverages.append(beverage3)
    
    orders=Groceryapplication()
    orders.run()

    
