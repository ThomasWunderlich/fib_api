import math as m
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fib/{num}")
def fib_seq_check(num: int):
    # FastAPI probably has a nice way to typecheck params but this will do for now
    if not isinstance(num, int):
        return "Error: num must be an integer."

    if is_fibbonaci(num):
        return calc_next_fib(num)
    else:
        return "not a Fibonacci number."

# Apparently, the Fibonacci sequence has a nice mathematical property to determine whether a number is part of the
# sequence.
# R is a Fibonacci number only if at least one of (5 * R * R + 4) or (5 * R * R - 4) are perfect squares

def is_perfect_square(num: int) -> bool:
    sqrt = int(m.sqrt(num))
    return sqrt * sqrt == num


def is_fibbonaci(num: int) -> bool:
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


# unsurprisingly, there's a similar mathematical property for calculating the next item in the fib seq
def calc_next_fib(num: int) -> int:
    return round(num * (1 + m.sqrt(5)) / 2.0)

