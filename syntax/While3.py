#While3

coffee = 10
money = 300

while money:
  print("get your coffee")
  coffee = coffee -1
  money = money -100
  print("remain coffee is %d " %coffee)

  if not coffee:
    print("out of stock")
    break

  if not money:
    print("your money is %d " %money)
    break



