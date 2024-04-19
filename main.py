import math as m
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fib/{num}")
def fib_seq_check(num: int):
    if is_fibbonaci(num):
        message = calc_next_fib(num)
    else:
        message = "not a Fibonacci number."
    return {"message": message}

# Apparently, the fibbonaci sequence has a nice mathematical property to determine whether a number is part of the
# sequence.
# R is a Fibinacci number only if at least one of (5 * R * R + 4) or (5 * R * R - 4) are perfect squares

def is_perfect_square(num: int) -> bool:
    sqrt = int(m.sqrt(num))
    return sqrt * sqrt == num


def is_fibbonaci(num: int) -> bool:
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


def calc_next_fib(num: int) -> int:
    return 2

