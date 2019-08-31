import nltk
from nltk.corpus import stopwords
import re
import numpy as np

def scorehim(him):
    
    sample1=him
    tsample1=nltk.sent_tokenize(sample1)
    #print(tsample1)
    stopwrds=set(stopwords.words('english'))

    tsample=nltk.word_tokenize(sample1)



    #Refine Data
    ntsample2=[w for w in tsample if not w in stopwrds]
    ntsample=[]
    for i in ntsample2:
        ntsample.append(i.lower())
    ntsampler=[i for i in ntsample if i.isalpha()]

    

    ntsampler = list(filter(None, ntsampler)) 
    ntsampler.sort()
    #for i in ntsampler:
        #print(i)    
        
    #print(ntsample,"\n")
    #print(ntsampler)




    #Word Count
    countsam=[]
    count=0
    for i in range(len(ntsampler)):
        if ntsampler[i] not in countsam:
            countsam.append(ntsampler[i])

    countsam.sort()
    b=[]
    for i in countsam:
        c=ntsampler.count(i)
        b.append(c)
    #print(countsam)
    #print(b)






    #Scoring
    exps = [np.exp(i) for i in b]
    sum_of_exps = sum(exps)
    f = [j/sum_of_exps for j in exps]

    g=dict(zip(countsam,f))
    li=g.items()


    #Ranking Sentences
    senval=[]
    for i in tsample1:
            
            val=0
            senword=nltk.word_tokenize(i)
            for j in senword:
                if j in countsam:
                    pl=countsam.index(j)
                    val+=f[pl]
            senval.append(val)

    d=[]
    re=[]
    d=senval
    d.sort()
    if len(d)<5:
        for i in d:
            re.append(i)
    else:
        for i in range(1,6):
            re.append(d[i])
    re.sort()
    fs=dict(zip(tsample1,senval))
    fs2=fs.items()


        
    #Selecting Sentence
    summary=[]
    for i in re:
        v=senval.index(i)
        summary.append(tsample1[v])
        
        
    return(summary)