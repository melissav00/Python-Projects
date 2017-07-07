import math
 math.pi

 def text(prompt_text):
       while 1:
          inp = input(prompt_text)
          if inp in 'yYnN':
              return inp in 'yY'
           else:
              print('Choose Y or N please.')
 def story_line():
     print("Welcome to Pizza Palace!")
       while 1:
     diam = prompt_float("What is the diameter of the pizza? ")
 price = prompt_float("What is the price of the pizza? ")
           answer=input("How big should the raidus in volume be?")
          answer2=input("How big should the radius be in the area?")
           r=answer
 def prompt_float(prompt_text):       while 1:
           inp = input(prompt_text)
           try:
             return float(inp)
 def unit_cost(diameter, price):
     rad = diameter/2.0
      area = math.pi * int(answer2)**2
        return price/area
         def volume(r):
29       v=(1.33333333)*math.pi*int(answer)**3
30       print(v)
31       return(v)
32
33   def area(r):
34       a=4*math.pi*int(answer2)**2
35       print(a)
36       return(a)
37   volume(r)
38   area(r)
