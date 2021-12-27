from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def modeling(dataForModel: tuple, model: str = "LogisticRegression") -> tuple:
    """Returns trained model and its accuracy score
    params:
        dataForModel: tuple<pandas.DataFrame>
            Its length is 4, and its elements are X_train, X_valid, y_train, y_valid in order.
        model: str
            The name of machine learning model. In this notebook, LogisticRegression only.
            When unknown name are assigned, return None
    return: tuple<(machine learning model), tuple<float>>
        The first element is trained model.
        The second element is dictionary which accuracy score of 'train' and 'valid' are in it.
    """
    X_train, X_valid, y_train, y_valid = dataForModel

    if (model == "LogisticRegression"):
        model = LogisticRegression()
    else:
        return None

    model.fit(X_train, y_train)
    accuracy_train: float = accuracy_score(y_train, model.predict(X_train))
    accuracy_valid: float = accuracy_score(y_valid, model.predict(X_valid))

    return model, {"accuracy_train": accuracy_train, "accuracy_valid": accuracy_valid}
    