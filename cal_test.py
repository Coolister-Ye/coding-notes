

"""
注意，使用脚本前先请安装pandas:    pip install pandas

usage: calc_score.py [-h] [-d D] [-w W] [-dates DATES [DATES ...]]

check input and calc scores.

optional arguments:
  -h, --help            show this help message and exit
  -d D                  指定件量预测和排班结果所在文件夹,
                        件量预测文件名必须为pred.csv,小哥排班文件名必须为sche.json
  -w W                  小哥列表文件
  -dates DATES [DATES ...]
                        预测和排班的日期

Example: python calc_score.py -d test_dir -dates 2020-08-11 2020-08-12
2020-08-13
"""



from collections import Counter
import pandas as pd
import numpy as np
import json
import argparse
import os


def check_constraint(sche):
    c = Counter()
    for zone,ids in sche.items():
        for _id in ids:
            c[_id] += 1
            
    return not any(v > 1 for v in c.values())


def calc_score(sches,predict,workers,date):
    predict = predict[predict['date_str'] == date]
    d = predict.set_index('zone_id')[['pai_num','shou_num']].to_dict()
    shou = d['shou_num']
    pai = d['pai_num']
    
    sche = sches[date]

    if not check_constraint(sche):
        raise Exception("bad sche input")

    cost = 0.0
    for i in range(30):
        zone = "zone_%s" % i
        ids = sche.get(zone,[])

        s,p = shou[zone],pai[zone]
        ws = workers[workers.index.isin(ids)]
        caps_shou = ws['收件能力'].sum()
        caps_pai = ws['派件能力'].sum()
        c = ws['保底收入'].sum()
        
        cost += c
        cost += max(p-caps_pai,0) * 12
        cost += max(s-caps_shou,0) * 18
        cost += min(p,caps_pai) * 1.0
        cost += min(s,caps_shou) * 1.0
        
    return cost

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='check input and calc scores.',epilog='Example: python calc_score.py -d test_dir  -dates 2020-08-11 2020-08-12 2020-08-13')
    parser.add_argument('-d', help='指定件量预测和排班结果所在文件夹, 件量预测文件名必须为pred.csv,小哥排班文件名必须为sche.json')
    parser.add_argument('-w',  help='小哥列表文件',default='小哥列表.csv')
    parser.add_argument('-dates',  help='预测和排班的日期',nargs='+')

    args = parser.parse_args()

    with open(os.path.join(args.d,'sche.json')) as f:
        sches = json.load(f)
        
    predict = pd.read_csv(os.path.join(args.d,'pred.csv'))
    predict['date_str'] = pd.to_datetime(predict['date_str'])
    predict['pai_num'] = predict['pai_num'].round()
    predict['shou_num'] = predict['shou_num'].round()
    workers = pd.read_csv(args.w)
    workers = workers.set_index('小哥id')

    for date in args.dates:
        print (date,calc_score(sches,predict,workers,date))


    
    


