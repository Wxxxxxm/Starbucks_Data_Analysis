#-*- coding:utf-8 -*-

from DataAnalysis import *
from Geohash import encode
from pandas import *
import time
from top import *


def find_largest(df1, lon, lat, r):
    if df1.shape[0] == 0:
        return r-1
    else:
        dis = []
        for index in range(df1.shape[0]):
            distance = haversine(df1['lat'][index], df1['lon'][index], lat, lon)
            dis.append(distance)
        df1.insert(0, 'distance', dis)

        arr = numpy.array(dis)
        arr = top_heap_sort(arr)
        return arr[0]


def r_cal(df, lon, lat, r):
    h_goal = encode(lat, lon, 4)
    df1 = df[df.h4 == h_goal[0:4]]
    df1 = df1.reset_index(drop=True)

    if(find_largest(df1, lon, lat, r) < r):
        df1 = df[df.h3 == h_goal[0:3]]
        df1 = df1.reset_index(drop=True)
        if(find_largest(df1, lon, lat, r) < r):
            df1 = df[df.h2 == h_goal[0:2]]
            df1 = df1.reset_index(drop=True)
            if(find_largest(df1, lon, lat, r) < r):
                df1 = df[df.h1 == h_goal[0]]
                df1 = df1.reset_index(drop=True)
                if(find_largest(df1, lon, lat, r) < r):
                    df1 = df.copy()
                    find_largest(df1, lon, lat, r)
                else:
                    df1 = df1
            else:
                df1 = df1
        else:
            df1=df1
    else:
        df1 = df1
    df_r = df1[df1.distance < r]
    return df_r


def r_analysis(df, lon, lat):
    list_cal_r = []
    for i in range(1, 500):
        r = 10*i

        start = time.time()
        dfr = r_cal(df, lon, lat, r)
        end = time.time()

        # if dfr.shape[0] == 0:
        #     print('No starbucks in R')
        # else:
        #     print(dfr)

        list_cal_r.append(end-start)
    r_analyze = DataFrame({
        'r': range(1, 500),
        'time': list_cal_r
    })
    return r_analyze

