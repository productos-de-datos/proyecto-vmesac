'''
Documentación transform_data(): Para transformar todos los archivos de excel a csv, se hace uso de la librería pandas
Dado que los archivos presentan diferentes formatos y caracteristicas se crea un condicional para dada caso y se agrupan
en él los archivos que cumplan con dichas caracteristicas, después se exporta el archivo usando el método to_csv de pandas 

'''

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd

    for year_file in range(1995, 2022):
        
        if year_file <= 1999:
            file_name = f'data_lake/landing/{year_file}.xlsx'
            df = pd.read_excel(file_name, sheet_name = 0, header = 3)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year_file}.csv'
            df.to_csv(new_file, index=False)
        
        elif year_file > 1999 and year_file <= 2015:
            file_name = f'data_lake/landing/{year_file}.xlsx'
            df = pd.read_excel(file_name, sheet_name = 0, header = 2)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year_file}.csv'
            df.to_csv(new_file, index=False)
        
        elif year_file > 2015 and year_file <= 2017:
            file_name = f'data_lake/landing/{year_file}.xls'
            df = pd.read_excel(file_name, sheet_name = 0, header = 2)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year_file}.csv'
            df.to_csv(new_file, index=False)

        else:
            file_name = f'data_lake/landing/{year_file}.xlsx'
            df = pd.read_excel(file_name,  sheet_name = 0)
            df = df.iloc[:, :25]
            new_file = f'data_lake/raw/{year_file}.csv'
            df.to_csv(new_file, index=False)
            
    return    

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    transform_data()

    doctest.testmod()
