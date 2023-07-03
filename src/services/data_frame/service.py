import base64
from typing import BinaryIO, NoReturn

import loglifos
from pandas import DataFrame, read_csv

from src.domain.enums.data_frame.regex import Replace
from src.domain.enums.data_frame.filter import ColumnsName, CnpjQuery
from src.domain.exceptions.service.exception import ErrorTryingToConvertCsv

loglifos.set_config(log_level=loglifos.DEBUG)


class DataFrameService:

    @classmethod
    async def convert_csv_to_df(cls, spooled_file: BinaryIO) -> DataFrame:
        try:
            df = read_csv(spooled_file, dtype=str)

        except Exception as ex:
            loglifos.error(msg="convert_to_df_unexpected_error", exception=ex)

            raise ErrorTryingToConvertCsv()

        treated_df = await cls.treat_partners_df(df=df)
        filtered_partners_df = await cls.filter_df_by_valid_cnpj(treated_df=treated_df)
        await cls.log_all_invalid_cnpj(treated_df=treated_df)

        return filtered_partners_df

    @staticmethod
    async def treat_partners_df(df: DataFrame) -> DataFrame:
        all_columns = [column for column in ColumnsName]
        df = df.set_axis(all_columns, axis='columns')

        select_columns = [ColumnsName.CNPJ, ColumnsName.PHONE, ColumnsName.ZIPCODE]
        df[select_columns] = df[select_columns].replace(
            to_replace=Replace.SPECIAL_CHARACTERS, value='', regex=True
        )

        return df

    @staticmethod
    async def filter_df_by_valid_cnpj(treated_df: DataFrame) -> DataFrame:
        filtered_partners_df = treated_df.query(CnpjQuery.equal_14_digits)
        return filtered_partners_df

    @staticmethod
    async def log_all_invalid_cnpj(treated_df: DataFrame) -> NoReturn:
        invalid_cnpj_df = treated_df.query(CnpjQuery.not_equal_14_digits)
        invalid_cnpj_list = [row["cnpj"] for index, row in invalid_cnpj_df.iterrows()]
        msg = {"invalid_cnpj_from_csv": invalid_cnpj_list}
        loglifos.info(msg=msg)
