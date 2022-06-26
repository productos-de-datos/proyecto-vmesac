"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #url https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls

    import wget
    #import os
    #os.chdir('data_lake/landing')

    path = 'data_lake/landing'

    different_years = [2016, 2017]

    for year_file in range(1995, 2022):
        
        if year_file in different_years:
            file_name = f'https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{year_file}.xls?raw=true'
            wget.download(file_name, out = path)
        else:
            file_name =  f'https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{year_file}.xlsx?raw=true'
            wget.download(file_name, out = path)
    return    

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    ingest_data()

    doctest.testmod()
