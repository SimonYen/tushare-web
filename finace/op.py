# 流动比率(current ratio)指流动资产总额和流动负债总额之比
# 资产负债率，是总负债与总资产的百分比
# 简称ROA，资产净利润率、资产报酬率或资产收益率，是企业在一定时期内的净利润和资产平均总额的比率
import tushare as ts
import pandas as pd
from . import name2code

ts.set_token('41addd8c3955aea5623099855def5d5ae794632258ad289d8fd02fb6')
pro = ts.pro_api('41addd8c3955aea5623099855def5d5ae794632258ad289d8fd02fb6')


def get_all_name_and_code() -> pd.DataFrame:
    """
    获取公司的名字，股票代码等等信息。
    :return: DataFrame格式，方便遍历以及生成文件
    """
    df = pro.query('stock_basic',
                   exchange='', list_status='L',
                   fields='ts_code,name, enname, area,industry,list_date')
    change = {
        'ts_code': '股票代码',
        'name': '股票名称',
        'enname': '英文全称',
        'area': '地域',
        'industry': '所属行业',
        'list_date': '上市时间',
    }
    df.rename(columns=change, inplace=True)

    return df


def get_asset(name: str, begin_date: str, end_date: str) -> pd.DataFrame:
    """
    获取资产负债表，注意date要去掉-
    :param:ts_code股票代码
    :return:DataFrame
    """
    if name not in name2code:
        return None
    bd = begin_date.replace('-', '')
    ed = end_date.replace('-', '')
    df = pro.balancesheet(ts_code=name2code[name], start_date=bd, end_date=ed,
                          fields='ts_code,ann_date,total_nca,total_cur_assets,total_cur_liab,total_assets,total_liab')
    change = {
        'ts_code': '股票代码',
        'ann_date': '公告日期',
        'total_nca': '非流动资产合计',
        'total_cur_assets': '流动资产合计',
        'total_cur_liab': '流动负债总计',
        'total_assets': '资产总计',
        'total_liab': '负债总计'
    }
    df.rename(columns=change, inplace=True)
    return df


def get_gain(name: str, begin_date: str, end_date: str) -> pd.DataFrame:
    """
    获取利润表，注意date要去掉-
    :param:ts_code股票代码
    :return:DataFrame
    """
    if name not in name2code:
        return None
    bd = begin_date.replace('-', '')
    ed = end_date.replace('-', '')
    df = pro.income(ts_code=name2code[name], start_date=bd, end_date=ed,
                    fields='ts_code,ann_date,total_profit,n_income')
    change = {
        'ts_code': '股票代码',
        'ann_date': '公告日期',
        'total_profit': '利润总和',
        'n_income': '净利润'
    }
    df.rename(columns=change, inplace=True)
    return df
