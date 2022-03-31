import pandas as pd
import datetime
from pathlib import Path
import numpy as np

def plus3h(data):
    columns = ['Created','First Lock', 'FirstResponse', 'Close Time']
    columns_to_3 = {column: f"{column}+3" for column in columns}
    for col in columns:
        for index, row in data.iterrows():
            row = str(row[col])
            if row == str(np.nan):
                data.loc[index, columns_to_3[col]] = 'NaN'
            else:
                time = datetime.datetime.fromisoformat(row) 
                plus = time + datetime.timedelta(hours=3)
                data.loc[index, columns_to_3[col]] = plus
    return columns_to_3.values(), data
        

def weekend_filtration(day):
    weekday = day.weekday()
    if weekday == 5:
        modified_date  = day.replace(hour= 8, minute= 0, second=0)
        return modified_date + datetime.timedelta(days=2)
    elif weekday == 6:
        modified_date  = day.replace(hour= 8, minute= 0, second=0)
        return modified_date + datetime.timedelta(days=1)
    else:
        return day


def working_hours_filtration(day):
    start_of_working_hours = datetime.datetime(1900, 1, 1, 8, 0, 0)
    end_of_working_hours = datetime.datetime(1900, 1, 1, 17, 0, 0)
    if day.time() < start_of_working_hours.time():
        modifies_date2  = day.replace(hour= 8, minute= 0, second=0)
        return modifies_date2
    elif day.time() > end_of_working_hours.time():
        modifies_date2  = day.replace(hour= 8, minute= 0, second=0)
        modifies_date2 = modifies_date2 + datetime.timedelta(days=1)
        return modifies_date2
    else:
        return day


def holiday_filtration(day):
    naujieji = datetime.datetime(2022, 1, 1)
    atkurimas = datetime.datetime(day.year, 2, 16)
    nepriklausomybes = datetime.datetime(day.year, 3, 11)
    velykos = datetime.datetime(day.year, 4, 17)
    velykos2 = datetime.datetime(day.year, 4, 18)
    darbininku = datetime.datetime(day.year, 5, 1)
    jonines = datetime.datetime(day.year, 6, 24)
    mindaugines = datetime.datetime(day.year, 7, 6)
    zolines = datetime.datetime(day.year, 8, 15)
    velines = datetime.datetime(day.year, 11, 1)
    velines2 = datetime.datetime(day.year, 11, 2)
    kucios = datetime.datetime(day.year, 12, 24)
    kaledos = datetime.datetime(day.year, 12, 25)
    kaledos2 = datetime.datetime(day.year, 12, 26)

    holidays_list = [naujieji, atkurimas, nepriklausomybes, velykos, velykos2, darbininku, jonines, 
            mindaugines, zolines, velines, velines2, kucios, kaledos, kaledos2]

    for holiday in holidays_list:
        while day.date() == holiday.date():
            day = day + datetime.timedelta(days=1)
            day  = day.replace(hour= 8, minute= 0, second=0)   
    return day


def final_time_modification(columns_list, data):
    columns_mod = {column: f"{column}mod" for column in columns_list}
    for column in columns_list:
        for index, row in data.iterrows():
            r = str(row[column])
            if r == "NaN" or r == "NaT":
                data.loc[index, columns_mod[column]] = r
            else:
                formated_date = datetime.datetime.fromisoformat(r)

                not_holiday = holiday_filtration(formated_date)
                not_weekend = weekend_filtration(not_holiday)
                working_hours = working_hours_filtration(not_weekend)
                data.loc[index, columns_mod[column]] = working_hours
    return columns_mod.values(), data

    # Solution Time % created - first response
    # INtake Time % created - first lock
def delta_counter(index, final_data, first, name, created, close):
    if (first == 'NaN' or first == 'NaT') and (close == 'NaN' or close == 'NaT'):
        final_data.loc[index, name] = first
    elif (first == 'NaN' or first == 'NaT') and (close != 'NaN' or close != 'NaT'):
        creat = datetime.datetime.fromisoformat(created)
        clo = datetime.datetime.fromisoformat(close) 
        if creat.date() == clo.date():
            rezult = clo - creat
            final_data.loc[index, name] = rezult
        else:
            sum = datetime.timedelta()
            creat2 = creat      
            end_of_working_hours = datetime.datetime(year=creat2.year, month=creat2.month, day = creat2.day, hour= 17, minute = 0, second = 0)
            delta_creat2 = end_of_working_hours - creat2
            sum = sum + delta_creat2

            while creat2.date() < clo.date() and creat2.date() + datetime.timedelta(days=1) < clo.date():
                creat2 = creat2 + datetime.timedelta(days=1)
                not_holiday = holiday_filtration(creat2)
                not_weekend = weekend_filtration(not_holiday)
                creat2 = not_weekend
                if  creat2.date() + datetime.timedelta(days=1) > clo.date():
                    break        
                sum = sum + datetime.timedelta(hours=8)

            start_of_working_hours = datetime.datetime(year=clo.year, month=clo.month, day = clo.day, hour= 8, minute = 0, second = 0) 
            delta_closed = clo - start_of_working_hours
            sum = sum + delta_closed
            final_data.loc[index, name] = sum
    else:
        creat = datetime.datetime.fromisoformat(created)
        first = datetime.datetime.fromisoformat(first)

        if creat.date() == first.date():
            rezult = first - creat
            final_data.loc[index, name] = rezult
        else:
            sum = datetime.timedelta()
            creat2 = creat     
            end_of_working_hours = datetime.datetime(year=creat2.year, month=creat2.month, day = creat2.day, hour= 17, minute = 0, second = 0)
            delta_creat2 = end_of_working_hours - creat2
            sum = sum + delta_creat2

            while creat2.date() < first.date() and creat2.date() + datetime.timedelta(days=1) < first.date():
                creat2 = creat2 + datetime.timedelta(days=1)
                not_holiday = holiday_filtration(creat2)
                not_weekend = weekend_filtration(not_holiday)
                creat2 = not_weekend
                if  creat2.date() + datetime.timedelta(days=1) > first.date():
                    break        
                sum = sum + datetime.timedelta(hours=8)

            start_of_working_hours = datetime.datetime(year=first.year, month=first.month, day = first.day, hour= 8, minute = 0, second = 0) 
            delta_closed = first - start_of_working_hours
            sum = sum + delta_closed
            final_data.loc[index, name] = sum

    return final_data
            

