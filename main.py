# -*- coding:UTF-8 -*-#
from DataAnalysis import *
from mainwindowUI import *
from urllib import *
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # widget = QtWidgets.QWidget()
    # MainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow = Ui_MainWindow()
    # url = "https://www.baidu.com"
    # MainWindow.load1()

    # MainWindow.menu()
    # QWebView.load(MainWindow,url)

    """starbucks_df = read_data()
    starbucks_df_time = time_preprocessing(starbucks_df)
    # 转为json文件

    # starbucks_json_file = "starbucks.geojson"
    # create_geojson(starbucks_df, starbucks_json_file)
    # 设置geo信息
    starbucks_world_geo = r'D:\\file\world.json'

    # 国家数量统计
    df_con = group(starbucks_df, 'Country')
    df_con_index = count_by_group(df_con, True)
    df_con_index_ase = count_by_group(df_con, False)

    # 国家数量统计柱状图【图】
    bar_con = Bar("各国家内店铺数量统计柱状图")
    bar_pic(bar_con, df_con_index, 'Country', 'count', '升序')
    bar_pic(bar_con, df_con_index_ase, 'Country', 'count','降序')
    bar_con.render(r'D:\\file\starbucks\Amount_Each_Country_Bar.html')
    pie = pie_pic(df_con_index,'Amount_Each_Country','Country','count')
    pie.render(r'D:\\file\starbucks\Amount_Each_Country_Pie.html')

    # 所有星巴克分布地图
    starbucks_category_color_stops = [['Starbucks', 'rgb(211,47,47)'], ]
    draw_map(starbucks_df, r'D:\\file\starbucks\fenbutu.html')

    # 时区数量统计
    df_time = group(starbucks_df_time, 'Time')
    df_time_index = count_by_group(df_time, True)
    df_time_index_ase = count_by_group(df_time, False)
    # 时区数量统计柱状图
    bar_time = Bar("各时区内店铺数量统计")
    bar_pic(bar_time, df_time_index, 'Time', 'count','升序')
    bar_pic(bar_time, df_time_index_ase, 'Time', 'count','降序')
    bar_time.render(r'D:\\file\starbucks\Amount_in_Each_Timezone_Bar.html')
    # 时区数量统计饼状图
    pie_time = pie_pic(df_time_index,'Amount of Starbucks in Each Timezone','Time','count')
    pie_time.render(r'D:\\file\starbucks\Amout_in_Each_Timezone_Pie.html')

    # 时区内小时区的数量统计
    df_gp = group(starbucks_df_time, ['Time', 'Timezone'])
    df_gp.columns = ['count']
    df_index = group(starbucks_df_time, ['Time'])
    df_index = df_index.reset_index(drop=False)
    timeline = Timeline(is_auto_play=False, timeline_bottom=0)
    for i in range(df_index.shape[0]):
        string = df_index['Time'][i]
        df_a_time = df_gp['count'][string].to_frame()
        df_a_time = df_a_time.reset_index(drop=False)
        # 这里的df_a_time就是各个时区内的dataframe可以直接画图【图】
        # bar = bar_pic(df_a_time, 'Amount of Starbucks in ' + string, 'Timezone', 'count')
        # timeline.add(bar, string)
        pie = pie_pic(df_a_time, 'Amount of Starbucks in ' + string, 'Timezone', 'count')
        timeline.add(pie, 'Amount of Starbucks in ' + string)
    timeline.render(r'D:\\file\starbucks\Amount_of_Country_in_Timezone_Pie.html')


    # 按时区的所有星巴克分布地图
    starbucks_category_color_time = []
    timezone_amount = []
    # for index, value in enumerate(df_time_index['Time']):
    #     i = 10*index
    #    timezone_amount.append(i)
    #df_time_index.insert(0, 'amount',timezone_amount)
    print(starbucks_df_time)
    for index in range(starbucks_df_time.shape[0]):
        i = df_time_index['count'][df_time_index.Time == starbucks_df_time['Time'][index]]
        timezone_amount.append(i)
    starbucks_df_time.insert(0, 'timezone_amount', timezone_amount)
    print(starbucks_df_time)
    #    starbucks_category_color_time.append([df_time_index_ase['Time'][index], 'rgb(%s,%s,%s)' % (i, j, k)])
    draw_timezone_map(starbucks_df_time, r'D:\\file\starbucks\map_time.html')

    # 渐变图
    draw_distribution_map(starbucks_world_geo,df_con_index,'Country', 'distribution_map_country.html')"""
    # draw_distribution_map(starbucks_world_geo,df_time_index,'Time','distribution_map_time.html')


    MainWindow.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
