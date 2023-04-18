from typing import List

from django.db import transaction

from api.application.partner import PartnerDto, PartnerStorage

from .models import Partner


class PartnerRepository(PartnerStorage):
    def __partner_dto_to_model(self, partner_dto: PartnerDto) -> Partner:
        partner = Partner()
        partner.id = partner_dto.id
        partner.cnpj = partner_dto.cnpj
        partner.cpf = partner_dto.cpf
        partner.corporate_name = partner_dto.corporate_name
        partner.trading_name = partner_dto.trading_name
        partner.phone = partner_dto.phone
        partner.cep = partner_dto.cep
        partner.uf = partner_dto.uf
        partner.city = partner_dto.city
        partner.email = partner_dto.email
        return partner

    def __model_to_dto(self, partner: Partner):
        return PartnerDto(
            id=partner.id,
            cnpj=partner.cnpj,
            cpf=partner.cpf,
            corporate_name=partner.corporate_name,
            trading_name=partner.trading_name,
            phone=partner.phone,
            email=partner.email,
            cep=partner.cep,
            uf=partner.uf,
            city=partner.city,
        )

    @transaction.atomic
    def save_or_update_partner(self, partner_dto: PartnerDto) -> None:
        partner = Partner.objects.filter(
            **{
                "cpf"
                if partner_dto.cpf
                else "cnpj": partner_dto.cpf
                if partner_dto.cpf
                else partner_dto.cnpj
            }
        )
        if partner:
            partner_dto.id = partner.first().id
            partner.update(**partner_dto.__dict__)
        else:
            partner = self.__partner_dto_to_model(partner_dto)
            partner.save()

    def get_all_partners(self) -> List[PartnerDto]:
        partners = Partner.objects.all()
        partners_dto: List[PartnerDto] = []
        for partner in partners:
            partners_dto.append(self.__model_to_dto(partner))
        return partners_dto
