import requests
import pandas as pd
import web_loader
import os

class Company:

    def __init__(self, name):
        self.name = name

    @property
    def company_data_frame(self):
        url = f'https://www.gpw.pl/archiwum-notowan?fetch=1&type=10&instrument={self.name}&date=&show_x=Pokaż+wyniki'
        r = requests.get(url)
        data_frame = pd.read_excel(r.content)
        return data_frame

    @property
    def ISIN(self):
        return self.company_data_frame.loc[1, 'ISIN']

    @property
    def sector(self):
        url = f'https://www.gpw.pl/spolka?isin={self.ISIN}#indicatorsTab'
        loader = web_loader.Loader(url)
        html = loader.get_html()
        a = str(html.find_all('a', {'class': 'nav-link', 'href': '#showNotoria'}))
        array = a.split("&amp;")
        for element in array:
            if 'sektor=' in element:
                return element.split('=')[1]
        return None

    def create_company_folder(self):
        if not os.path.exists(f'Companies/{self.sector}/{self.name}'):
            os.makedirs(f'Companies/{self.sector}/{self.name}')

    def save_data_frame_to_file(self):
        date = self.company_data_frame.iloc[-1]['Data']
        print(date)
        if not os.path.exists(f'Companies/{self.sector}/{self.name}/df_{date}.csv'):
            self.company_data_frame.to_csv(f'Companies/{self.sector}/{self.name}/df_{date}.csv')


comp_1 = Company("11BIT")
comp_1.create_company_folder()
comp_1.save_data_frame_to_file()