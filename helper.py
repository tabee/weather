import sys

import time

import datetime


def writeData(filename, data, city):
    with open(filename, "a") as text_file:
        tmp = time_stamp(city, data)
        text_file.writelines(tmp)


def save_in_file(filename, data):
    with open(filename, "w") as text_file:
        text_file.writelines(data)


def time_stamp(city, data):
    '''
    2016-02-26 20:07:10, Bern, rain

    :param city:
    :param data:
    :return:
    '''
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return str(st) + ', ' + city + ', ' + data + '\n'
