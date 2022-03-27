import pandas as pd
import datetime

class DataDelete():
    def delete_old_data(self, filter_direktorija):

        data = pd.read_csv(f'{filter_direktorija}/base.csv', delimiter=';', engine='python').set_index('TecReq#') 

        now = datetime.datetime.now()
        old_data = now - datetime.timedelta(days=30)

        data['Created+3mod'] = pd.to_datetime(data['Created+3mod'])
        formatas =data['Created+3mod']
        print(type(formatas))

        df = data[formatas > old_data]
        df.to_csv(f"{filter_direktorija}/base.csv", sep=';')

