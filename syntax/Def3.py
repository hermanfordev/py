#-*- coding: utf-8 -*-
#def 3

def sum_many(*args):
  sum = 0
  for i in args:
    sum = sum + i
  return sum

result = sum_many(1,2,3,4)

print(result)




