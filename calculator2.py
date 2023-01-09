#create function called main that prints the sqaured value of the user input
def main():
    x = int(input("What's X? "))
    print("X sqaured is", square(x))

#create a square function that squares 2 numbers
def square(n):
    return n * n

# Calls function main
main()
