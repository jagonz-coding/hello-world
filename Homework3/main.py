#Name: Juan Gonzalez
#ID: 1808943

class FoodItem:

    def __init__(self, food, fat, carbs, protein):
        self.food = food
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def __init__(self, name = "None", fat = 0.0, carbs = 0.0, protein = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":

    fitem1 = FoodItem()

    fname = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    fitem2 = FoodItem(fname, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())

    fitem1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, fitem1.get_calories(num_servings)))

    print()

    fitem2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, fitem2.get_calories(num_servings)))
