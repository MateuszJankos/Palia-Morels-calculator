num1 = float(input("Enter your glow worm farm count:   "))
num2 = float(input("Enter how many morels left:   "))
num3 = float(30)

result = (num3 - num2) * num1
stacks = float(result / 30)
rows = float(stacks / 8)
print("Needed Morels: ", result)
print("Stacks: ", stacks)
print("Rows: ", rows)