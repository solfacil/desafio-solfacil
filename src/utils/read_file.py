from csv import DictReader


async def read_csv(file) -> DictReader:
    # Read the contents of the file asynchronously
    content = await file.read()

    # Decode the bytes to a UTF-8 string
    decoded_content = content.decode("utf-8")

    # Define the column names for the CSV data
    header = ("CNPJ", "Razão Social", "Nome Fantasia",
              "Telefone", "Email", "CEP")

    # Parse the CSV data into a list of dicts using csv.DictReader
    rows = DictReader(decoded_content.splitlines(),
                      fieldnames=header, delimiter=",")

    # Return the list of parsed rows
    return rows
