
class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
     def eat(self):
        print(self)
        

    def digest(self, nutrients)
        print(nutrients)

 

class Fruit(Food):
    def (self, name, calories):
        super().(name, calories)
        
class Vegetable(Food):
    def (self, name, calories, color):
        super().(name, calories, color)
        self.color() = color

       

   

if __name__ == "__main__":
    apple = Fruit("Apple", 95,)
    broccoli = Vegetable("Broccoli", 50)


    print(apple)
    print(broccoli)
    apple.eat(self)
    apple.digest(self, 5)
