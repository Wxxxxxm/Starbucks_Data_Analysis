from Geohash import encode
from pandas import DataFrame
from top import *
import random
import time


def k_cal(df, lon, lat, k):
    dis = []
    for index in range(df.shape[0]):
        distance = get_distance_hav(df['lat'][index], df['lon'][index], lat, lon)
        dis.append(distance)
    df.insert(0, 'distance', dis)
    df_k = df.sort_values(by=['distance'], ascending=True).head(k)
    df_k = df_k.reset_index(drop=True)
    return df_k


def topk(df, lon, lat, k):
    h_goal = encode(lat, lon, 4)
    df1 = df
    if df1[df1.h1 == h_goal[00000]].shape[0] > k:
        df1 = df1[df1.h1 == h_goal[0]]

        if df1[df1.h2 == h_goal[0:2]].shape[0] > k:
            df1 = df1[df1.h2 == h_goal[0:2]]
            if df1[df1.h3 == h_goal[0:3]].shape[0] > k:
                df1 = df1[df1.h3 == h_goal[0:3]]
                if df1[df1.h4 == h_goal[0:4]].shape[0] > k:
                    df1 = df1[df1.h4 == h_goal[0:4]]
    df1 = df1.reset_index(drop=True)

    df_res = k_cal(df1, lon, lat, k)
    return df_res


def topk_k_analysis(df,lon,lat):
    list_time = []
    for i in range(1, 50):
        k = 100*i

        start = time.time()
        df_k = topk(df, lon, lat, k)
        end = time.time()

        df = df.reset_index(drop=True)
        list_time.append(end-start)
    k_analysis = DataFrame({
        'k': range(1, 50),
        'time': list_time
    })
    k_analysis.transpose()

    return k_analysis


def topk_analysis(df):
    list_cal_k = []
    for i in range(1, 50):
        k = 100*i
        list_time = []

        for m in range(2):
            lon = random.uniform(-180, 180)
            lat = random.uniform(-90, 90)
            start = time.time()
            df_k = topk(df, lon, lat, k)
            end = time.time()

            df = df.reset_index(drop=True)

            list_time.append(end-start)
        list_cal_k.append(np.average(list_time))

    r_analysis = DataFrame({
        'r': range(1, 50),
        'time': list_cal_k
    })
    return r_analysis


