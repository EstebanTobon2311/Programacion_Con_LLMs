import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor


def detectar_convergencia(df, target_col, fracciones, umbral, random_state):

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=random_state
    )

    scaler = StandardScaler()

    X_train_sc = scaler.fit_transform(X_train)
    X_test_sc = scaler.transform(X_test)

    rmses = []

    for fraccion in fracciones:

        n = max(2, int(len(X_train_sc) * fraccion))

        X_sub = X_train_sc[:n]
        y_sub = y_train.iloc[:n]

        model = GradientBoostingRegressor(
            n_estimators=50,
            random_state=random_state
        )

        model.fit(X_sub, y_sub)

        y_pred = model.predict(X_test_sc)

        rmse = np.sqrt(
            np.mean((y_test.values - y_pred) ** 2)
        )

        rmses.append(rmse)

    for i in range(1, len(rmses)):

        mejora_relativa = (
            (rmses[i - 1] - rmses[i]) / rmses[i - 1]
        )

        if mejora_relativa < umbral:
            return int(i)

    return int(len(fracciones) - 1)