# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# Outer loop for rows
for i in range(1, 6):  # Outer loop will run from 1 to 5
    # Inner loop for columns
    for j in range(1, 6):  # Inner loop will also run from 1 to 5
        print(i * j, end="\t")  # Print the product and a tab for spacing
    print()  # Newline after each row
