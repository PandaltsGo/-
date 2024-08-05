import os
import pandas
import re
import matplotlib.pyplot as plt

# 此文件用于筛选波森情感分析后高度积极和消极的语句，作为百度情感分析的语料。

name = '所有评论（波森）.txt'


def read_text(name):
    with open(f"{name}", encoding="UTF-8") as f:
        text = f.read()
        return text

def main():    txt = read_text(f"{name}")
    # re取情感评分及内容
    resp = re.findall(r"情感分析文本：(.*?)\n情感值：(\-?\d+.\d+)\n", txt, re.M)
    # print(resp)
    print("开始统计")
    x = 0
    y = 0
    m = 0
    n = 0
    for l in resp:
        # print(l[0])
        # print(l[1])
        if float(l[1]) > 2 and float(l[1]) < 3:  # 数值自己根据实际情况调整
            # write_text(f'积极语料.{name}', l[0] + "\n")
            x += 1
        if float(l[1]) > 3 and float(l[1]) < 5:  # 数值自己根据实际情况调整
            # write_text(f'积极语料.{name}', l[0] + "\n")
            y += 1.0
        elif float(l[1]) < (-2):
            # write_text(f"消极语料.{name}", l[0] + "\n")
            m += 1.0
        elif float(l[1]) > (-0.5) and float(l[1]) < 1:
            # write_text(f"中性语料.{name}", l[0] + "\n")
            n += 1.0
        else:
            continue

    print(f"积极语料数量：{x},积极语料数量:{y},消极语料数量{m},中性语料数量{n}")


if __name__ == '__main__':
    main()
