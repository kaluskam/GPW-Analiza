import web_loader
import general

today = general.prepare_date()
date = '03-07-2020'
fetch = 0
URL = f'https://www.gpw.pl/archiwum-notowan?fetch={fetch}&type=10&instrument=&date=03-07-2020&show_x=Pokaż+wyniki'

notowania = web_loader.Loader(URL)

def get_companies_names():
    notowania.get_html()
    all_options = notowania.get_content_within_tags('select', id='selectInstrument')
    names = []
    for company in all_options.find_all('option'):
        if company['value'] != '':
            names.append(company['value'].replace(' ', '+'))
    return names


def get_company_ISIN():
    pass



