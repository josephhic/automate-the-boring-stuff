# Function that defines the Collatz sequence
def collatz(number): 
    if number % 2 == 0:
        half = number/2
        print(half)
        return half
    else: 
        collatz = 3*number + 1
        print(collatz)
        return collatz

# Create Collatz sequence until final condition is met (number = 1)  
user_number = int(input())
while user_number != 1: 
    collatz(user_number)

