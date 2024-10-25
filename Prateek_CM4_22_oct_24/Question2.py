# Step 1: Accept input from the user
n = input("Enter an integer: ")

# Step 2: Create the values for nn and nnn
nn = n + n  # Concatenates the string n twice
nnn = n + n + n  # Concatenates the string n three times

# Step 3: Convert the strings to integers and compute the result
result = int(n) + int(nn) + int(nnn)

# Step 4: Output the result
print(f"The result of n + nn + nnn for n = {n} is: {result}")
