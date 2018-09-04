# -*- coding: utf-8 -*-
#for4

marks = [60, 80, 90, 30, 40, 10, 90, 83]
number = 0

for mark in marks:
  number = number + 1
  if mark < 60:
    continue
  print("congratulations number %d" %number)

  