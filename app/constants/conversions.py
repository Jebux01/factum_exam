from enum import Enum

class TypeConversionsTemperature(Enum):
    C_TO_F = "CELSIUS A FAHRENHEIT"
    C_TO_K = "CELSIUS A KELVIN"
    F_TO_C = "FAHRENHEIT A CELSIUS"
    F_TO_K = "FAHRENHEIT A KELVIN"
    K_TO_C = "KELVIN A CELSIUS"
    K_TO_F = "KELVIN A FAHRENHEIT"

class TypeConversionsWeight(Enum):
    G_TO_K = "GRAMOS A KILOS"
    G_TO_O = "GRAMOS A ONZAS"
    G_TO_L = "GRAMOS A LIBRAS"
    K_TO_G = "KILOS A GRAMOS"
    K_TO_O = "KILOS A ONZAS"
    K_TO_L = "KILOS A LIBRAS"
    O_TO_G = "ONZAS A GRAMOS"
    O_TO_K = "ONZAS A KILOS"
    O_TO_L = "ONZAS A LIBRAS"
    L_TO_K = "LIBRAS A KILOS"
    L_TO_G = "LIBRAS A GRAMOS"
    L_TO_O = "LIBRAS A ONZAS"

class TypeConversionsLength(Enum):
    C_TO_M = "CENTIMENTROS A METROS"
    C_TO_K = "CENTIMENTROS A KILOMENTROS"
    C_TO_P = "CENTIMETROS A PULGADAS"
    C_TO_PI = "CENTIMENTROS A PIES"
    C_TO_Y = "CENTIMENTROS A YARDAS"
    C_TO_ML = "CENTIMENTROS A MILLAS"

    M_TO_C = "METROS A CENTIMENTROS"
    M_TO_K = "METROS A KILOMETROS"
    M_TO_P = "METROS A PULGADAS"
    M_TO_PI = "METROS A PIES"
    M_TO_Y = "METROS A YARDAS"
    M_TO_ML = "METROS A MILLAS"

    K_TO_M = "KILOMENTROS A METROS"
    K_TO_C = "KILOMENTROS A CENTIMETROS"
    K_TO_P = "KILOMETROS A PULGADAS"
    K_TO_PI = "KILOMETROS A PIES"
    K_TO_Y = "KILOMETROS  A YARDAS"
    K_TO_ML = "KILOMETROS A MILLAS"

    P_TO_M = "PULGADAS A METROS"
    P_TO_C = "PULGADAS A CENTIMENTROS"
    P_TO_K = "PULGADAS A KILOMETROS"
    P_TO_PI = "PULGADAS A PIES"
    P_TO_Y = "PULGADAS A YARDAS"
    P_TO_ML = "PULGADAS A MILLAS"

    PI_TO_M = "PIES A METROS"
    PI_TO_C = "PIES A CENTIMETROS"
    PI_TO_K = "PIES A KILOMETROS"
    PI_TO_P = "PIES A PULGADAS"
    PI_TO_Y = "PIES A YARDAS"
    PI_TO_ML = "PIES A MILLAS"
    
    Y_TO_C = "YARDAS A CENTIMETROS"
    Y_TO_M = "YARDAS A METROS"
    Y_TO_K = "YARDAS A KILOMETROS"
    Y_TO_P = "YARDAS A PULGADAS"
    Y_TO_PI = "YARDAS A PIES"
    Y_TO_ML = "YARDAS A MILLAS"
    
    ML_TO_C = "MILLAS A CENTIMETROS"
    ML_TO_M = "MILLAS A METROS"
    ML_TO_K = "MILLAS A KILOMETROS"
    ML_TO_P = "MILLAS A PULGADAS"
    ML_TO_PI = "MILLAS A PIES"
    ML_TO_Y = "MILLAS A YARDAS"

class TypeConversionsVolumes(Enum):
    M_TO_L = "MILILITROS A LITROS"
    M_TO_G = "MILILITROS A GALONES"

    L_TO_M = "LITROS A MILILITROS"
    L_TO_G = "LITROS A GALONES"
    
    G_TO_M = "GALONES A MILILITROS"
    G_TO_L = "GALONES A LITROS"

class TypeConversionsStorage(Enum):
    B_TO_M = "BYTES A MEGA"
    B_TO_G = "BYTES A GIGA"
    B_TO_T = "BYTES A TERA"


    M_TO_B = "MEGA A BYTES"
    M_TO_G = "MEGA A GIGA"
    M_TO_T = "MEGA A TERAS"

    G_TO_B = "GIGA A BYTES"
    G_TO_M = "GIGAS A MEGAS"
    G_TO_T = "GIGAS A TERAS"

    T_TO_B = "TERAS A BYTES"
    T_TO_M = "TERAS A MEGAS"
    T_TO_G = "TERAS A GIGAS"