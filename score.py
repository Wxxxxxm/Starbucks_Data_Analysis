# -*- coding: UTF-8 -*-

import pandas as pd


def input_score(df, score, name):
    # if not set(['Average Score', 'Numofusers']).issubset(df.columns):
    #     df['Average Score'] = 0.0
    #     df['Numofusers'] = 0
    for i in range(len(df)):
        if (df['Store Name'][i] == name):
            df.loc[i, 'Average Score'] = average_score(df, i, score)
            df.loc[i, 'Numofusers']+= 1
            break
    return df


def average_score(df,i,score):
        sum=float(df.loc[i,'Average Score'])*int(df.loc[i,'Numofusers'])+score
        num=int(df.loc[i,'Numofusers'])+1
        return sum/num

'''
if __name__ == '__main__':
    df = read_data()
    #导入score文件之后，每一次点击一个店铺后台就可直接调用input_score函数来响应；以下为4次测试
    # df = input_score(df, 70, 'Ajman Drive Thru')
    # df = input_score(df, 0, 'Ajman Drive Thru')
    # df = input_score(df, 50, 'Ajman Drive Thru')
    # df = input_score(df, 20, 'Ajman Drive Thru')
    # print df.head(5)
    df.fillna(0)
    print(df)
    df.to_csv('temp.csv')'''
