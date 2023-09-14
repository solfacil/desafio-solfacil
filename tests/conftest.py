import os

from fastapi import UploadFile
from pytest_asyncio import fixture

from src.services.data_frame.service import DataFrameService
from tests import ROOT_DIR

FILE_PATH = os.path.join(ROOT_DIR, 'assets/exemplo.csv')

@fixture(scope="function")
def upload_file():
    upload_file = UploadFile(file=open(FILE_PATH, 'rb'), filename='exemplo.csv')
    return upload_file

@fixture(scope="function")
def wrong_file_ext():
    upload_file = UploadFile(file=open(FILE_PATH, 'rb'), filename='exemplo.docx')
    return upload_file

@fixture(scope="function")
async def partners_df(upload_file):
    df = await DataFrameService.convert_csv_to_df(spooled_file=upload_file.file)
    return df