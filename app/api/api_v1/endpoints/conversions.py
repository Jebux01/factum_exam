from typing import List, Union
from fastapi import APIRouter, status, HTTPException, Query
from app.constants.conversions import *
router = APIRouter()


@router.get("temperature/{type}/{value}")
def temperature_conversion(type: TypeConversionsTemperature, value: float) -> str:
    valor = generate_conversions_temperature(type=type, value=value)
    return f"La conversion del valor {value} en {type.value} es {valor}"

    

def generate_conversions_temperature(type: TypeConversionsTemperature, value: int):
    multiply = 1.8
    k = 273.15
    c = 32
    data = {
        TypeConversionsTemperature.C_TO_F: (value * multiply) + c,
        TypeConversionsTemperature.F_TO_C: (value - c) / multiply,
        TypeConversionsTemperature.C_TO_K: value + k,
        TypeConversionsTemperature.K_TO_C: value - k,
        TypeConversionsTemperature.F_TO_K: ((value - c) * multiply) + k,
        TypeConversionsTemperature.K_TO_F: ((value - k) * multiply) + c
    }

    return round(data[type], 2)


@router.get("weight/{type}/{value}")
def weight_conversion(type: TypeConversionsWeight, value: float) -> str:
    valor = generate_conversions_weight(type=type, value=value)
    return f"La conversion del valor {value} en {type.value} es {valor}"


def generate_conversions_weight(type: TypeConversionsWeight, value: float):

    base_g_k = 1000
    div_b_g = 28.35
    base_g_l = 453.60
    base_k_l = 2.205
    base_k_o = 35.274
    base_o_l = 16
    data = {
        TypeConversionsWeight.G_TO_K: value / base_g_k,
        TypeConversionsWeight.G_TO_O: value / div_b_g,
        TypeConversionsWeight.G_TO_L: value / base_g_l,
        TypeConversionsWeight.K_TO_G: value * base_g_k,
        TypeConversionsWeight.K_TO_L: value * base_k_l,
        TypeConversionsWeight.K_TO_O: value * base_k_o,
        TypeConversionsWeight.O_TO_G: value * div_b_g,
        TypeConversionsWeight.O_TO_K: value / base_k_o,
        TypeConversionsWeight.O_TO_L: value / base_o_l,
        TypeConversionsWeight.L_TO_G: value * base_g_l,
        TypeConversionsWeight.L_TO_K: value / base_k_l,
        TypeConversionsWeight.L_TO_O: value * base_o_l
    }

    return round(data[type], 2)


@router.get("length/{type}/{value}")
def length_conversion(type: TypeConversionsLength, value: float):
    valor = generate_conversions_lenght(type=type, value=value)
    return f"La conversion del valor {value} en {type.value} es {valor}"

def generate_conversions_lenght(type: TypeConversionsLength, value: float):
    base_k = 100000
    base_mlc = 160900
    base_my = 91.44
    base_cp = 2.54
    base_cpi = 30.48
    base_mk = 1000
    base_p = 39.37
    base_y = 1.094
    base_mlp = 63360
    base_pi = 3281
    base_mlpi = 5280
    base_ypi = 3
    base_mly = 1760
    base_pp = 12

    data = {
        TypeConversionsLength.C_TO_M: value * (base_k / 1000),
        TypeConversionsLength.C_TO_K: value / base_k,
        TypeConversionsLength.C_TO_ML: value / base_mlc,
        TypeConversionsLength.C_TO_P: value / base_cp,
        TypeConversionsLength.C_TO_PI: value / base_cpi,
        TypeConversionsLength.C_TO_Y: value / base_my,
        TypeConversionsLength.M_TO_C: value * (base_k / 1000),
        TypeConversionsLength.M_TO_K: value / base_mk,
        TypeConversionsLength.M_TO_P: value * base_p,
        TypeConversionsLength.M_TO_Y: value * base_y,
        TypeConversionsLength.M_TO_ML: value / (base_mlc / 100),
        TypeConversionsLength.P_TO_C: value * base_cp,
        TypeConversionsLength.P_TO_M: value * base_p,
        TypeConversionsLength.P_TO_K: value / (base_p * 1000),
        TypeConversionsLength.P_TO_PI: value / base_pp,
        TypeConversionsLength.P_TO_Y: value / (base_pp * 3),
        TypeConversionsLength.P_TO_ML: value / base_mlp,
        TypeConversionsLength.PI_TO_C: value * base_cpi,
        TypeConversionsLength.PI_TO_K: value / base_pi,
        TypeConversionsLength.PI_TO_M: value / (base_pi / 1000),
        TypeConversionsLength.PI_TO_ML: value / base_mlpi,
        TypeConversionsLength.PI_TO_P: value * base_pp,
        TypeConversionsLength.PI_TO_Y: value / base_ypi,
        TypeConversionsLength.Y_TO_C: value * base_my,
        TypeConversionsLength.Y_TO_M: value / base_y,
        TypeConversionsLength.Y_TO_K: value / (base_y * 1000),
        TypeConversionsLength.Y_TO_P: value * (base_pp * 3),
        TypeConversionsLength.Y_TO_PI: value * base_ypi,
        TypeConversionsLength.Y_TO_ML: value / base_mly,
        TypeConversionsLength.ML_TO_C: value * base_mlc,
        TypeConversionsLength.ML_TO_M: value * (base_mlc / 100),
        TypeConversionsLength.ML_TO_K: value * (base_mlc / 1000),
        TypeConversionsLength.ML_TO_P: value * base_mlp,
        TypeConversionsLength.ML_TO_PI: value * base_mlpi,
        TypeConversionsLength.ML_TO_Y: value * base_mly
    }

    return round(data[type], 2)

@router.get("volumes/{type}/{value}")
def volumes_conversion(type: TypeConversionsVolumes, value: float) -> str:
    valor = generate_conversions_volumes(type=type, value=value)
    return f"La conversion del valor {value} en {type.value} es {valor}"

def generate_conversions_volumes(type: TypeConversionsVolumes, value: float):
    data = {
        TypeConversionsVolumes.M_TO_L: value,
        TypeConversionsVolumes.M_TO_G: value,
        TypeConversionsVolumes.L_TO_M: value,
        TypeConversionsVolumes.L_TO_G: value,
        TypeConversionsVolumes.G_TO_L: value,
        TypeConversionsVolumes.G_TO_M: value
    }

    return round(data[type], 2)


@router.get("volumes/{type}/{value}")
def storage_conversion(type: TypeConversionsStorage, value: float) -> str:
    valor = generate_conversions_storage(type=type, value=value)
    return f"La conversion del valor {value} en {type.value} es {valor}"

def generate_conversions_storage(type: TypeConversionsVolumes, value: float):

    base = 1024
    data = {
        TypeConversionsStorage.B_TO_M: value / base**2,
        TypeConversionsStorage.B_TO_G: value / base**3,
        TypeConversionsStorage.B_TO_T: value / base**4,
        TypeConversionsStorage.M_TO_B: value * base**2,
        TypeConversionsStorage.M_TO_G: value / base,
        TypeConversionsStorage.M_TO_T: value * base**2,
        TypeConversionsStorage.G_TO_B: value * base**3,
        TypeConversionsStorage.G_TO_M: value * base,
        TypeConversionsStorage.G_TO_T: value / base,
        TypeConversionsStorage.T_TO_B: value * base**4,
        TypeConversionsStorage.T_TO_M: value / base**3,
        TypeConversionsStorage.T_TO_G: value * base
    }

    return round(data[type], 2)