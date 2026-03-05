import numpy as np
import random
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def generar_caso_de_uso_evaluar_kmeans_silhouette():

    n_samples = random.randint(30, 80)
    n_features = random.randint(2, 5)

    X = np.random.randn(n_samples, n_features)

    k = random.randint(2, 5)

    input_data = {
        'X': X.copy(),
        'k': k
    }

    modelo = KMeans(n_clusters=k, n_init=10)

    labels = modelo.fit_predict(X)

    score = silhouette_score(X, labels)

    output_data = score

    return input_data, output_data

if __name__ == "__main__":
    input_data, output_data = generar_caso_de_uso_evaluar_kmeans_silhouette()

    print("INPUT:")
    print(input_data)

    print("\nOUTPUT:")
    print(output_data)