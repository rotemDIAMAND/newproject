import consts
import pandas as pd
import pygame
import csv


START = False
STOP = False
dict = {
   consts.ONE_KEY: {},
    consts.TWO_KEY: {},
    consts.THREE_KEY: {},
    consts.FOUR_KEY: {},
    consts.FIVE_KEY: {},
    consts.SIX_KEY: {},
    consts.SEVEN_KEY: {},
    consts.EIGHT_KEY: {},
    consts.NINE_KEY: {}
}

def detect_key(key):
    if key[consts.ONE_KEY]:
        return 0
    elif key[consts.TWO_KEY]:
        return 1
    elif key[consts.THREE_KEY]:
        return 2
    elif key[consts.FOUR_KEY]:
        return 3
    elif key[consts.FIVE_KEY]:
        return 4
    elif key[consts.SIX_KEY]:
        return 5
    elif key[consts.SEVEN_KEY]:
        return 6
    elif key[consts.EIGHT_KEY]:
        return 7
    elif key[consts.NINE_KEY]:
        return 8
    else:
        return False

def creating_cvs_file(data):
    file_name = str(data["key"]) + ".csv"
    with open(file_name, 'w') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, data.keys())
        w.writeheader()
        w.writerow(data)

def put_data_in_chart(key, file):
    dict[key] = file

def opening_csv_file(key):
    data_continue = {
    }
    file_name = str(key)+".csv"
    with open(file_name, newline='') as pscfile:
        reader = csv.DictReader(pscfile)
        for row in reader:
            data_continue.update(row)
    return data_continue

def what_time_key_pressed(key, data, time):
    key1 = detect_key(key)
    if time <= 1.0:
        file = creating_cvs_file(data)
        put_data_in_chart(key1, file)
        return data
    else:
        data_continue = opening_csv_file(key1)
        return data_continue

def main_database(soldier_place, mines, grass, key_game, time):
    data = {
        "key": detect_key(key_game),
        "soldier_place": soldier_place,
        "mines": mines,
        "grass": grass
    }
    return what_time_key_pressed(key_game, data, time)