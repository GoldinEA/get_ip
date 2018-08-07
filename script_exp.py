import csv
import sys
from urllib.request import urlopen
from io import StringIO
import os
import time

URL = 'https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv'
DATA_VALUE = 30000
DIR = '/Users/evgenij/PycharmProjects/file_creater'
TIME = 2


class GetData:

    def __init__(self, url, dr, data_value):
        self.__url = url
        self.__dr = dr
        self.__data_value = data_value
        csv.field_size_limit(sys.maxsize)

    def Get_Data(self):
        data = urlopen(self.__url).read().decode('cp1251')
        data_file = StringIO(data)
        data_clear = [x[0] for x in csv.reader(data_file, delimiter=';')]
        return {y.strip() for x in data_clear for y in x.split('|')}

    @property
    def gt_dt(self):
        m = 0
        data = tuple(self.Get_Data())[1:]
        ln = len(data)
        for ip_adress in (data[i:i + self.__data_value] for i in range(0, ln, self.__data_value)):
            os.chdir(self.__dr)
            with open('{}'.format(m), 'w') as f:
                [f.write(x + '\n') for x in ip_adress]
            m += 1
        del m

while True:
    m = GetData(URL, DIR, DATA_VALUE).gt_dt
    time.sleep(TIME)
