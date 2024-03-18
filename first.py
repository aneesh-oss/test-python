def factorial(n):
# Calculate the factorial of a number.
    if n == 0:
        return 1
    else:
        return n * factorial(n- 1)
        
def main():
    num = int(input("Enter a nonnegative integer: "))
    print("The factorial of",num,"is",factorial(num))
main()