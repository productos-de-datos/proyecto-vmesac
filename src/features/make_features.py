'''
Documentación make_features(): crea las variables  o features necesarios para crear un modelo que pronostique los datos
para esto se aplica una transformacion logaritmica a la serie de tiempo y se crean 2 columnas adicionales:
 precio_lag_12: el precio de la energia 12 meses atras del mes actual (lag 12)
 y el logaritmo de estra nueva variable
'''

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    import pandas as pd
    import numpy as np
    
    df_daily_prices = pd.read_csv('data_lake/business/precios-diarios.csv')
    df_daily_prices['log_precio'] = np.log(df_daily_prices['precio'])
    df_daily_prices['precio_lag_12'] = df_daily_prices.precio.shift(12)
    df_daily_prices['log_precio_lag_12'] = np.log(df_daily_prices['precio_lag_12'])
    df_daily_prices.to_csv('data_lake/business/features/precios-diarios.csv', index=False)

    return

    raise NotImplementedError("Implementar esta función")


import pytest
def test_make_features():
    """Evalua la creación de características para modelos"""
    import pandas as pd

    make_features()

    df_to_test = pd.read_csv('data_lake/business/features/precios-diarios.csv')

    assert df_to_test.empty is False


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
