start = int(input("Pick a starting number for a list:"))
end  = int(input("Pick a ending number for a list:"))


def generateNumbers(start,end):
    num_list=[]
    if start == end:
        print("Both values are equal to each other. Please input opposite values.")
    elif start > end:
        print("Enter a start values less than end.")
    while (start < end):
            start = start + 1
            num_list.append(start)
    print(num_list)

generateNumbers(start,end)
