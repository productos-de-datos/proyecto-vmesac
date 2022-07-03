"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
Permite descargar a la carpeta Landing del datalake los archivos que se usaran para el proyecto,
se hace uso de la librería wget y del m{etodo download para descargar los archivos a través de la url, y la información de cada uno, 
cómo el año (que hace parte del nombre del archivo) y su extensión. Se creo un ciclo for para hacer cambiar la variable año y 
un condicional segun el tipo de archivo: xls o xlsx

"""

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #url https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls

    import wget

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
