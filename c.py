#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd

import jieba


def loadData(filepath):
    compare = list()
    workbook1 = xlrd.open_workbook(filepath,encoding_override="gbk")
    booksheet2 = workbook1.sheet_by_name('feedback')
    #Compare

    rows = booksheet2.nrows
    mark = True
    lineCount = 0
    for i in range(rows):
        if mark:
            mark=False
            continue
        array = booksheet2.row_values(i)
        text = array[4]
        if type(text) == type(3.4):
            continue

        divideWord = jieba.cut(text,cut_all=False)
        divideWord = [str(word) for word in divideWord if word != '']

        compare.append((text,','.join(divideWord)))
        

    return compare
def output(outputPath,compare):

    with open(outputPath,'w') as f:
        for x1,x2 in compare:
            x2 = x2.replace('\n',',')
            x2 = x2.replace('\r',',')
            f.write('%s & %s\n' % (x1.decode('utf-8').encode('utf-8'),x2.decode('utf-8').encode('utf-8')))
            

if __name__=='__main__':

    outputPath = r'nova.csv'
    reportPath2 = r'report_tlbb2.xlsx'
    reportPath1 = r'report_tlbb1.xlsx'

    compare1 = loadData(reportPath2)
    compare2 = loadData(reportPath1)
    compare = compare1
    compare.extend(compare2)
    output(outputPath,compare)

