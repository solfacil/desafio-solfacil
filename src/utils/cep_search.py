import requests


def define_parceiro_location(cep: str) -> dict:
    # Define the URL for the ViaCEP API based on the given CEP number
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # Send a GET request to the ViaCEP API and raise an exception if an HTTP error occurs
        response = requests.get(url)
        response.raise_for_status()

        # Decode the JSON response and return a dictionary object with city (cidade) and state (estado) information # noqa
        data = response.json()
        return {"cidade": data["localidade"], "estado": data["uf"]}

    except requests.exceptions.HTTPError:
        # Return None if there is an HTTP error during the request
        return None
