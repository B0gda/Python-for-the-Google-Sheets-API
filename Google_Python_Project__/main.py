import sys
import time
from os import system
from Google import Create_Service
from Helper import printHello
import pandas as pd
import os
import pyautogui

CLIENT_SECRET_FILE = 'credentials.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
spreadsheet_id = "paste your sheet's ID"
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()



def case1():
    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        majorDimension='ROWS',
        range='ListOne'
    ).execute()
    #print(response['values'])
    columns = response['values'][0]
    data = response['values'][1:]
    df = pd.DataFrame(data, columns=columns)
    df2 = df.set_index('Счетчик')
    print(df2)
def case2():
    name = input("Введите название продукта: ")
    categoty = input("Введите категорию товара: ")
    weight = input("Введите вес товара: ")
    estimation = input("Введите оценку качества: ")
    price = input("Введите цену товара: ")
    range1 = 'A'
    lastRow = 1
    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='ListOne!A1:A'
    ).execute()
    lastRow += len(response['values'])  # lastRow выше на 1 значение
    range3 = range1 + str(lastRow)
    worksheet_name = 'ListOne!'
    cell_range_insert = range3
    values = (
        (lastRow - 1, name, categoty, weight, estimation, price),
    )
    value_range_body = {
        'majorDimension': 'ROWS',  #COLUMNS
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        valueInputOption='USER_ENTERED',
        range=worksheet_name + cell_range_insert,
        body=value_range_body
    ).execute()

def case3():
    case1()
    row_number = int(input("Введите номер удаляемой записи: "))
    row_number_next = row_number - 1
    lastRow = 1
    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='ListOne!A1:A'
    ).execute()
    lastRow += len(response['values'])  # lastRow выше на 1 значение
    request_body_delete = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'dimension': 'ROWS',
                        'startIndex': row_number_next + 1,
                        'endIndex': row_number + 1  ###
                    }
                }
            }
            ]
    }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body=request_body_delete
    ).execute()
    request_body3 = {
        'requests': [
            {
                'autoFill': {
                    'useAlternateSeries': False,
                    'sourceAndDestination': {
                        'source': {

                            'startRowIndex': 2,
                            'endRowIndex': 4,
                            'startColumnIndex': 0,
                            'endColumnIndex': 1
                        },
                        'dimension': 'ROWS',
                        'fillLength': lastRow - 6
                    }
                }
            }
        ]
    }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body=request_body3
    ).execute()

def case4():
    case1()
    row_number_start = int(input("Введите номер копируемой строки: "))
    lastRow = 1
    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='ListOne!A1:A'
    ).execute()
    lastRow += len(response['values'])  # lastRow выше на 1 значение
    request_body2 = {
        'requests': [
            {
                'copyPaste': {
                    'source': {
                        'startRowIndex': row_number_start,
                        'endRowIndex': row_number_start + 1,  ##
                        'startColumnIndex': 1,
                        'endColumnIndex': 6
                    },

                    'destination': {
                        'startRowIndex': lastRow - 1,
                        'endRowIndex': lastRow,  ##
                        'startColumnIndex': 1,
                        'endColumnIndex': 6
                    },
                    'pasteType': 'PASTE_FORMULA'
                }
            }
        ]
    }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body=request_body2
    ).execute()
    request_body3 = {
        'requests': [
            {
                'autoFill': {
                    'useAlternateSeries': False,
                    'sourceAndDestination': {
                        'source':{

                                          'startRowIndex': 2,
                                                'endRowIndex': 4,
                                                'startColumnIndex': 0,
                                                'endColumnIndex': 1
                        },
                        'dimension': 'ROWS',
                        'fillLength': lastRow - 4
                    }
                }
            }
        ]
    }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body=request_body3
    ).execute()



def default():
    print('Произведен выход...')

def case0():
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range='ListOne'
    ).execute()

def switch(menu):
    dict={
        1: case1,
        2: case2,
        3: case3,
        4: case4,
        0: case0
    }
    return dict.get(menu, default)()



files = ['data/ascii10.txt']
frames = []

clear = lambda: system('clear')

for name in files:
    with open(name, 'r', encoding='utf8') as f:
        frames.append(f.readlines())
for i in range(1):
    for frame in frames:
        print(''.join(frame))
        time.sleep(0.5)
        clear = lambda: system('clear')
menu = 77

while menu != 121:

    printHello()
    menu = int(input("Введите номер действия: "))
    switch(menu)


