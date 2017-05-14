#encoding:utf-8
import numpy as np
import scipy as sp
import sklearn
import gensim
import xlrd
import xlwt
import jieba


print("fdsfsdfds")
reportPath1 = r'../../../dataset/report_tlbb1.xlsx'
reportPath2 = r'../../../dataset/report_tlbb2.xlsx'
workbook1 = xlrd.open_workbook(reportPath1,encoding_override="gbk")
workbook2 = xlrd.open_workbook(reportPath2,encoding_override="gbk")
booksheet1 = workbook1.sheet_by_name('feedback') 
booksheet2 = workbook2.sheet_by_name('feedback')

#Compare
compare = list()
rows = booksheet1.nrows
mark = True
lineCount = 0
for i in range(rows):
    if mark:
        mark=False
        continue
    array = booksheet1.row_values(i)
    text = array[4]
  
    if type(text)!=type(''):
        continue
  
    divideWord = jieba.cut(text,cut_all=False)
  
    divideWord = [str(word) for word in divideWord if word != '']
 
    compare.append((text,','.join(divideWord)))
     
    
 
rows = booksheet2.nrows
mark = True
lineCount = 0
for i in range(rows):
    if mark:
        mark = False
        continue
    array = booksheet2.row_values(i)
    text = array[4]
    if type(text)!=type(''):
        continue
    
    divideWord = jieba.cut(text,cut_all=False)
 
    divideWord = [str(i) for i in divideWord if i !='']
    compare.append((text,','.join(divideWord)))
    
outputPath = r'../../../output/compare.csv'
with open(outputPath,'w',encoding="utf-8") as f:
    for x1,x2 in compare:
        x2 = x2.replace('\n',',')
        x2 = x2.replace('\r',',')
        f.write('%s & %s\n' % (x1,x2))
        
print("over")

if __name__=='__main__':
    pass