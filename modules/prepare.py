import pandas

def getRawData(file_path: str) -> pandas.DataFrame:
    return pandas.read_csv(file_path)