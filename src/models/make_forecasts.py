'''
Documentación make_forecasts(): se leen los datos a pronosticar y se hace uso del archivo .pkl para realizar 
el pronóstico, se guardan los resultados en el archivo indicado

'''

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pickle
    import pandas as pd 
    import numpy as np

    # lectura datos
    df_complete = pd.read_csv('data_lake/business/features/precios-diarios.csv').dropna()
    df = df_complete.iloc[7001:-1, :] # sólo muestra testing

    # Carga modelo y predice
    pickled_model = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    df['pronostico_log'] = pickled_model.predict(np.array(df.log_precio_lag_12).reshape(-1, 1))
    df['pronostico'] = np.exp(df['pronostico_log'])

    # limpiar archivo
    df_forecast = df.drop(['log_precio', 'precio_lag_12', 'log_precio_lag_12', 'pronostico_log'], axis = 1)

    # exportar archivo
    df_forecast.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=False)

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
