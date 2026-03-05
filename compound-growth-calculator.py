w = input("Increase(1) or Decrease(2): ")
while len(w) == 0:
   w = input("Increase(1) or Decrease(2): ")

w = int(w)
if w == 1:
   x = float(input("The pricipal amount: "))

   y = int(input("The number of iterations (integers only): "))

   z = float(input("Percentage increase: "))
   z = z/100

   for _ in range(y):
    x =  x + x*z
   
elif w == 2:
   x = float(input("The pricipal amount: "))

   y = int(input("The number of iterations (integers only): "))

   z = float(input("Percentage decrease: "))
   z = z/100
   for _ in range(y):
      x =  x - x*z
else:
   print("Invalid choice")   
   

print("The answer is :" , x)
