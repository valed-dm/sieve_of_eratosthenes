# Python program to print all
# primes smaller than or equal to
# N using Sieve of Eratosthenes
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
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:

        # If prime[p] is not
        # changed to 'False', then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    N = 25
    print("Following are the prime numbers smaller"),
    print("than or equal to", N)
    sieve_of_eratosthenes(num=N)
