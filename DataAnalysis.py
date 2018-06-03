# -*- coding: UTF-8 -*-

import Tkinter as tk
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd
import folium
import time
import matplotlib.image as mping
import matplotlib as mpl
import numpy as numpy
import pandas as pd
import folium
import os
import subprocess
import random
import sys

from PIL import Image

from mapboxgl.utils import *
from mapboxgl.viz import *
from math import radians, cos, sin, asin, sqrt
import subprocess
import random

from PIL import Image

from mapboxgl.utils import *
from mapboxgl.viz import *
from pyecharts import Bar
from pyecharts import Pie, Timeline
from miniheap2 import *
###############################################

sys.setrecursionlimit(1000000)
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
    df.insert(0,'Timezone',timezone)
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


# category_color_stops要传颜色列表
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