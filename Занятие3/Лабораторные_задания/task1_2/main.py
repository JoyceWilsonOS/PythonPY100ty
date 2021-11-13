def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_rec(n):
    if n == 1:
        return n
    else:
        return n * factorial_rec(n-1)

if __name__ == "__main__":
    print(factorial(4))
    print(factorial_rec(4))
    # Write your solution here
    pass
