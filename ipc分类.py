import pandas as pd

data = pd.read_excel('./分类.xlsx')
ipcList = data['分类']
total_list = []
for value in ipcList[1:]:
    # 取出每一行数据 按照分号分割成列表
    ipc_list_index = value.split(';')
    # 去重
    new_list = list(set(ipc_list_index))
    # 把去重后的列表添加到总列表里 数据按照分号拼接
    total_list.append(';'.join(new_list))

for index, value in enumerate(total_list):
    print('内容：', value)
    print('==============')
# print(total_list)
new_dict = {'ipc': pd.Series(total_list)}
dd = pd.DataFrame(new_dict)
print(dd)

#dd.to_excel('output.xlsx')
dd.to_excel('out分类.xlsx')
