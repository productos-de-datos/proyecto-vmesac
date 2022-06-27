def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    df_daily_prices = pd.read_csv('data_lake/business/precios-diarios.csv')
    df_daily_prices['fecha'] = pd.to_datetime(df_daily_prices["fecha"])

    x = df_daily_prices['fecha']
    y = df_daily_prices['precio']

    plt.figure(figsize=(12, 8)) 
    plt.plot(x, y, label='Promedio Diario') 
    plt.title('Promedio Diario') 
    plt.xlabel('Fecha') 
    plt.ylabel('Precio') 
    plt.savefig("data_lake/business/reports/figures/daily_prices.png") 

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_daily_prices_plot()
