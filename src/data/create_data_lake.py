'''
Esta función crea el datalake haciendo uso de la función makedirs de la libreria OS,
que permite crear directorios intermedios y finales simultaneamente.
'''

def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```

    """
    import os

    os.makedirs('data_lake/business/reports/figures')
    os.makedirs('data_lake/business/features')
    os.makedirs('data_lake/business/forecasts')
    os.makedirs('data_lake/cleansed')
    os.makedirs('data_lake/landing')
    os.makedirs('data_lake/raw')

    return

    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    # llamado función
    create_data_lake()

    doctest.testmod()

