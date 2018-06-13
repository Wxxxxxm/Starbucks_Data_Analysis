# -*- coding:utf-8 -*-
import difflib
import Levenshtein
from pandas.core.frame import DataFrame
from DataAnalysis import *
from k import *


def find_same(df, attr, query_str):
    res = []
    res.append(query_str)
    df_res = df[df[attr].isin(res)]
    if df_res.empty:
        df1 = df.copy()
        str_list = df1.pop(attr).tolist()# pop:弹出指定列并返回series
        df_res = find_similar(df, attr, query_str, str_list)
    return df_res


# 找相似的 str_list是查找的范围，query_str是查找的目标，attr是查找的属性
def find_similar(df, attr, query_str, str_list):
    df_temp=df
    similarity = []
    for index in range(len(str_list)):
        # 文本相似度————编辑距离
        # 用difflib库
        # sim = difflib.SequenceMatcher(None, query_str, str_list[index]).quick_ratio()
        # 用Levenshtein库,计算相似度距离的函数
        # sim = Levenshtein.ratio(query_str, str_list[index])
        # 文本相似度————汉明距离
        if len(str_list[index])-len(query_str) > 0:
            hanming = []
            for i in range(len(str_list[index])-len(query_str)+1):
                str_comp = str_list[index][i:i+len(query_str)]
                han = sum(el1 == el2 for el1, el2 in zip(str_comp, query_str))
                hanming.append(han)
            sim = numpy.max(hanming)
        else:
            hanming = []
            for i in range(len(query_str) - len(str_list[index]) + 1):
                str_comp = query_str[i:i + len(str_list[index])]
                han = sum(el1 == el2 for el1, el2 in zip(str_comp, str_list[index]))
                hanming.append(han)
            sim = numpy.max(hanming)
        similarity.append(sim)


    # similarity是相似度列表 比较两种方法的正确程度可能可以从similarity入手？
    # print(similarity)
    df_str = {"similarity": similarity,
              "str": str_list}
    str_with_sim = DataFrame(df_str)
    #print str_with_sim
    # 可以设置head里面的数字来控制最接近的n个值 根据相似度距离来对dataframe进行排序，
    # str_with_sim = str_with_sim.drop_duplicates().sort_values(by=['similarity'], ascending=False).head(2)
    str_with_sim = str_with_sim[str_with_sim.similarity == max(similarity)].drop_duplicates()

    res = str_with_sim.pop('str').tolist()
    df_res = df[df[attr].isin(res)]
    df_res = df_res.reset_index(drop=True)
    return df_res


def find_similar_test(query_str, str_list):
    # df_temp=df
    similarity = []
    for index in range(len(str_list)):
        # 文本相似度————汉明距离
        if len(str_list[index]) - len(query_str) > 0:
            hanming = []
            for i in range(len(str_list[index]) - len(query_str) + 1):
                str_comp = str_list[index][i:i + len(query_str)]
                han = sum(el1 == el2 for el1, el2 in zip(str_comp, query_str))
                hanming.append(han)
            sim = numpy.max(hanming)
        else:
            hanming = []
            for i in range(len(query_str) - len(str_list[index]) + 1):
                str_comp = query_str[i:i + len(str_list[index])]
                han = sum(el1 == el2 for el1, el2 in zip(str_comp, str_list[index]))
                hanming.append(han)
            sim = numpy.max(hanming)
        similarity.append(sim)

    # similarity是相似度列表 比较两种方法的正确程度可能可以从similarity入手？
    df_str = {"similarity": similarity,
              "str": str_list}
    str_with_sim = DataFrame(df_str)
    #print str_with_sim
    # 可以设置head里面的数字来控制最接近的n个值 根据相似度距离来对dataframe进行排序，
    str_with_sim = str_with_sim.drop_duplicates().sort_values(by=['similarity'], ascending=False)
    # str_with_sim = str_with_sim[str_with_sim.similarity == max(similarity)].drop_duplicates()
    print(str_with_sim)


"""
if __name__ == "__main__":
    starbucks_df = read_data()
    df_find = find_same(starbucks_df, 'City', '广州市珠海市')
    # df_find = find_similar_test('仁恒星园', ['仁恒兴园' , '仁恒明星园'])

    print(df_find)
    # df_find就是结果dataframe
    # 要画图可能要reset_index再用DataAnalysis里面的draw_map函数"""""