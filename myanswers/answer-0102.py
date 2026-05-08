from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


def optimizar_random_forest(X, y, param_grid, cv=5):

    rf = RandomForestClassifier(random_state=42)

    grid_search = GridSearchCV(
        rf,
        param_grid,
        cv=cv,
        scoring='accuracy',
        return_train_score=False
    )

    grid_search.fit(X, y)

    resultado = {
        'best_params': grid_search.best_params_,
        'best_score': grid_search.best_score_,
        'best_estimator': grid_search.best_estimator_
    }

    return resultado