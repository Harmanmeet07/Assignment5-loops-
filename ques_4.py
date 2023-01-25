# nested loop is a loop inside another loop
#used when you have nested arrays,lists or matrix
#also used when you need to print star or number pattern
for row in range(9):
  for column in range(5):
    if row <= 4:
      if column <= row:
        print("*", end=" ")
    else:
      if column >= row-4:
        print("*", end=" ")
  print()