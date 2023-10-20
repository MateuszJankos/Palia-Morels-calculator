num1 = float(input("Enter your glow worm farm count:     "))
num2 = float(input("Enter how many morels left inside:   "))
num3 = float(30)

result = (num3 - num2) * num1
stacks = float(0)
rows = float(0)
print("Overall Morels:   ", result)

while result >= 240:
    result = result - 240
    rows += 1

while result >= 30:
    result = result - 30
    stacks += 1

print("Rows of Morels:   ", rows)
print("Stacks of Morels: ", stacks)
print("Single Morels:    ", result)