import pandas

def preprocess(data: pandas.DataFrame, targetColumn: str) -> pandas.DataFrame:
    if targetColumn in data.columns:
        data = data[[targetColumn, 'Pclass', 'Age', 'Fare']]
    else:
        data = data[['Pclass', 'Age', 'Fare']]
        
    data = data.fillna(data.mean())
    return data