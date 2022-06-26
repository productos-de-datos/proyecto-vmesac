def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd

    main_df = pd.DataFrame(columns=['fecha', 'hora', 'precio'])

    for year_file in range(1997, 2022):

        df = pd.read_csv(f'data_lake/raw/{year_file}.csv')

        df_unpivot = pd.melt(df, id_vars='Fecha', value_vars=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'])
        df_unpivot.columns = ['fecha', 'hora', 'precio']
        df_unpivot_sorted = df_unpivot.sort_values(by=['fecha', 'hora'], ignore_index=True)
        
        main_df = main_df.append(df_unpivot_sorted)

    main_df.to_csv('data_lake/cleansed/precios-horarios.csv', index=False)    

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
