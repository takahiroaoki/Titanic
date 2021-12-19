import pandas

def getRawData(filePath: str) -> pandas.DataFrame:
    return pandas.read_csv(filePath)