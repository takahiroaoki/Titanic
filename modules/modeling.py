from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def modeling(dataFormodel: tuple, model: str = "LogisticRegression") -> tuple:
    X_train, X_valid, y_train, y_valid = dataFormodel

    if (model == "LogisticRegression"):
        model = LogisticRegression()
    else:
        return

    model.fit(X_train, y_train)
    accuracy_train: float = accuracy_score(y_train, model.predict(X_train))
    accuracy_valid: float = accuracy_score(y_valid, model.predict(X_valid))

    return model, {"accuracy_train": accuracy_train, "accuracy_valid": accuracy_valid}
    