import random

sides = ["with Roasted Cauliflower","with Scalloped Potatoes","with Wild Rice","with Sweet Potato Fries"]
main_course = ["Bean Soup","Chili","Chickpea Wraps","Couscous salad","Black Bean Burgers"]
desserts = ["Brownies","Chocolate Chip Cookies","Ice Cream","Yogurt Bars"]


first = (random.choice(main_course))
second=(random.choice(sides))
third=(random.choice(desserts))

random_list = [first,second,third]


def menu():
    random_list


print(random_list)
