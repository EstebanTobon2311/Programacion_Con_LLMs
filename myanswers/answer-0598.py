import pandas as pd


def limpiar_outliers_iqr(df, columna):

    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return df[
        (df[columna] >= lower) &
        (df[columna] <= upper)
    ]