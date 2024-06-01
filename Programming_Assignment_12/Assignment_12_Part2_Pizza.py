def main():
    class snack:
        def __init__(self):
            self.pizza = "plain"
            self.sauce = "Barbeque"
            self.topping = "olives"
            self.extratopping = "none"
        
        def chicken_pizza(self):
            self.rice = "Chicken"
            
        def add_sauce1(self):
            self.sauce = "Creamy Ceaser"
            
        def add_veggies(self):
            self.extratopping = "Tomatoes"

        def __str__(self):
            return(f"Your pizza will have {self.pizza} pizza, {self.sauce} sauce, and {self.topping} as topping and extratopping {self.extratopping}")
    nrml = snack()
    print(nrml)
    
    Specl = snack()
    Specl.chicken_pizza()
    Specl.add_sauce1()
    Specl.add_veggies()
    print(Specl)
    
if __name__ == "__main__":
     main()