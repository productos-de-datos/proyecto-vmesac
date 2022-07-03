'''
Documentación train_daily_model(): se hace uso del archivo de precios diarios con los features, se limpian los valores faltantes
y se defininen los X y y para el entrenamiento del modelo. Se hace uso de una red neuronal para pronosticar la serie
de tiempo con base en la variable transformada (logaritmo del precio 12 días atrás), se ajusta el modelo y se guarda suando la libreria pickle

'''

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl

    """
    import pandas as pd 
    import numpy as np
    from sklearn.neural_network import MLPRegressor
    import pickle

    # Preparación datos: definición de X y y
    df_train = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    df_model = df_train.dropna()
    X = df_model.iloc[:, -1]
    X = np.array(X).reshape(-1, 1)
    y = df_model.iloc[:, 2]

    # Creación del modelo
    H=1
    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=10000,
        )

    # Entrenamiento
    #mlp.fit(X, y)  
    mlp.fit(X[:7000], y[:7000])   # en caso de tomar solo mustra de entrenamiento

    # Salvar modelo .pkl
    pickle.dump(mlp, open('src/models/precios-diarios.pkl', 'wb'))

    return

    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
