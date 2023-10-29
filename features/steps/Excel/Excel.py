from pandas import read_excel
from pandas.core.frame import DataFrame


class Excel:

    def __init__(self, excel_path: str):
        self.excel_path = excel_path
        self.excel_dataframe = self.read_exel_data_to_df()

    def find_value_in_column(self, column: str, value: str) -> DataFrame:
        return self.excel_dataframe[self.excel_dataframe[column] == value]

    def read_exel_data_to_df(self, exel_path) -> DataFrame:
        return read_excel(exel_path)
