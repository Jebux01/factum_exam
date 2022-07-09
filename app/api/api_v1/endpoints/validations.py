
from typing import List
from fastapi import APIRouter, status, HTTPException

import math
router = APIRouter()

@router.get("fibonacci/{number}")
def validate_is_fibonacci(number: int) -> str:

    def is_perfect(number: int):
        check = int(math.sqrt(number))
        return check*check == number

    first_val = (5*number*number + 4)
    second_val = (5*number*number - 4)
    perfect = is_perfect(number=first_val) or is_perfect(number=second_val)
    if perfect:
        message = f"El numero {number} pertene a la serie Fibonacci"
    else:
        message = f"El numero {number} no pertene a la serie Fibonacci"
    return message


@router.get("factoria/{number}")
def validate_is_factorial(number: int) -> str:
    if number > 0:
        return {"message": """
            Es factorial

            La cantidad de factores que tienen los números sirve para clasificarlos en primos y compuestos.
            Los primeros tienen sólo dos factores, mientras que los segundos cuentan con más de dos.
            El número uno no es primo ni compuesto, porque tiene un sólo factor: él mismo.
        """}

@router.get("primo/{number}")
def validate_is_primo(number: int) -> str:
    if number <= 2:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="El numero ingresa no se permite por favor ingresa otro")

    for n in range(2, number):
        if number % n == 0:
            return f"El numero {number} no es primo"

        return f"El numero {number} es primo"

@router.get("palindromo/{number}")
def validate_is_palindromo(number: int) -> str:
    return f"El numero {number} es un palindromo" if str(number) == str(number)[::-1] else f"El numero {number} no es un palindromo"