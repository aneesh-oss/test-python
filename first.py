def factorial(n):
# Calculate the factorial of a number.
    if n == 0:
        return 1
    else:
        return n * factorial(n- 1)
        
def main():
    num = 7
    print("The factorial of",num,"is",factorial(num))
main()