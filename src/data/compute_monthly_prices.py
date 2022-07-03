'''
Documentación compute_monthly_prices(): se agrupa el archivo por mes, para esto se extraen los ultimos
7 caracteres del campo fecha que contienen el año y el mes(se añade el 1 simbolicamente para indicar el primer dia del mes en todas las filas)
se agrupa por este campo y se le calcula la media a los datos con el método grupby de pandas, se exporta el archivo 
a la carpeta indicada
'''

def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional
    """

    import pandas as pd

    hourly_prices_df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    hourly_prices_df = hourly_prices_df[['fecha', 'precio']]
    hourly_prices_df['mes'] = hourly_prices_df['fecha'].str[:7] + '-01'
    
    monthly_prices_df = hourly_prices_df.groupby('mes', as_index = False).mean()
    monthly_prices_df.columns = ['fecha', 'precio']
    monthly_prices_df.to_csv('data_lake/business/precios-mensuales.csv', index=False)

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
