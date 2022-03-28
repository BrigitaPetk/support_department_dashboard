import pandas as pd
import datetime

class DataDelete():
    def delete_old_data(self, filter_direktorija,filter_direktorija_GB):

        def delete(location, name):
            data = pd.read_csv(f'{location}/{name}.csv', delimiter=';', engine='python').set_index('TecReq#') 

            now = datetime.datetime.now()
            old_data = now - datetime.timedelta(days=30)

            data['Created+3mod'] = pd.to_datetime(data['Created+3mod'])
            formatas =data['Created+3mod']
            df = data[formatas > old_data]
            df.to_csv(f"{location}/{name}.csv", sep=';')

        delete(filter_direktorija, 'base')
        delete(filter_direktorija_GB, 'base_GB')
