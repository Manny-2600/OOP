class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

 

class Fruit(Food):
    def __init__(self, name, calories, color):
        super().__init__(name, calories)
        
class Vegetable(Food):
    def __init__(self, name, calories):
        super().__init__(name, calories)
       

   

if __name__ == "__main__":
    apple = Fruit("Apple", 95,)
    broccoli = Vegetable("Broccoli", 50)

    print(apple)
    print(broccoli)