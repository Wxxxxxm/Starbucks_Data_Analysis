from math import sin, asin, cos, radians, fabs, sqrt
import numpy as np
import pandas as pd
from Geohash import encode

EARTH_RADIUS = 6371

# 计算距离
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
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # average radium of the earth , kilometer
    return c * r


# 排序
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
    first_exchange_elem = (int)(length / 2) - 1
    for x in range(first_exchange_elem + 1):
        heap_adjust(arr, first_exchange_elem - x, length)
    return arr


def topk_heap(df, lon, lat, k):
    dis = []

    for index in range(df.shape[0]):
        distance = haversine(df['lat'][index], df['lon'][index], lat, lon)
        dis.append(distance)
    df.insert(0, 'distance', dis)
    df.set_index('distance', inplace=True, drop=True)
    arr = np.array(dis)
    res = np.zeros(k)
    for i in range(k):
        res[i] = arr[i]

    res = top_heap_sort(res)
    for i in range(k, len(arr)):
        if arr[i] < res[0]:
            res[0] = arr[i]
            res = top_heap_sort(res)
    res = res.tolist()
    res = list(set(res))
    df_top = pd.DataFrame(columns=['Brand', 'Store Number', 'Store Name', 'Ownership Type', 'Street Address', 'City', 'State/Province',
                 'Country', 'Postcode', 'Phone Number', 'Timezone', 'lon', 'lat'])
    for index in range(len(res)):
        df_top = df_top.append(df.loc[[res[index]]])
    # df = df.drop(['distance'], axis=1)
    return df_top


def quick_sort(df, lon, lat, k):
    dis = []

    for index in range(df.shape[0]):
        distance = get_distance_hav(df['lat'][index], df['lon'][index], lat, lon)
        # distance = distance.astype('float32')
        dis.append(distance)
    df.insert(0, 'distance', dis)
    df.set_index('distance', inplace=True, drop=True)

    list_k = quick(dis, 0, len(dis)-1)

    list_k = list(set(list_k))

    df_topk = pd.DataFrame(columns=['Brand', 'Store Number', 'Store Name', 'Ownership Type', 'Street Address', 'City', 'State/Province',
                  'Country', 'Postcode', 'Phone Number', 'Timezone', 'lon', 'lat'])
    for i in range(min(k, len(list_k))):

        df_topk = df_topk.append(df.loc[[list_k[i]]])
        if df_topk.shape[0] > k:
            df_topk = df_topk.head(k)
    return df_topk


def quick(a, left, right):
    if left > right:
        return
    temp = a[left]
    i = left
    j = right
    while i != j:
        while a[j] >= temp and i < j:
            j = j-1
        while a[i] <= temp and i < j:
            i = i+1
        if i < j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
    a[left] = a[i]
    quick(a, left, i-1)
    quick(a, i+1, right)
    return a


def preprocessing(df):
    h4 = []
    h3 = []
    h2 = []
    h1 = []
    for index in range(df.shape[0]):
        h = encode(df['lat'][index], df['lon'][index], 4)
        h4.append(h)
        h3.append(h[0:3])
        h2.append(h[0:2])
        h1.append(h[0])
    df.insert(0, 'h4', h4)
    df.insert(0, 'h3', h3)
    df.insert(0, 'h2', h2)
    df.insert(0, 'h1', h1)
    return df
