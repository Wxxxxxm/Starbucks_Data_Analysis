#-*- coding:utf-8 -*-

from DataAnalysis import *
from math import sin, asin, cos, radians, fabs, sqrt
from Geohash import encode
from pandas import *


EARTH_RADIUS = 6371


def hav(theta):
    s = sin(theta / 2)
    return s * s



def get_distance_hav(lat0, lon0, lat1, lon1):
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lon0 = radians(lon0)
    lon1= radians(lon1)

    dlon = fabs(lon0 - lon1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlon)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # translate shijinzhi into hudu
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # average radium of the earth , kilometer
    return c * r


def heap_adjust(arr, low, high):
    tmp = arr[low]
    i = low
    j = 2*i+1

    while j < high:
        if j < high-1 and arr[j] < arr[j+1]:
            j = j+1
        if tmp < arr[j]:
            arr[i] = arr[j]
            i = j
            j = 2*i+1
        else:
            break
    arr[i] = tmp


def top_heap_sort(arr):
    length = len(arr)
    first_exchange_elem = (length / 2) - 1
    for x in range(first_exchange_elem + 1):
        heap_adjust(arr, first_exchange_elem - x, length)
    return arr


def find_largest(df1, lon, lat, r):
    if df1.shape[0] == 0:
        return r-1
    else:
        dis = []
        for index in range(df1.shape[0]):
            distance = haversine(df1['lat'][index], df1['lon'][index], lat, lon)
            dis.append(distance)
        df1.insert(0, 'distance', dis)
        print(df1)
        # df1.set_index('distance', inplace=True, drop=True)
        arr = numpy.array(dis)
        # print(arr)
        arr = top_heap_sort(arr)
        # print(arr)
        # print(arr[0])
        return arr[0]


def r_cal(df, lon, lat, r):
    h_goal = encode(lat, lon, 4)
    # 筛选h4属性为h_goal[0:4]的行组成dataframe
    df1 = df[df.h4 == h_goal[0:4]]
    df1 = df1.reset_index(drop=True)
    if find_largest(df1, lon, lat, r) < r:
        df1 = df[df.h3 == h_goal[0:3]]
        df1 = df1.reset_index(drop=True)
        #pbar.setValue(1)
        if find_largest(df1, lon, lat, r) < r:
            df1 = df[df.h2 == h_goal[0:2]]
            df1 = df1.reset_index(drop=True)
            if find_largest(df1, lon, lat, r) < r:
                df1 = df[df.h1 == h_goal[0]]
                df1 = df1.reset_index(drop=True)
                if find_largest(df1, lon, lat, r) < r:
                    df1 = df.copy()
                    find_largest(df1, lon, lat, r)
    # dis = []
    # for index in range(df1.shape[0]):
    #    distance = get_distance_hav(df1['lat'][index], df1['lon'][index], lat, lon)
    #    dis.append(distance)
    # df1.insert(0, 'distance', dis)
    # print(df1)
    df_r = df1[df1.distance < r]
    return df_r


def r_analysis(df, lon, lat):
    list_cal_r = []
    for i in range(1, 500):
        r = 10*i
        list_time = []
        print(r)
        start = time.time()
        # print(df)
        dfr = r_cal(df, lon, lat, r)
        end = time.time()
        print(lon)
        print(lat)
        if dfr.shape[0] == 0:
            print('No starbucks in R')
        else:
            print(dfr)
        print('---------------------------------------------')
        list_cal_r.append(end-start)
    print list_cal_r
    r_analyze = DataFrame({
        'r': range(1, 500),
        'time': list_cal_r
    })
    return r_analyze

