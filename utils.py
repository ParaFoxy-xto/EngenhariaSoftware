import datetime

def formata_data():
    data = datetime.datetime.now()
    return data.strftime('%d/%m/%Y')
