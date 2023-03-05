import tushare as ts

ts.set_token('41addd8c3955aea5623099855def5d5ae794632258ad289d8fd02fb6')
pro = ts.pro_api('41addd8c3955aea5623099855def5d5ae794632258ad289d8fd02fb6')

name2code = dict()
code2name = dict()

# 刷新数据
name2code.clear()
code2name.clear()
data = pro.query('stock_basic',
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
data.rename(columns=change, inplace=True)

for _, row in data.iterrows():
    name2code[row['股票名称']] = row['股票代码']
    code2name[row['股票代码']] = row['股票名称']
