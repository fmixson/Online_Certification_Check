import pandas as pd
import openpyxl

online_remote_spring_schedule = pd.read_csv('C:/Users/fmixson/Desktop/DE Programming sheets/Copy of DE Classes - Fall 2023 5.5.23.csv', encoding='Latin')


de_certified = pd.read_csv("C:/Users/fmixson/Desktop/DE Programming sheets/Dean's List (APPROVED DE Faculty spreadsheet 2023).csv", encoding='Latin')

for i in range(len(de_certified)):
    for j in range(len(online_remote_spring_schedule)):
        if de_certified.loc[i, 'LAST_NAME'] == online_remote_spring_schedule.loc[j, 'Instructor']:
            print(de_certified.loc[i, 'LAST_NAME'],online_remote_spring_schedule.loc[j, 'Instructor'])
            if de_certified.loc[i, 'DIV'] == online_remote_spring_schedule.loc[j, 'Div']:
                print(de_certified.loc[i, 'DIV'], online_remote_spring_schedule.loc[j, 'Div'])
                print(de_certified.loc[i, 'FULL CERT?'])
                print(i, j)
                # de_certified.loc[i, 'FULL CERT?'] = spring_schedule.loc[j, 'DE_CERT']
                online_remote_spring_schedule.loc[j, 'DE_CERT'] = de_certified.loc[i, 'FULL CERT?']
                print(de_certified.loc[i, 'FULL CERT?'])
online_remote_spring_schedule.to_excel('Online_and_Remote_DE_Certification.xlsx')

# hybrid_spring_schedule = pd.read_csv('C:/Users/fmixson/Desktop/DE Programming sheets/Spring 2023 - List of Hybrid Classes.csv', encoding='Latin')
#
# for i in range(len(de_certified)):
#     for j in range(len(hybrid_spring_schedule)):
#         if de_certified.loc[i, 'LAST_NAME'] == hybrid_spring_schedule.loc[j, 'Instructor']:
#             print(de_certified.loc[i, 'LAST_NAME'],hybrid_spring_schedule.loc[j, 'Instructor'])
#             if de_certified.loc[i, 'DIV'] == hybrid_spring_schedule.loc[j, 'Div']:
#                 print(de_certified.loc[i, 'DIV'], hybrid_spring_schedule.loc[j, 'Div'])
#                 print(de_certified.loc[i, 'FULL CERT?'])
#                 print(i, j)
#                 # de_certified.loc[i, 'FULL CERT?'] = spring_schedule.loc[j, 'DE_CERT']
#                 hybrid_spring_schedule.loc[j, 'DE_CERT'] = de_certified.loc[i, 'FULL CERT?']
#                 print(de_certified.loc[i, 'FULL CERT?'])
# hybrid_spring_schedule.to_excel('Hybrid_DE_Certification.xlsx')