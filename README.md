
# Compound Growth Calculator

A small Python program that calculates how a number changes when it is repeatedly increased or decreased by a percentage.

The program asks the user whether they want to **increase or decrease**, then applies that percentage change for a chosen number of iterations.

This demonstrates how **compound percentage change** works.

---

## How it works

The program takes four inputs from the user:

* Whether the value should increase or decrease
* The starting value (principal amount)
* The number of iterations
* The percentage change

Each iteration applies the percentage change to the **current value**, not the original value.

Example:

Start: `100`
Increase: `10%`
Iterations: `2`

Calculation:

100 → 110 → 121

Final result:

121

---

## Python Code

```python
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
```

---

## Example Run

```
Increase(1) or Decrease(2): 1
The principal amount: 100
The number of iterations (integers only): 3
Percentage increase: 5
```

Output:

```
The answer is : 115.7625
```

---

## Requirements

* Python 3
* Runs in any terminal or command prompt

---

## Author
**Noel**

