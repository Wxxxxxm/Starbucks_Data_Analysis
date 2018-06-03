from DataAnalysis import *
from math import sin, asin, cos, radians, fabs, sqrt
from Geohash import encode
import  jdt


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
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # average radium of the earth , kilometer
    return c * r * 1000


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


def topk_heap(df, lon, lat, k):
    dis = []
    # print(df)
    for index in range(df.shape[0]):
        distance = haversine(df['lat'][index], df['lon'][index], lat, lon)
        dis.append(distance)
    df.insert(0, 'distance', dis)
    df.set_index('distance', inplace=True, drop=True)
    arr = np.array(dis)
    res = np.zeros(k)
    for i in range(k):
        res[i] = arr[i]
    # print(res)
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


def calculate(df, lon, lat, k):
    dis = []
    for index in range(df.shape[0]):
        distance = get_distance_hav(df['lat'][index], df['lon'][index], lat, lon)
        dis.append(distance)
    df.insert(0, 'distance', dis)
    # df.set_index('distance', inplace=True, drop=False)
    df_k = df.sort_values(by=['distance'], ascending=True).head(k)
    df_k = df_k.reset_index(drop=True)
    return df_k


def quick_sort(df, lon, lat, k):
    dis = []
    # print(df)
    for index in range(df.shape[0]):
        distance = get_distance_hav(df['lat'][index], df['lon'][index], lat, lon)
        # distance = distance.astype('float32')
        dis.append(distance)
    df.insert(0, 'distance', dis)
    df.set_index('distance', inplace=True, drop=True)
    # print(df)
    list_k = quick(dis, 0, len(dis)-1)
    # print(list_k)
    list_k = list(set(list_k))
    # print(len(list_k))
    df_topk = pd.DataFrame(columns=['Brand', 'Store Number', 'Store Name', 'Ownership Type', 'Street Address', 'City', 'State/Province',
                  'Country', 'Postcode', 'Phone Number', 'Timezone', 'lon', 'lat'])
    for i in range(min(k, len(list_k))):
        # print(df.loc[[list_k[i]]])
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


def topk(df, lon, lat, k):
    h_goal = encode(lat, lon, 4)
    df1 = df
    #ex=jdt.Example()
   # ex.show()
    if df1[df1.h1 == h_goal[00000]].shape[0] > k:
        df1 = df1[df1.h1 == h_goal[0]]
        #jdt.Example().setValue(25)
        if df1[df1.h2 == h_goal[0:2]].shape[0] > k:
            df1 = df1[df1.h2 == h_goal[0:2]]
            if df1[df1.h3 == h_goal[0:3]].shape[0] > k:
                df1 = df1[df1.h3 == h_goal[0:3]]
                if df1[df1.h4 == h_goal[0:4]].shape[0] > k:
                    df1 = df1[df1.h4 == h_goal[0:4]]
    df1 = df1.reset_index(drop=True)
    # print(df1)
    df_res = calculate(df1, lon, lat, k)
    return df_res

def topk_k_analysis(df,lon,lat):
    list_time = []
    for i in range(1, 50):
        k = 100*i
        #print(k)
        start = time.time()
        df_k = topk(df, lon, lat, k)
        end = time.time()
        #print(df_k)
        #print('---------------------------------------------')
        df = df.reset_index(drop=True)
        list_time.append(end-start)
        #print list_time
    k_analysis = DataFrame({
        'k': range(1, 50),
        'time': list_time
    })
    k_analysis.transpose()
    print(len(k_analysis['k']),len(k_analysis['time']))
    return k_analysis


def topk_analysis(df):
    list_cal_k = []
    for i in range(1, 50):
        k = 100*i
        list_time = []
        print(k)
        for m in range(2):
            lon = random.uniform(-180, 180)
            lat = random.uniform(-90, 90)
            start = time.time()
            df_k = topk(df, lon, lat, k)
            end = time.time()
            print(lon)
            print(lat)
            print(df_k)
            print('---------------------------------------------')
            # df = df.drop(['distance'], axis=1)
            df = df.reset_index(drop=True)
            # df = df.drop(['distance'], axis=1)
            list_time.append(end-start)
        list_cal_k.append(np.average(list_time))
    print list_cal_k
    r_analysis = DataFrame({
        'r': range(1, 50),
        'time': list_cal_k
    })
    return r_analysis


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

"""
if __name__ == "__main__":

    starbucks_df = read_data()
    h4 = []
    h3 = []
    h2 = []
    h1 = []
    for index in range(starbucks_df.shape[0]):
        h = encode(starbucks_df['lat'][index], starbucks_df['lon'][index], 4)
        h4.append(h)
        h3.append(h[0:3])
        h2.append(h[0:2])
        h1.append(h[0])
    starbucks_df.insert(0, 'h4', h4)
    starbucks_df.insert(0, 'h3', h3)
    starbucks_df.insert(0, 'h2', h2)
    starbucks_df.insert(0, 'h1', h1)
    # starbucks_df.set_index('h3', inplace=True, drop=True)
    # print(starbucks_df)
    # df_topk = topk(starbucks_df, 112, 26, 5)
    # print(df_topk)
    df_topkk=preprocessing(starbucks_df)
    df_topkk=topk_k_analysis(starbucks_df,113.23,23.40)
    print(df_topkk)
    bar2 = Bar("topk time with different k ")
    bar2 = bar_pic(bar2, df_topkk, 'k', 'time', 'Analysis Bar')
    bar2.render('TOPK_Analysis_with_growing_k.html')
    df_analysis = topk_analysis(starbucks_df)
    bar = Bar("SORT Time Analysis with geohash")
    bar = bar_pic(bar, df_analysis, 'r', 'time', 'Analysis Bar')
    bar.render('TOPK_Analysis_SORT_with_geohash.html')


    
    df_analysis = topk_analysis(starbucks_temp)
    bar = Bar("SORT Time Analysis with geohash")
    bar = bar_pic(bar, df_analysis, 'r', 'time', 'Analysis Bar')
    bar.render('TOPK_Analysis_SORT_with_geohash.html')"""