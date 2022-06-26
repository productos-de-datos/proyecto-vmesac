def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    import pandas as pd

    hourly_prices_df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    hourly_prices_df = hourly_prices_df[['fecha', 'precio']]
    
    daily_prices_df = hourly_prices_df.groupby(['fecha'], as_index = False ).mean()  
    daily_prices_df.to_csv('data_lake/business/precios-diarios.csv', index=False) 

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
