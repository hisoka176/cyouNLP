#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from  gensim import corpora,models,similarities
import os
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',filename='./mylog.log', level=logging.INFO)

def process():
    result = []
    with open(r'nova.csv') as f:
        for line in f:
            array = line.rstrip('\n').split("&")

            if len(array)!=2:
                continue
            divideWord = array[1].split(',')
            divideWord = [i  for i in divideWord if i !='']
            if len(divideWord)==0:
                continue
            result.append(divideWord)

    return result

def transform(result):
    dictionary = corpora.Dictionary(result);
    dictionary.save("/tmp/result.dict")
    print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in result]
    corpora.MmCorpus.serialize("/tmp/corpora.mm",corpus)
    print(corpora)
def train():
    if os.path.exists("/tmp/result.dict"):
        dictionary = corpora.Dictionary.load("/tmp/result.dict")
    else:
        print("no file1")
    if os.path.exists("/tmp/corpora.mm"):
        corpus = corpora.MmCorpus("/tmp/corpora.mm")
    else:
        print("no file2")
    lda  = models.LdaModel(corpus, id2word=dictionary, num_topics=100)
    print('-----------------')
    lda.print_topics(100)

    lda.save("/tmp/model.lda")

def getModel():
    lda  = models.LdaModel.load("/tmp/model.lda")
    print(lda)
    lda.print_topics(100)
    if os.path.exists("/tmp/corpora.mm"):
        corpus = corpora.MmCorpus("/tmp/corpora.mm")
    else:
        print("no file2")

    num = 0
    for cor in corpus:
        print(lda[cor])
        if num >10:
            break
        num += 1
if __name__=='__main__':
#    result = process()
#    transform(result)
#    train()
    getModel()
