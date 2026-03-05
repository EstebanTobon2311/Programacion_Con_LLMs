import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_top_categorias_ingresos():

    categorias = ['A', 'B', 'C', 'D', 'E']

    n = random.randint(10, 30)

    df = pd.DataFrame({
        'categoria': np.random.choice(categorias, n),
        'precio': np.random.uniform(5, 100, n),
        'cantidad_vendida': np.random.randint(1, 20, n)
    })

    umbral_cantidad = random.randint(3, 10)
    n_top = random.randint(1, 3)

    input_data = {
        'df': df.copy(),
        'umbral_cantidad': umbral_cantidad,
        'n_top': n_top
    }

    df_filtrado = df[df['cantidad_vendida'] >= umbral_cantidad].copy()

    df_filtrado['ingreso_total'] = df_filtrado['precio'] * df_filtrado['cantidad_vendida']

    resultado = (
        df_filtrado
        .groupby('categoria')['ingreso_total']
        .sum()
        .sort_values(ascending=False)
        .head(n_top)
    )

    output_data = resultado

    return input_data, output_data

if __name__ == "__main__":
    input_data, output_data = generar_caso_de_uso_top_categorias_ingresos()

    print("INPUT:")
    print(input_data)

    print("\nOUTPUT:")
    print(output_data)