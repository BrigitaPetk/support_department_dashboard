import pandas as pd
import datetime

class FilterFinalData():
    def final_data(self, filter_direktorija, final_direktorija):

        df = pd.read_csv(f'{filter_direktorija}/base.csv', delimiter=';', engine='python')

        week_number = list(df['Week'].unique()) 

        years = []

        total = [] 
        total_LT = []
        total_LT_CTS = []
        total_AT =[]
        total_CH =[]
        total_DE =[]
        total_IN =[]

        total_LT_DE = []
        total_LT_CH = []
        total_LT_AT = []

        total_LT_STRAT = []
        total_LT_IMP = []
        totoal_LT_SMART = []
        total_LT_EMPTY =[]

        STRAT_solution =[]
        IMP_solution =[]
        SMART_solution =[]
        TUST_solution =[]

        STRAT_intake =[]
        IMP_intake =[]
        SMART_intake =[]
        TUST_intake =[]

        Intake_average = []
            
        letter_number = []

        know1 = []
        know2 = []
        know3 = []
        know4 = []
        know5 = []
        know6 = []
        know0 = []


        for week in week_number:

            df1 = df.loc[df['Week'] == week]
            
            total_number = df1['TecReq#'].count()  
            total.append(total_number)
            
            df_lt = df1.loc[df1['Owner Country Code'] == 'LT']
            rows_lt, columns = df_lt.shape
            total_LT.append(rows_lt)

            year = df1['Year'].unique()
            years.append(year[0])
            
            #CTS counter:
            df_LT_CTS =df1.loc[df1['Queue'].str.contains("CTS")]
            rows_lt_cts, columns = df_LT_CTS.shape
            total_LT_CTS.append(rows_lt_cts)

            # AT, CH DE IN LT
            df_AT = df1.loc[df1['Owner Country Code'] == 'AT']
            rows_AT, columns = df_AT.shape
            total_AT.append(rows_AT)
            
            df_CH = df1.loc[df1['Owner Country Code'] == 'CH']
            rows_CH, columns = df_CH.shape
            total_CH.append(rows_CH)
            
            df_DE = df1.loc[df1['Owner Country Code'] == 'DE']
            rows_DE, columns = df_DE.shape
            total_DE.append(rows_DE)
            
            df_IN = df1.loc[df1['Owner Country Code'] == 'IN']
            rows_IN, columns = df_IN.shape
            total_IN.append(rows_IN)
            
            
            #LT_DE, LT_CH, LT_AT
            DE_total = df_lt.loc[df_lt['Queue'].str.contains("TH_DE")]
            rows, columns = DE_total.shape
            total_LT_DE.append(rows)

            CH_total = df_lt.loc[df_lt['Queue'].str.contains("TH_CH")]
            rows, columns = CH_total.shape
            total_LT_CH.append(rows)
            
            AT_total = df_lt.loc[df_lt['Queue'].str.contains("TH_AT")]
            rows, columns = AT_total.shape
            total_LT_AT.append(rows)
            
            #letter counter
            letter = df_lt['Number of Articles'].sum()
            final_letter_number = letter -(rows_lt *2)
            letter_number.append(final_letter_number)

            # SOLUTION time  
            S_unanswered = 0
            S_STRAT_in_time = 0
            S_STRAT_late =0 
            S_IMP_in_time = 0
            S_IMP_late =0
            S_SMART_in_time = 0
            S_SMART_late =0
            S_EMPTY_in_time = 0
            S_EMPTY_late =0
            
            for index, row in df_lt.iterrows():  
                date = str(row['First Response - Created'])
                client = str(row['Case CV'])
                delta = pd.to_timedelta(date)
                
                if date == 'nan':
                    S_unanswered = S_unanswered +1
                elif client == 'nan':
                    if delta < datetime.timedelta(hours=6):
                        S_EMPTY_in_time = S_EMPTY_in_time +1
                    else:
                        S_EMPTY_late = S_EMPTY_late +1
                elif client == 'STRAT':
                    if delta < datetime.timedelta(hours=4):
                        S_STRAT_in_time = S_STRAT_in_time +1
                    else:
                        S_STRAT_late = S_STRAT_late +1
                elif client == 'IMP':
                    if delta < datetime.timedelta(hours=6):
                        S_IMP_in_time =S_IMP_in_time +1
                    else:
                        S_IMP_late = S_IMP_late +1
                elif client == 'SMART':
                    if delta < datetime.timedelta(hours=8):
                        S_SMART_in_time =S_SMART_in_time +1
                    else:
                        S_SMART_late = S_SMART_late +1
            
            try:
                STRAT_sol = round((S_STRAT_in_time/(S_STRAT_in_time+S_STRAT_late))*100)
                STRAT_solution.append(STRAT_sol)
            except ZeroDivisionError:
                STRAT_solution.append(0)

            
            IMP_sol = round((S_IMP_in_time/(S_IMP_in_time+S_IMP_late))*100)
            IMP_solution.append(IMP_sol)
            
            SMART_sol = round((S_SMART_in_time/(S_SMART_in_time+S_SMART_late))*100)
            SMART_solution.append(SMART_sol)
            
            try:
                TUST_sol = round((S_EMPTY_in_time/(S_EMPTY_in_time+S_EMPTY_late))*100)
                TUST_solution.append(TUST_sol)
            except ZeroDivisionError:
                TUST_solution.append(0)
            
            
            
            # INTAKE TIME 
            I_unanswered = 0
            I_STRAT_in_time = 0
            I_STRAT_late =0 
            I_IMP_in_time = 0
            I_IMP_late =0
            I_SMART_in_time = 0
            I_SMART_late =0
            I_EMPTY_in_time = 0
            I_EMPTY_late =0
            
            for index, row in df1.iterrows():  
                date = str(row['First Lock - Created'])
                client = str(row['Case CV'])
                delta = pd.to_timedelta(date)
                
                if date == 'nan':
                    I_unanswered = I_unanswered +1
                elif client == 'nan':
                    if delta < datetime.timedelta(hours=6):
                        I_EMPTY_in_time = I_EMPTY_in_time +1
                    else:
                        I_EMPTY_late = I_EMPTY_late +1
                elif client == 'STRAT':
                    if delta < datetime.timedelta(hours=4):
                        I_STRAT_in_time = I_STRAT_in_time +1
                    else:
                        I_STRAT_late = I_STRAT_late +1
                elif client == 'IMP':
                    if delta < datetime.timedelta(hours=6):
                        I_IMP_in_time =I_IMP_in_time +1
                    else:
                        I_IMP_late = I_IMP_late +1
                elif client == 'SMART':
                    if delta < datetime.timedelta(hours=8):
                        I_SMART_in_time =I_SMART_in_time +1
                    else:
                        I_SMART_late = I_SMART_late +1
            
            
            I_STRAT = round((I_STRAT_in_time/(I_STRAT_in_time+I_STRAT_late))*100)
            STRAT_intake.append(I_STRAT)
            
            I_IMP = round((I_IMP_in_time/(I_IMP_in_time+I_IMP_late))*100)
            IMP_intake.append(I_IMP)
            
            I_SMART = round((I_SMART_in_time/(I_SMART_in_time+I_SMART_late))*100)
            SMART_intake.append(I_SMART)
            
            try:
                I_TUST = round((I_EMPTY_in_time/(I_EMPTY_in_time+I_EMPTY_late))*100)
                TUST_intake.append(I_TUST)
            except ZeroDivisionError:
                TUST_intake.append(0)

            Intake_av = (I_STRAT + I_IMP+ I_SMART +I_TUST) /4
            Intake_average.append(round(Intake_av))
            
            
            #Total STRAT, IMP, SMART, EMPTY
            strat = df_lt.loc[df_lt['Case CV'] == "STRAT"]
            rows_start, columns = strat.shape
            total_LT_STRAT.append(rows_start)
            
            imp = df_lt.loc[df_lt['Case CV'] == "IMP"]
            rows_imp, columns = imp.shape
            total_LT_IMP.append(rows_imp)
            
            smart = df_lt.loc[df_lt['Case CV'] == "SMART"]
            rows_smart, columns = smart.shape
            totoal_LT_SMART.append(rows_smart)
            
            tuscios = rows_lt -rows_start -rows_imp -rows_smart
            total_LT_EMPTY.append(tuscios)
            
            
            #knolage level pasiskirstmas
            level1 = df_lt.loc[df_lt['Needed knowledge level'] == "1 - Catalogue knowledge"]
            rows1, columns = level1.shape
            know1.append(rows1)
            
            level2 = df_lt.loc[df_lt['Needed knowledge level'] == "2 - Operation manual knowledge"]
            rows2, columns = level2.shape
            know2.append(rows2)
            
            level3 = df_lt.loc[df_lt['Needed knowledge level'] == "3 - Product Repair"]
            rows3, columns = level3.shape
            know3.append(rows3)
            
            level4 = df_lt.loc[df_lt['Needed knowledge level'] =="4 - Interaction / systems with other Festo components or special software necessary"]
            rows4, columns = level4.shape
            know4.append(rows4)

            level5 = df_lt.loc[df_lt['Needed knowledge level'] =="5 - Interaction/systems with 3rd party products"]
            rows5, columns = level5.shape
            know5.append(rows5)
            
            level6 = df_lt.loc[df_lt['Needed knowledge level'] =="6 - R&D knowledge (Special knowledge above catalogue and trainings)"]
            rows6, columns = level6.shape
            know6.append(rows6)
            
            empty_level = rows_lt - rows1- rows2 -rows3 - rows4 - rows5 - rows6
            know0.append(empty_level)
            
            
        # print(f'metai:{years}')
        # print('---------------')

        # print(f'bendras uzklausu skaicius 2{total}')
        # print(f'bendras lietuva :{total_LT}')
        # print(f'DE apdorota lietuvoje{total_LT_DE}')  
        # print(f'CH apdorota lietuvoje{total_LT_CH}')
        # print(f'AT apdorota lietuvoje{total_LT_AT}')
        # print('---------------')
        # print(f'STRAT kiekis :{total_LT_STRAT}')
        # print(f'IMP kiekis :{total_LT_IMP}') 
        # print(f'SMART kiekis :{totoal_LT_SMART}') 
        # print(f'Tuscios kiekis :{total_LT_EMPTY}') 
        # print('---------------')
        # print(f'parasyta laisku{letter_number}')
        # print('---------------')

        # print('---------------')
        # print(f'knowlage level nenustatytas:{know0}')
        # print(f'knowlage level 1: {know1}')
        # print(f'knowlage level 2: {know2}')
        # print(f'knowlage level 3: {know3}')
        # print(f'knowlage level 4: {know4}')
        # print(f'knowlage level 5: {know5}')
        # print(f'knowlage level 6: {know6}')
            
        # print('---------------')
        # print(f'STRAT solution: {STRAT_solution}')
        # print(f'IMP solution: {IMP_solution}')      
        # print(f'SMART solution: {SMART_solution}')
        # print(f'TUST solution: {TUST_solution}')   

        # print('---------------')
        # print(f'STRAT intake: {STRAT_intake}')
        # print(f'IMP intake: {IMP_intake}')      
        # print(f'SMART intake: {SMART_intake}')
        # print(f'TUST intake: {TUST_intake}')  
        # print(f'TUST intake: {Intake_average}')  

        # print('---------------')
        # print(f'total_AT: {total_AT}') 
        # print(f'total_CH: {total_CH}')
        # print(f'total_DE: {total_DE}')
        # print(f'total_IN: {total_IN}')


        base_by_week = pd.read_csv(f'{final_direktorija}/base_by_week.csv', sep=';')
        base_by_week.index = pd.MultiIndex.from_arrays(base_by_week[['Year', 'Week']].values.T, names=['idx1', 'idx2'])

        data = {'Year':years, 'Week': week_number,'request number': total,'request number in LT': total_LT, 
                'request number in AT':total_AT , 'request number in CH':total_CH ,
                'request number in DE':total_DE , 'request number in IN':total_IN ,
                'IMP request number': total_LT_IMP, 'SMART request number':totoal_LT_SMART, 'STRAT request number': total_LT_STRAT,
                'EMPTY request number': total_LT_EMPTY, 'LT request number in DE':total_LT_DE,
                'LT request number in CH':total_LT_CH, 'LT request number in AT':total_LT_AT, 'LT CTS': total_LT_CTS,
                'knowledge level empty': know0,  'knowledge level 1': know1, 
                'knowledge level 2': know2, 'knowledge level 3': know3, 'knowledge level 4': know4,
                'STRAT solution time': STRAT_solution, 'IMP solution time': IMP_solution, 'SMART solution time': SMART_solution,
                'EMPTY solution time': TUST_solution, 'Intake': Intake_average }

        week_df = pd.DataFrame(data)
        week_df.index = pd.MultiIndex.from_arrays(week_df[['Year', 'Week']].values.T, names=['idx1', 'idx2'])

        final_data_by_week = base_by_week.combine_first(week_df)

        final_data_by_week.to_csv(f'{final_direktorija}/base_by_week.csv', sep=';', index=False)

        print("data analyze done")