import os
from obspy import read


def read_data(datalist):
    path = os.path.join(os.path.dirname(__file__), '..', 'data')
    data = {}

    for channel, file in datalist:
        st = read(os.path.join(path, file))

        data[channel] = {'st': st}

    return data
