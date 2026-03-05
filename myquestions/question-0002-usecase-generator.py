import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_suavizar_temperaturas():

    n = random.randint(20, 50)

    fechas = pd.date_range("2024-01-01", periods=n, freq="H")

    df = pd.DataFrame({
        'fecha_hora': fechas.astype(str),
        'temperatura': np.random.uniform(10, 35, n)
    })

    ventana = random.randint(2, 5)

    input_data = {
        'df': df.copy(),
        'ventana': ventana
    }

    df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])

    resultado = (
        df
        .set_index('fecha_hora')[['temperatura']]
        .rolling(ventana)
        .mean()
        .dropna()
    )

    output_data = resultado

    return input_data, output_data

if __name__ == "__main__":
    input_data, output_data = generar_caso_de_uso_suavizar_temperaturas()

    print("INPUT:")
    print(input_data)

    print("\nOUTPUT:")
    print(output_data)