
from re import L
from typing import List, Union
from fastapi import APIRouter, status, HTTPException, Query

import math as MH
router = APIRouter()


@router.get("fibonacci/{number_iterations}")
def generate_fibonacci(number_iterations: int) -> List:
    first_val = 0
    second_val = 1
    fibonacci = []
    for n in range(0, number_iterations):
        if n <= 1:
            next = n
        else:
            next = first_val + second_val
            first_val = second_val
            second_val = next

        fibonacci.append(next)

    return fibonacci


@router.get("collatz/{number}")
def generate_collatz(number: int) -> List:
    if number < 0 or number > 25:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="El numero ingresa no se permite por favor ingres uno dentro del rango")

    collatz = []
    collatz.append(number)
    
    while number > 1:
        if number % 2 == 0:
            number = (number / 2)
            collatz.append(number)
        else:
            number = (number * 3) + 1
            collatz.append(number)
    else:
        collatz.append(number)

    return collatz


@router.get("factorial/{number}")
def obtain_factorial(number: int, math: bool = False) -> str:
    if number < 0:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="El factorial de numeros negativos no existe")
    
    if math:
        return f"{MH.factorial(number)} es el factorial del numero: {number}"

    factorial_init = 1
    while(number > 1):
        factorial_init *= number
        number -= number

    return f"{factorial_init} es el factorial del numero: {number}"

@router.get("IMC/{height}/{weight}")
def calculate_imc(height: float, weight: float) -> str:
    return round(weight / (height**2), 2)