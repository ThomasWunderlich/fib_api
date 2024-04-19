from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fib/{num}")
def read_item(num: int, ):
    if is_fibbonaci(num):
        message = calc_next_fib(num)
    else:
        message = "not a Fibonacci number."
    return {"message": message}


def is_fibbonaci(num: int) -> bool:
    return True

def calc_next_fib(num: int) -> int:
    return 2

