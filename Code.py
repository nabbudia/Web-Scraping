
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
def analyze_tf_idf(arr,K):
    tf_idf=None
    top_K=None
    tff=np.sum(arr, axis=1)
    #print(tff)
    tfff=np.reshape(tff,(3,1))
    #print(tfff)
    tf=arr/tfff
    #print(tf)
    bool_val= np.where(arr>0, 1, 0)
    df=np.sum(bool_val, axis=0)
    #print(df)
    tf_idf=tf/(np.log(df)+1)
    print(tf_idf)
    #print(type(tf_idf))
    top_K=(np.argsort(tf_idf,axis=1)[:,-K:])#[::-1])
    print(top_K)          
    return tf_idf, top_K
arr=np.array([[0,1,0,2,0,1],[1,0,1,1,2,0],[0,0,2,0,0,1]])
analyze_tf_idf(arr,3)


import pandas as pd
import csv
def analyze_data(filepath):
    df=pd.read_csv(filepath)
    #print(df)
    col=df.columns
    answercount1=df[df.answercount>0]
    largest=answercount1.nlargest(3,'viewcount')
    #print(largest)
    title_view=pd.DataFrame(largest,columns=["title", "viewcount"])
    print(title_view)
    topuser=df.quest_name.value_counts()
    topuser1=topuser.index[0:5]
    print("top 5 user who asked most question")
    print(list(topuser1))
    df["first_tag"]=df["tags"].str.split(',').apply(lambda x: x[0])
    #print(df)
    value1=['python']
    p1=df.loc[df['first_tag'].isin(value1)]
    print(df["first_tag"].value_counts())
    print("The minimum, maximum and mean value for viewpoint for tag-python")
    print(p1.viewcount.min())
    print(p1.viewcount.max())
    print(p1.viewcount.mean())
    value2=['pandas']
    p2=df.loc[df['first_tag'].isin(value2)]    
    print("The minimum, maximum and mean value for viewpoint for tag-pandas")
    print(p2.viewcount.min())
    print(p2.viewcount.max())
    print(p2.viewcount.mean())
    value3=['dataframe']
    p3=df.loc[df['first_tag'].isin(value3)]
    print("The minimum, maximum and mean value for viewpoint for tag-dataframe")
    print(p3.viewcount.min())
    print(p3.viewcount.max())
    print(p3.viewcount.mean())
    d=pd.crosstab(index=df.answercount, columns=df.first_tag)
    print(d)
    finalsclice=d.loc[[0,1,2],["python"]]
    print(finalsclice)
analyze_data("question.csv")

import array as arr
import string
def analyze_corpus(filepath):
    df=pd.read_csv(filepath)
    p=df.title.values
    df["title"]=df["title"].str.lower().apply(lambda x: x)
    df["val"]=df["title"].str.split().apply(lambda x:x)
    val1=df["val"].values
    #print(df.val)
    emptyuniqueval=[]
    token1=[]
    for c in range(0,1000):
        token1+=val1[c]
    print(token1)
    for a in df.val.values:
        emptyuniqueval+=a
    print(emptyuniqueval)
    for v in token1:
        if not v in emptyuniqueval:
            emptyuniqueval.append(v)
    print(emptyuniqueval)        
    #uniqe1=set(emptyuniqueval)
    #print(len(uniqe1))
    zeroarray=np.zeros((1000,1849),dtype=np.int)
    print(zeroarray)
    for z in range(0,len(val1)):
        for p in val1[z]:
            column=emptyuniqueval.index(p)
            zeroarray[z][column]+=1
            
    zeroarray
    tf_idf,top_k=analyze_tf_idf(zeroarray,5)
    topk=top_k[0:20,:]
    print(topk)
    
    
    
      
analyze_corpus('question.csv')    
    

