# Values are per 100 grams of fruit.
# Sources: USDA FoodData Central, Nutritionix, Healthline.
fruits = {
    "apple": {
        "calories": 52,
        "carbohydrates": 13.8,  # g
        "fiber": 2.4,  # g
        "sugar": 10.4,  # g
        "vitamins": {"Vitamin C": 4.6, "Vitamin K": 2.2, "Vitamin B6": 0.041},  # mg or µg
        "minerals": {"Potassium": 107, "Manganese": 0.035},  # mg
        "antioxidants": ["Quercetin", "Catechin", "Chlorogenic Acid"]
    },
    "orange": {
        "calories": 47,
        "carbohydrates": 11.8,
        "fiber": 2.4,
        "sugar": 9.4,
        "vitamins": {"Vitamin C": 53.2, "Vitamin A": 11, "Vitamin B9 (Folate)": 30},
        "minerals": {"Calcium": 40, "Potassium": 181, "Magnesium": 10},
        "antioxidants": ["Flavonoids", "Carotenoids"]
    },
    "banana": {
        "calories": 89,
        "carbohydrates": 22.8,
        "fiber": 2.6,
        "sugar": 12.2,
        "vitamins": {"Vitamin B6": 0.367, "Vitamin C": 8.7, "Vitamin A": 3},
        "minerals": {"Potassium": 358, "Magnesium": 27, "Manganese": 0.27},
        "antioxidants": ["Dopamine", "Catechins"]
    },
    "strawberry": {
        "calories": 32,
        "carbohydrates": 7.7,
        "fiber": 2.0,
        "sugar": 4.9,
        "vitamins": {"Vitamin C": 58.8, "Vitamin B9 (Folate)": 24, "Vitamin K": 2.2},
        "minerals": {"Manganese": 0.386, "Potassium": 153, "Iron": 0.41},
        "antioxidants": ["Anthocyanins", "Ellagic Acid", "Quercetin"]
    },
    "grapes": {
        "calories": 69,
        "carbohydrates": 18.1,
        "fiber": 0.9,
        "sugar": 15.5,
        "vitamins": {"Vitamin C": 3.2, "Vitamin K": 14.6, "Vitamin B6": 0.086},
        "minerals": {"Copper": 0.127, "Potassium": 191, "Manganese": 0.071},
        "antioxidants": ["Resveratrol", "Flavonoids", "Anthocyanins"]
    },
    "mango": {
        "calories": 60,
        "carbohydrates": 15.0,
        "fiber": 1.6,
        "sugar": 13.7,
        "vitamins": {"Vitamin A": 54, "Vitamin C": 36.4, "Vitamin E": 0.9, "Vitamin B6": 0.119},
        "minerals": {"Potassium": 168, "Magnesium": 9},
        "antioxidants": ["Beta-carotene", "Mangiferin"]
    },
    "pineapple": {
        "calories": 50,
        "carbohydrates": 13.1,
        "fiber": 1.4,
        "sugar": 9.9,
        "vitamins": {"Vitamin C": 47.8, "Vitamin B6": 0.112, "Vitamin A": 3},
        "minerals": {"Manganese": 0.927, "Copper": 0.11, "Potassium": 109},
        "antioxidants": ["Bromelain", "Flavonoids"]
    },
    "watermelon": {
        "calories": 30,
        "carbohydrates": 7.6,
        "fiber": 0.4,
        "sugar": 6.2,
        "vitamins": {"Vitamin C": 8.1, "Vitamin A": 28, "Vitamin B5": 0.221},
        "minerals": {"Potassium": 112, "Magnesium": 10},
        "antioxidants": ["Lycopene", "Beta-carotene", "Cucurbitacin E"]
    },
    "blueberry": {
        "calories": 57,
        "carbohydrates": 14.5,
        "fiber": 2.4,
        "sugar": 9.7,
        "vitamins": {"Vitamin C": 9.7, "Vitamin K": 19.3, "Vitamin B6": 0.052},
        "minerals": {"Manganese": 0.336, "Iron": 0.28, "Calcium": 6},
        "antioxidants": ["Anthocyanins", "Quercetin", "Resveratrol"]
    },
    "pomegranate": {
        "calories": 83,
        "carbohydrates": 18.7,
        "fiber": 4.0,
        "sugar": 13.7,
        "vitamins": {"Vitamin C": 10.2, "Vitamin K": 16.4, "Vitamin B9 (Folate)": 38},
        "minerals": {"Potassium": 236, "Iron": 0.3},
        "antioxidants": ["Punicalagins", "Anthocyanins", "Ellagic Acid"]
    }
}

# Example: Print detailed nutrition info for a mango
print(fruits["mango"])