def sol_int_counter(final_data):
    for index, row in final_data.iterrows():
        created = str(row['Created+3mod'])
        close = str(row['Close Time+3mod'])
        first_restonse = str(row['FirstResponse+3mod'])
        first_lock = str(row['First Lock+3mod'])
        delta_counter(index, final_data, first_restonse,'First Response - Created', created, close)
        delta_counter(index, final_data, first_lock, 'First Lock - Created', created, close)
    
    return final_data

def date(data3):
    for index, row in data3.iterrows():
        r = str(row['Created'])
        x = datetime.datetime.fromisoformat(r)
        date_numbers = x.isocalendar()
        month = x.month
        data3.loc[index,'Month'] = month
        data3.loc[index,'Year'] = int(date_numbers[0])
        data3.loc[index,'Week'] = int(date_numbers[1])
    return data3


class CsvFiltration():
    def first_filtration_GB(self, extract_direktorija, filter_direktorija_GB):

        base = pd.read_csv(f'{filter_direktorija_GB}/base_GB.csv', delimiter=';', engine='python').set_index('TecReq#')

        file_location = extract_direktorija
        files = list(file_location.glob("*.csv*"))
        for x in files:
            data = pd.read_csv(x, delimiter=';', engine='python')
            df1 = data[['TecReq#', 'Created', 'First Lock', 'FirstResponse', 'Close Time', 'Queue', 'Owner Country Code', 'State', 'Number of Articles', 'Needed knowledge level', 'Case CV']]
            df2 = df1.loc[df1['State'] != "merged"]
            final_data = df2.loc[df2['Queue'].str.contains("TH_GB|TH_IE")]

        
            colums_list, data1 = plus3h(final_data)
            mod_list, data2 = final_time_modification(colums_list, data1)
            data3 = sol_int_counter(data2)
            final_data = date(data3)

            new_data = final_data[['TecReq#', 'Year','Month', 'Week', 'Created+3mod', 'First Lock+3mod', 'FirstResponse+3mod', 'Close Time+3mod', 
                                        'First Response - Created', 'First Lock - Created', 'Queue', 'Owner Country Code', 'State', 'Number of Articles', 
                                        'Needed knowledge level', 'Case CV']]
        
            base = base.combine_first(new_data.set_index('TecReq#'))

        base.to_csv(f"{filter_direktorija_GB}/base_GB.csv", sep=';')

        print("base was updated")


    def first_filtration(self, extract_direktorija, filter_direktorija):

        base = pd.read_csv(f'{filter_direktorija}/base.csv', delimiter=';', engine='python').set_index('TecReq#')

        file_location = extract_direktorija
        files = list(file_location.glob("*.csv*"))
        for x in files:
            data = pd.read_csv(x, delimiter=';', engine='python')
            df1 = data[['TecReq#', 'Created', 'First Lock', 'FirstResponse', 'Close Time', 'Queue', 'Owner Country Code', 'State', 'Number of Articles', 'Needed knowledge level', 'Case CV']]
            df2 = df1.loc[df1['State'] != "merged"]
            final_data = df2.loc[df2['Queue'].str.contains("TH_DE|TH_AT|TH_CH|TH_IT")]

        
            colums_list, data1 = plus3h(final_data)
            mod_list, data2 = final_time_modification(colums_list, data1)
            data3 = sol_int_counter(data2)
            final_data = date(data3)

            new_data = final_data[['TecReq#', 'Year','Month', 'Week', 'Created+3mod', 'First Lock+3mod', 'FirstResponse+3mod', 'Close Time+3mod', 
                                        'First Response - Created', 'First Lock - Created', 'Queue', 'Owner Country Code', 'State', 'Number of Articles', 
                                        'Needed knowledge level', 'Case CV']]
        
            base = base.combine_first(new_data.set_index('TecReq#'))

        base.to_csv(f"{filter_direktorija}/base.csv", sep=';')

        print("base was updated")
        # len(set(baze.index.values)) == len(baze.index.values)
        # len(set(baze.index.values))
        # len(baze.index.values)