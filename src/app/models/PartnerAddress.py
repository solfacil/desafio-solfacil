import os
import time
from typing import Optional

import requests
from cachetools.func import ttl_cache
from loguru import logger
from pydantic import BaseModel, root_validator


@ttl_cache(ttl=60 * 30)  # cache for 30 minutes
def query_viacep(cep):
    max_retries = 5
    retry = 1
    while retry < max_retries:
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if not r.ok:
            time.sleep(3)
            retry += 1
            continue
        break
    return r


class PartnerAddress(BaseModel):
    cep: Optional[str]
    logradouro: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    localidade: Optional[str]
    uf: Optional[str]
    ibge: Optional[str]
    gia: Optional[str]
    ddd: Optional[str]
    siafi: Optional[str]

    class Config:
        orm_mode = True

    @root_validator
    def fill_from_viacep(cls, values: dict):
        if not (cep := values.get('cep')):
            raise KeyError("Please provide the CEP information")
        cep = str(cep)
        cep = cep.replace('-', '')

        if bool(int(os.environ.get('GET_ADDRESS_FROM_VIACEP', '0'))):
            # I was getting too many bad requests from viacep while testing
            r = query_viacep(cep)
            err_msg = f"Couldn't get CEP {cep} info: Reason = '{r.reason}'. Status = '{r.status_code}'. url = '{r.url}'"
            # cep_lookup_error = Exception(err_msg)
            if not r.ok:

                # raise an error and prevents system add this partner?
                # could also insert all values as empty ""
                # raise cep_lookup_error
                logger.debug(err_msg)

            values = r.json()
            if values.get('erro') is True:
                # raise cep_lookup_error
                ...
        else:
            logger.debug("Viacep query is disable, set GET_ADDRESS_FROM_VIACEP to '1' to enable it")
            values = {'cep': cep}
        logger.debug(f"CEP VALUES -> {values}")
        return values
