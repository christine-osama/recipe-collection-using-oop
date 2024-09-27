class Recipe:
    def __init__(self,recipe_name,ingredients,cooking_time,instructions):
        self. recipe_name=recipe_name
        self. ingredients=ingredients
        self. cooking_time=cooking_time
        self. instructions=instructions

    def display_recipe(self):
        print(f"Recipe Name: {self. recipe_name}")
        print(f"Ingradiants:{self. ingredients}")
        print(f"Cooking_time: {self. cooking_time}")
        print(f"instructions:{self. instructions}")
        print(f"_"*20)
def create_recipe():
    recipe_name=input("Enter recipe name:")
    ingredients=input("Enter recipie ingredients(comma_separated):")
    cooking_time=input("Enter cooking time:")
    instructions=input("Enter cooking instructions:")
    return Recipe(recipe_name,ingredients,cooking_time,instructions)

print("welcome to Recipe collection \n")    
my_recipe = create_recipe()
print("Recipe added successefly")
my_recipe.display_recipe()



        