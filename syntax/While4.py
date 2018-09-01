#-*- coding: utf-8 -*-
#While4

coffee = 10

while True:
  money = int(input("insert money : "))

  if money == 300:
    print("here is yor coffee")
    coffee = coffee - 1
    print("coffee %d left" %coffee)

  elif money > 300:
    print("coffee here and the change %d" %(money - 300))
    coffee = coffee - 1
    print("coffee %d left" %coffee)

  else:
    print("here is your money")
    print("coffee %d left" %coffee)

  if coffee == 0:
    print("out of stock")
    break



  

