"""
Documentación Pipeline:
Se crea un pipeline de luigi que permite ejecutar todas las funciones creadas anteriormente
de forma secuencial, teniendo en cuenta las dependencias que puedan existir, lo que permite automotizar y tener control sobre
la ejecución


Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.

"""
 
import luigi 
from luigi import Task, LocalTarget 
 
class task_ingestar_data(Task): 
    def output(self): 
        return LocalTarget('data_lake/landing/arc.csv') 
 
    def run(self): 
        from ingest_data import ingest_data 
        with self.output().open('w') as archivos: 
            ingest_data() 
 
 
class task_transformar_data(Task): 
    def requires(self): 
        return task_ingestar_data() 
 
    def output(self): 
        return LocalTarget('data_lake/raw/arc.txt') 
 
    def run(self): 
        from transform_data import transform_data 
        with self.output().open('w') as archivos: 
            transform_data() 
 
 
class task_limpiar_data(Task): 
    def requires(self): 
        return task_transformar_data() 
 
    def output(self): 
        return LocalTarget('data_lake/cleansed/arc.txt') 
 
    def run(self): 
        from clean_data import clean_data 
        with self.output().open('w') as archivos: 
            clean_data() 
 
 
class task_computar_precio_diario(Task): 
    def requires(self): 
        return task_limpiar_data() 
 
    def output(self): 
        return LocalTarget('data_lake/business/arc.txt') 
 
    def run(self): 
        from compute_daily_prices import compute_daily_prices 
        with self.output().open('w') as archivos: 
            compute_daily_prices() 
 
 
class task_computar_precio_mensual(Task): 
    def requires(self): 
        return task_computar_precio_diario() 
 
    def output(self): 
        return LocalTarget('data_lake/business/arc.txt') 
 
    def run(self): 
        from compute_monthly_prices import compute_monthly_prices 
        with self.output().open('w') as archivos: 
            compute_monthly_prices() 
 
 
if __name__ == '__main__': 
    luigi.run(["task_computar_precio_mensual", "--local-scheduler"]) 
 
if __name__ == "__main__": 
    import doctest 
    doctest.testmod()