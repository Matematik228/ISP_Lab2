import random


def gen(num, min_val, max_val):
    with open('numbers.txt', 'w') as outf:
        for _ in range(num):
            outf.write(str(random.randint(min_val, max_val)) + '\n')


if __name__ == '__main__':
    gen(5000000, -1000000, 1000000)