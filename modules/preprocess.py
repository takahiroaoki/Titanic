import pandas

def preprocess(data: pandas.DataFrame, targetColumn: str) -> pandas.DataFrame:
    """Returns preprocessed data as pandas.DataFrame
    params:
        data: pandas.DataFrame
            Basically, not processed data
        targetColumn: str
            The name of target column. We should take care of it because dataset for test does not usually
            have the target column.
    returns: pandas.DataFrame
        The preprocessed data
    """
    # The survival rate of male is less than that of female
    data["MaleFlg"] = (data["Sex"] == "male").values

    # The survival rate of Embarked=="C" is less than others
    data["CFlg"] = (data["Embarked"] == "C").values
    
    
    if targetColumn in data.columns:
        data = data[[targetColumn, "Pclass", "Age", "Fare", "MaleFlg", "CFlg"]]
    else:
        data = data[["Pclass", "Age", "Fare", "MaleFlg", "CFlg"]]
        
    data = data.fillna(data.mean())
    return data