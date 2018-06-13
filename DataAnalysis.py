# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import pandas as pd
import time
import numpy as numpy
import pandas as pd
import folium

import os
import sys


from math import radians, cos, sin, asin, sqrt
import random

from mapboxgl.utils import *
from mapboxgl.viz import *
from pyecharts import Bar
from pyecharts import Pie, Geo, Timeline, Map
from PyQt5.QtWidgets import *

from pyecharts import Bar
import pyecharts.echarts.events as events
from pyecharts_javascripthon.dom import alert,window


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView


import time


def read_data():
    data_url = 'temp.csv'
    df = pd.read_csv(data_url, header=0)
    df.columns = ['Brand', 'Store Number', 'Store Name', 'Ownership Type', 'Street Address', 'City', 'State/Province',
                  'Country', 'Postcode', 'Phone Number', 'Timezone', 'lon', 'lat','Average Score','Numofusers']
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
    return df


def time_preprocessing(df):
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
    df.insert(0, 'Timezone', timezone)
    return df

def group(df, a_list):
    df_gp = df.groupby(a_list).size()
    df_gp = df_gp.to_frame()
    return df_gp


def count_by_group(df_gp, asc):
    df_gp.columns = ['count']
    df_gp = df_gp.sort_values(by=['count'], ascending=asc)
    df_gp_index = df_gp.reset_index(drop=False)
    return df_gp_index


def draw_distribution_map(world_geo, df_gp_index, string, save_path):
    star_map = folium.Map(location=[-121, 38.5], tiles='Mapbox Bright', zoom_start=3.5)
    star_map.choropleth(geo_data=world_geo, data=df_gp_index,
                        columns=[string, 'count'],
                        key_on='feature.properties.POSTAL',
                        threshold_scale=[0, 2000, 5000, 9000, 12000, 15000],
                        fill_color='YlOrRd', fill_opacity=0.6, line_opacity=0.3,
                        legend_name='Amount of Starbucks in the country')
    star_map.save(os.path.join('D:\\file\starbucks', save_path))


def bar_pic(bar, df_gp_index, x_label, y_label, name):
    attr = []
    v = []
    for index, value in enumerate(df_gp_index[x_label]):
        attr.append(df_gp_index[x_label][index])
        v.append(df_gp_index[y_label][index])
    # bar = Bar("Bar chart", name)
    bar.add(name, attr, v)
    # bar.render(path= save_path)
    return bar


def pie_pic(df_gp_index, name, x_label, y_label):
    pie = Pie(name)
    attr = []
    v = []
    for index, value in enumerate(df_gp_index[x_label]):
        attr.append(df_gp_index[x_label][index])
        v.append(df_gp_index[y_label][index])
    pie.add(name, attr, v, is_label_show=True, radius=[30, 55], rosetype='radius')
    return pie


def create_geojson(df, json_file):
    df_to_geojson(
        df,
        filename=json_file,
    )


def on_click():
    alert("评分吧")


def geo_formatter(params):
    return params.name
           # + '\n' + 'Phone Number:' + params.name[2][0] + \
           # '\n' + 'Street Address' + params.value[2][1] + '\n'+'Score'+ params.value[2][2]


# category_color_stops要传颜色列表
def draw_map(df, map_html):
    geo = Geo("星巴克店铺分布图",
              title_color="#fff", title_pos="center",
              width=1200, height=500, background_color='#404a59')
    # df['Store Name'] = df['Store Name'].fillna("")
    # df['Store Number'] = df['Store Number'].fillna("")
    # print(type(df['Store Name'][0]))
    # print(type(df['Store Number'][0].encode("utf-8")))
    # print(type(df['Phone Number'][0].encode("utf-8")))
    # df['Phone Number'] = df['Phone Number'].fillna("")
    df = df[['Store Name']]
    geo_cities_coords = {df.iloc[i]['Store Name']: [df.iloc[i]['lon'], df.iloc[i]['lat']] for i in range(len(df))}
    # attr = list(df['Store Name'])
    value = list(df['Average Score'])
    attr = list(df['Store Name'])
    # for i in range(len(df)):
    #     attr.append([df.iloc[i]['Store Name'],df.iloc[i]['Phone Number'].encode("utf-8")])
    # print(attr[0][0])
    # name = [[df.iloc[i]['Store Number'],df.iloc[i]['Phone Number'], df.iloc[i]['Street Address'], df.iloc[i]['Average Score']] for i in range(len(df))]
    geo.add("", attr, value,
            visual_range=[0, 10], visual_text_color="#fff",
            visual_split_number=5,
            maptype="world",
            is_visualmap=True, is_piecewise=True,
            symbol_size=5, center=(-121, 38.5),
            tooltip_formatter=geo_formatter,
            geo_cities_coords=geo_cities_coords)
    # geo.on(events.MOUSE_CLICK, on_click)
    geo.render(map_html)


def draw_timezone_map(df, map_html):
    geo = Geo("星巴克时区分布地图",
              title_color="#fff", title_pos="center",
              width=1200, height=700, background_color='#404a59')
    geo_cities_coords = {df.iloc[i]['Store Name']: [df.iloc[i]['lon'], df.iloc[i]['lat']] for i in range(len(df))}
    attr = list(df['Store Name'])
    value = list(df['timezone_amount'])
    geo.add("", attr, value, visual_text_color="#fff",
            maptype="world",
            visual_range=[0, 2000],
            is_visualmap=True,
            symbol_size=5, center=(-121, 38.5),
            tooltip_formatter=geo_formatter,
            geo_cities_coords=geo_cities_coords)
    geo.render(map_html)


