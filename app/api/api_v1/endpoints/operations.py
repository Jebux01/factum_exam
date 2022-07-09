from typing import Any, List, Optional, Union
from fastapi import APIRouter, status, HTTPException, Query
import random
import statistics
router = APIRouter()


@router.get("operaciones/{value_min}/{value_max}/{num_generate}/{explicit}")
def operations_random(num_generate: int, value_min: int = 0, value_max: int = 99, explicit: Optional[bool] = False) -> Any:
    random_numbers = []
    for n in range(0, num_generate): # numero de iteraciones dada el numero a generar
        number_random = random.randint(value_min, value_max) # obtenemos valor random en base al numero minimo y maximo
        random_numbers.append(number_random)

    sum_all = sum(random_numbers)
    mean = statistics.mean(random_numbers)
    min_value = min(random_numbers)
    max_value = max(random_numbers)
    _range = list(range(min_value, max_value)) if explicit else [min_value, max_value]
    return {
        "Promedio": mean,
        "Suma": sum_all,
        "Minimo": min_value,
        "Maximo": max_value,
        "Rango": _range
    }
