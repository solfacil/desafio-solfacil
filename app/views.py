from django.shortcuts import render
from .models import Partner, PartnerAddress
from rest_framework.decorators import api_view
import csv
import requests

def app(request):
    return render(request, 'home.html')

def list_partners(request):
    partners = Partner.objects.all()
    return render(request,'partner_list.html', {'partners': partners})

@api_view(['GET', 'POST'])
def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        cnpj_error = []
        cnpj_success = []
        for i, row in enumerate(data):
            if i==0:
                pass
            else:
                cnpj = row[0]
                razao_social = row[1]
                nome_fantasia = row[2]
                telefone = row[3] 
                email = row[4] 
                cep = row[5]
                 
                if validate_cnpj(cnpj):
                  
                    partner, created = Partner.objects.get_or_create(cnpj=cnpj)
                    partner.razao_social = razao_social
                    partner.nome_fantasia = nome_fantasia 
                    partner.telefone = telefone
                    partner.email = email
                    partner.cep = cep
                    partner.save()
                    cnpj_success.append(cnpj)
                    
                    send_email(email)
                    generate_partner_address(cep, partner)
                else:
                    cnpj_error.append(cnpj)
        return render(request, 'success.html', {'cnpj_error':cnpj_error, 'cnpj_success': cnpj_success})
    return render(request, 'csv_upload.html')

def send_email(email):
    #implement email sending
    print(f"Welcome to my app {email}")
    return

def validate_cnpj(value):
    cnpj = ''.join(filter(str.isdigit, value))
    if len(cnpj) == 14:
        return cnpj
    else:
        return None

def generate_partner_address(cep, partner):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        address = response.json()
        partnerAddress, created = PartnerAddress.objects.get_or_create(partner=partner)
        partnerAddress.cep = cep
        partnerAddress.logradouro = address['logradouro']
        partnerAddress.complemento = address['complemento']
        partnerAddress.localidade = address['localidade']
        partnerAddress.uf = address['uf']
        partnerAddress.ibge = address['ibge']
        partnerAddress.gia = address['gia']
        partnerAddress.ddd = address['ddd']
        partnerAddress.siafi = address['siafi']
        partnerAddress.save()
        return 
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
def list_address_partners(request):
    partners = PartnerAddress.objects.all()
    return render(request,'partner_address_list.html', {'partners': partners})