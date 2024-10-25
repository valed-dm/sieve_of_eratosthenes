# Python program to print all
# primes smaller than or equal to
# N using Sieve of Eratosthenes
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

# Описание алгоритма
#
# Этот алгоритм назван в честь древнегреческого учёного Эратосфена Киренского.
#
# Алгоритм заключается в том, что изначально мы берём всё множество целых чисел в интересующем
# нас диапазоне, от 2 до N. Затем последовательно проходимся по этому множеству,
# вычёркивая каждое чётное число, т.к. оно делится на 2.
# После этого возвращаемся в начало и вычёркиваем все числа, делящиеся на 3,
# если они ещё не зачёркнуты. Затем делящиеся на следующее простое число – на 5.
# Затем на 7, на 11 и т. д. То есть мы «просеиваем» исходное множество целых чисел через сито.
# В итоге у нас останутся только простые числа.

def sieve_of_eratosthenes(num):
    if num < 2:
        return []

    # Only consider odd numbers; assume all are prime initially
    prime = [True] * ((num // 2) + 1)
    prime[0] = False  # 1 is not prime

    # Start from the first prime number, 3
    for p in range(3, int(num**0.5) + 1, 2):
        if prime[p // 2]:
            # Mark multiples of `p`, starting from `p^2`, skipping even multiples
            for i in range(p * p, num + 1, 2 * p):
                prime[i // 2] = False

    # Collect primes, handling `2` separately and only up to `num`
    primes = [2] + [2 * i + 1 for i in range(1, len(prime)) if prime[i] and (2 * i + 1) <= num]
    print(primes)
    return primes


if __name__ == '__main__':
    N = 30
    print("Following are the prime numbers smaller"),
    print("than or equal to", N)
    sieve_of_eratosthenes(num=N)
