import time
import random


def print_hi(name, age):
    for i in range(10):
        print(f'Hello, {name}')
        time.random.randint(1, 3)
        if i//2 == 0:
            print(f'your age is {age}')


if __name__ == '__main__':
    print_hi('PyCharm')
