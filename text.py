import openpyxl 

#读取的代码：
wb = openpyxl.load_workbook('电气.xlsx')
sheet = wb['new title']
colB=sheet['B']
data=[]
for B in colB:
    data.append(B.value)
s=''.join(data)
print(s)