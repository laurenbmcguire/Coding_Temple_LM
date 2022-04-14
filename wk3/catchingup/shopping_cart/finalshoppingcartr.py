class ShoppingCart:
    
    def __init__(self):
        self.cart = []
    
    def run(self):
        print=input("Welcome to the grocery shopping cart press enter to continue ")
        
        while True:
            item = input("what do you want to add? type 'quit' to exit. type 'clear' to remove an item. ")
            
            if item == 'quit':
                print(self.cart)
                
                break
                
            if item == 'clear':
                pluck = input("what do you want to remove? ")
                self.cart.remove(pluck)
                print(self.cart)
                
            else:
                self.cart.append(item)
                print(self.cart)
        

shopping_cart = ShoppingCart()
shopping_cart.run()