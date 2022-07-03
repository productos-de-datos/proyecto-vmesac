'''
Documentación create_data_lake():
Esta función crea el datalake, o el directorio de trabajo del proyecto, haciendo uso de la función 
makedirs de la libreria OS, que permite crear directorios intermedios y finales simultaneamente, estos directorios
serán usados durente el proyecto para almacenar los archivos que se va generando y los resultados finales.

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

