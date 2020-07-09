from datetime import datetime

def prepare_date():
    date = str(datetime.today())
    date = date.split(" ")[0]
    year, month, day = date.split("-")
    return f'{day}-{month}-{year}'