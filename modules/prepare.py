import pandas

def getRawData(filePath: str) -> pandas.DataFrame:
    """Returns raw dataset as pandas.DataFrame
    params:
        filePath: str
            The absolute path to dataset.
    return: pandas.DataFrame
        Raw dataset
    """
    return pandas.read_csv(filePath)