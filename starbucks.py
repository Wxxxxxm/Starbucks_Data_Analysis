# coding: utf-8

import Tkinter as tk
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd
import folium
import re
import numpy as np
import subprocess
import random

from PIL import Image

from mapboxgl.utils import *
from mapboxgl.viz import *


###############################################
def read_data():
    data_url = 'D:\\file\Starbucks.csv'
    df = pd.read_csv(data_url, header=0)
    df.columns = ['Brand', 'Store Number', 'Store Name', 'Ownership Type', 'Street Address', 'City', 'State/Province',
                  'Country', 'Postcode', 'Phone Number', 'Timezone', 'lon', 'lat']
    # Only Brand as Starbucks
    # #df.loc[df['Brand'].isin(['Starbucks'])]
    df['lon'] = df['lon'].fillna(0)
    df['lat'] = df['lat'].fillna(0)
    # Convert Elevation series to float
    df['lon'] = df['lon'].astype(float)
    df['lat'] = df['lat'].astype(float)
    # Clean up by dropping null rows
    df = df.dropna(axis=1, how='all')
    df.fillna('', inplace=True)
    df = df.drop_duplicates('Store Number', keep="first", inplace=False)
    # reset index  duplicate droped
    df = df.reset_index(drop=True)
    time = []
    timezone = []
    for i in range(df.shape[0]):
        arr = df['Timezone'][i].split(' ')
        if arr[0] == 'GMT+000000':
            arr[0] = 'GMT+0:00'
        if arr[0] == 'GMT+05:30':
            arr[0] = 'GMT+05:00'
        if arr[0] == 'GMT-03:30':
            arr[0] = 'GMT-03:00'
        timezone.append(' '.join(arr))
        time.append(arr[0])
    df = df.drop(['Timezone'], axis=1)
    df.insert(0, 'Time', time)
    return df


def group(df, a_list):
    df_gp = df.groupby(a_list).size()
    df_gp = df_gp.to_frame()
    return df_gp


def count_by_group(df_gp, string):
    df_gp.columns = ['count']
    df_gp_index = df_gp.reset_index(drop=False)
    df_gp_index.sort_values([string], ascending=True)
    return df_gp


def draw_distribution_map(world_geo, df_gp_index):
    star_map = folium.Map(location=[-121, 38.5], tiles='Mapbox Bright', zoom_start=3.5)
    star_map.choropleth(geo_data=world_geo, data=df_gp_index,
                        columns=['Country', 'count'],
                        key_on='feature.properties.POSTAL',
                        threshold_scale=[0, 2000, 5000, 9000, 12000, 15000],
                        fill_color='YlOrRd', fill_opacity=0.6, line_opacity=0.3,
                        legend_name='Amount of Starbucks in the country')
    star_map.save(os.path.join('D:\\', 'star_map.html'))


def bar_pic(df_gp, x_label, y_label, file_name):
    plt.figure(figsize=(20, 18), dpi=100)
    df_gp.plot(kind="bar")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(file_name)#改成子窗口显示


def create_geojson(df, json_file):
    df_to_geojson(
        df,
        filename=json_file,
        # properties=['Brand','Store Number', 'Store Name', 'Ownership Type', 'Street Address','City','State/Province','Country','Postcode','Phone Number','Timezone'],
    )


def draw_map(json_file, category_color_stops, color_property, html_name):
    # Initialize CircleViz with Categorical Measure Data
    viz = CircleViz(
        data=json_file,
        access_token='pk.eyJ1Ijoid3h0ZW5nIiwiYSI6ImNqZjZ4dm00YTAwazIycW9iYW1ydDhsZXQifQ.yHJQ23MnMf1t7PEo4Hxj7g',
        height='500px',
        # opacity=1,
        color_property=color_property,
        # color_default='grey',
        color_function_type='match',
        color_stops=category_color_stops,
        # center=(-121, 38.5),
        zoom=3
        )
    html = viz.create_html()
    map_html = viz.as_iframe(html)
    with open(html_name, 'w') as f:
        f.write(map_html)

# ##################################################


if __name__ == "__main__":
    # 读取数据
    starbucks_df = read_data()
    # 转为json文件
    starbucks_json_file = "starbucks.geojson"
    create_geojson(starbucks_df, starbucks_json_file)
    # 设置geo信息
    starbucks_world_geo = 'G:\\world.json'

    # 国家数量统计
    df_con = group(starbucks_df, 'Country')
    df_con_index = count_by_group(df_con, 'count')
    draw_distribution_map(starbucks_world_geo, df_con_index)
    # 国家数量统计柱状图【图】【改】
    # bar_pic(df_con_index, 'Country', 'count', 'G:\\country.jpg')

    # 所有星巴克分布地图
    starbucks_category_color_stops = [['Starbucks', 'rgb(211,47,47)'], ]
    draw_map(starbucks_json_file, starbucks_category_color_stops, 'Brand', 'fenbutu.html')

    # 时区数量统计
    df_time = group(starbucks_df, 'Time')
    df_time_index = count_by_group(df_time, 'count')
    # 时区数量统计柱状图【图】【改】
    # bar_pic(df_time_index, 'Time', 'count', 'D:\\timezone.jpg')

    # 时区内小时区的数量统计
    df_gp = group(starbucks_df, ['Time', 'Timezone'])
    df_gp.columns = ['count']
    df_index = group(starbucks_df, ['Time'])
    df_index = df_index.reset_index(drop=False)
    for i in range(df_index.shape[0]):
        string = df_index['Time'][i]
        df_a_time = df_gp['count'][string].to_frame()
        # 这里的df_a_time就是各个时区内的dataframe可以直接画图【图】

    # 按时区的所有星巴克分布地图
    starbucks_category_color_time = []
    for index, value in enumerate(df_time_index['Timezone']):
        i = random.randint(0, 255)
        j = random.randint(0, 255)
        k = random.randint(0, 255)
        starbucks_category_color_time.append([df_time_index['Timezone'][index], 'rgb(%s,%s,%s)' % (i, j, k)])
    draw_map(starbucks_json_file, starbucks_category_color_time, 'Timezone', 'map_time.html')

    window = tk.Tk()
    window.title('星巴克数据分析')
    window.geometry('400x200')

    canvas = tk.Canvas(window, bg='white', height=150, width=200)

    def b1():
        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '1236'])  # change the duankou
        webbrowser.open_new_tab('http://localhost:1236/fenbutu.html')  # open the html
    b1 = tk.Button(window, text='店铺地区分布图及信息', command=b1)

    def b2():
        image_file = tk.PhotoImage(file='G:\\country.jpg')
        label_img = tk.Label("country", image=image_file)
        label_img.pack()
        # img = Image.open('D:\\country.png')
        plt.figure("country")
        # plt.imshow(img)
        # plt.axis('off')
        plt.show()
    b2 = tk.Button(window, text='国家数量柱状图', command=b2)

    def b3():
        subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '1236'])  # change the duankou
        webbrowser.open_new_tab('http://localhost:1236/map_time.html')  # open the html
    b3 = tk.Button(window, text='店铺时区分布图', command=b3)

    def b4():
        img2 = Image.open('G:\\timezone.jpg')
        plt.figure("timezone")
        plt.imshow(img2)
        plt.show()
    b4 = tk.Button(window, text='店铺时区数量柱状图', command=b4)

    def b5():
        webbrowser.open_new_tab('G:\\star_map.html')  # open the html
    b5 = tk.Button(window, text='不同国家的数量渐变图', command=b5)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
window.mainloop()
