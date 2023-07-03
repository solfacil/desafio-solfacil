from fastapi import UploadFile
from pydantic import BaseModel, validator

from src.domain.enums.file.extensions import FileExtension
from src.domain.exceptions.domain.exception import InvalidFileTypeError


class CsvValidator(BaseModel):
    file: UploadFile

    @validator('file')
    def validate_file_extension(cls, file: UploadFile):
        file_name_splited = file.filename.lower().split('.')
        extension = file_name_splited[-1]
        if not extension == FileExtension.CSV:
            raise InvalidFileTypeError()
