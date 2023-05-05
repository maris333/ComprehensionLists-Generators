def my_generator():
    yield 1
    yield 2
    yield 3
    raise ValueError("Generator Exception")


def primes_generator():
    yield 2
    primes = [2]
    n = 3
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 2


def fibonacci_generator():
    yield 0
    yield 1
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def main():
    gen = my_generator()
    print(next(gen))  # 1
    print(gen.__next__())  # 2
    print(next(gen))  # 3
    # print(next(gen))  # raises ValueError: Generator Exception
    print()

    gen = primes_generator()
    print(next(gen))  # 2
    print(next(gen))  # 3
    print(next(gen))  # 5
    print(next(gen))  # 7
    print(next(gen))  # 11
    print()

    examp = (i for i in range(10))
    print(examp)
    for ex in examp:
        print(ex)
    print()

    fib = fibonacci_generator()
    print(next(fib))  # 0
    print(next(fib))  # 1
    print(next(fib))  # 1
    print(next(fib))  # 2
    print(next(fib))  # 3
    print(next(fib))  # 5
    print(next(fib))  # 8
    print()

    numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
    filtered_list = [x for x in numbers if x < 0]
    print(filtered_list)
    print()

    text = "The quick brown fox jumps over the lazy dog is an English-language " \
           "pangram—a sentence that contains all of the letters of the English alphabet"
    length_of_words = [len(x) for x in text.split() if x != "The" and x != "the"]
    print(length_of_words)
    print()

    three_d = [
        [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
        [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
    ]
    new_list = [subsublist for sublist in three_d for subsublist in sublist if len(subsublist) > 4]
    print(new_list)


if __name__ == main():
    main()
