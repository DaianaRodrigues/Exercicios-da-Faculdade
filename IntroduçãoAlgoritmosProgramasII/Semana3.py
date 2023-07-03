def countdown(n):
    if n <= 0:
        print('Lançar!!!')
    else:
        print(n)
        countdown(n - 1)


print(countdown(3))


# Exercicio 10.1
def reverse(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        reverse(n // 10)


print(reverse(56981))


# Exercicio 10.2
def saude(n):
    if n == 0:
        print('Hurrah!!')
    else:
        print('Hip', end=' ')
        saude(n - 1)


print(saude(5))


# Exercicio 10.3
def factorial(n):
    if n in [0, 1]:
        return 1
    return factorial(n - 1) * n


print(factorial(5))


def pattern(n):
    if n == 0:
        print(0, end=' ')
    else:
        pattern(n - 1)
        print(n, end=' ')
        pattern(n - 1)


# Exercicio 10.4
def pattern2(n):
    if n > 0:
        pattern2(n - 1)
        print(n * '*')
        pattern2(n - 1)


print(pattern2(4))


def koch(n):
    if n == 0:
        return 'F'

    tmp = koch(n - 1)

    return tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp


from turtle import Screen, Turtle


def drawkoch(n):
    s = Screen()
    t = Turtle()
    directions = koch(n)

    for move in directions:
        if move == 'F':
            t.forward(300 / 3 ** n)
        if move == 'L':
            t.lt(60)
        if move == 'R':
            t.rt(120)
    s.bye()


print(drawkoch(1))


# Exercicio 10.5
def drawSnowflake(n):
    s = Screen()
    t = Turtle
    directions = koch(n)
    for i in range(3):
        for move in directions:
            if move == 'F':
                t.fd(300 / 3 ** n)
            if move == 'L':
                t.lt(60)
            if move == 'R':
                t.rt(120)
        t.rt(120)
    s.bye()

def power(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res

def rpower(a, n):
    global counter

    if n == 0:
        return 1
    tmp = rpower(a, n//2)

    if n % 2 == 0:
        return tmp*tmp
    else:
        return a*tmp*tmp

import time
def timing(func, n):
    funcInput = buildInput(n)

    start = time.time()
    func(funcInput)
    end = time.time()

    return end - start

def buildInput(n):

    return n

def timingAnalysis(func, start, stop, inc, runs):
    for n in range(start, stop, inc):
        acc = 0.0

        for i in range(runs):
            acc += timing(func, n)

        formatStr = 'Tempo de execução de {}({}) é {:.7f} segundos.'
        print(formatStr.format(func.__name__, n, acc/runs))
