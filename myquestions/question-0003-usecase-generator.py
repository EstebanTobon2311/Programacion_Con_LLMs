import numpy as np
import random
from sklearn.decomposition import PCA

def generar_caso_de_uso_pca_varianza_minima():

    n_samples = random.randint(20, 60)
    n_features = random.randint(4, 8)

    X = np.random.randn(n_samples, n_features)

    varianza_objetivo = random.uniform(0.8, 0.95)

    input_data = {
        'X': X.copy(),
        'varianza_objetivo': varianza_objetivo
    }

    modelo = PCA(n_components=varianza_objetivo)

    X_transformado = modelo.fit_transform(X)

    n_componentes = modelo.n_components_

    output_data = (X_transformado, n_componentes)

    return input_data, output_data

if __name__ == "__main__":
    input_data, output_data = generar_caso_de_uso_pca_varianza_minima()

    print("INPUT:")
    print(input_data)

    print("\nOUTPUT:")
    print(output_data)