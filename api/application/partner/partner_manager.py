from typing import List

from api.domain.partner.exceptions import MissingParamError
from api.presenters.helpers import bad_request, created, ok, server_error

from .address_api import AddressApi
from .partner_dto import PartnerDto
from .partner_storage import PartnerStorage


class PartnerManager:
    storage: PartnerStorage
    address_api: AddressApi

    def __init__(self, storage: PartnerStorage, address_api: AddressApi) -> None:
        self.storage = storage
        self.address_api = address_api

    def create_or_update_partners(self, partners_dto: List[PartnerDto]):
        try:
            for partner_dto in partners_dto:
                partner_aggregate = partner_dto.to_domain()
                partner_aggregate.create_partner()
                address = self.address_api.handle(partner_aggregate.cep)
                partner_aggregate.uf = address["uf"]
                partner_aggregate.city = address["city"]
                self.storage.save_or_update_partner(
                    partner_dto.to_dto(partner_aggregate)
                )
            return created()
        except MissingParamError as ex:
            return bad_request(ex)
        except Exception as e:
            print(e)
            return server_error()

    def get_all_partners(self):
        partners = self.storage.get_all_partners()
        return ok(data=partners)
