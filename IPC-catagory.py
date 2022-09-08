import pandas as pd

data = pd.read_excel('./ipc.xlsx')
ipcList = data['IPC分类号']
total_list = []
length_list = []
for value in ipcList[1:]:
    # 取出每一行数据 按照分号分割成列表
    ipc_list_index = value.split(';')
    # 1、去除空格 2、取前四位  3、 覆盖原来的数值
    for index, ipc in enumerate(ipc_list_index):
        # 1、去除空格 2、取前四位
        # new_ipc = ipc.strip()[0:4]
        #取前八位
        new_ipc = ipc.strip()[0:8]
        # 3、 覆盖原来的数值
        ipc_list_index[index] = new_ipc
    # 去重
    new_list = list(set(ipc_list_index))
    # 记录每一个专利包含的ipc列表长度
    length_list.append(len(new_list))
    # 把去重后的列表添加到总列表里 数据按照分号拼接
    total_list.append(';'.join(new_list))

for index, value in enumerate(total_list):
    print('索引：', index)
    print('内容：', value)
    print('长度：', len(value))
    print('==============')
# print(total_list)
new_dict = {'ipc': pd.Series(total_list), 'lenth': pd.Series(length_list)}
dd = pd.DataFrame(new_dict)
print(dd)

#dd.to_excel('output.xlsx')
dd.to_excel('output8.xlsx')
