def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_till_n(N):
    primes = [n for n in range(2, N+1) if is_prime(n)]
    return primes

if __name__ == "__main__":
    try:
        N = int(input("Enter a number: "))
        if N < 2:
            print("There are no prime numbers less than 2.")
        else:
            print("Prime numbers up to", N, ":", find_primes_till_n(N))
    except ValueError:
        print("Please enter a valid integer.")
