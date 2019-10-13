
# coding: utf-8

# In[3]:


get_ipython().system('pip install mecab-python3')
get_ipython().system('pip install wordcloud')


# In[4]:


import MeCab
import csv
import pandas as pd
import collections
from wordcloud import WordCloud


# In[11]:


csv_path = input("CSVファイルのパスを入力してください：")
df = pd.read_csv(csv_path)
df = df["作品名"]
mecab= MeCab.Tagger("")


# In[6]:


s = []
for text in df:
  node = mecab.parseToNode(text)
  while node:
    if node.feature[:2] == '名詞':
      s.append(node.surface)
    node = node.next

word_count = collections.Counter(s)


# In[7]:


with open("WordCount.txt",mode = 'x') as f:
  for key in word_count:
    f.write(key + " : "+str(word_count[key])+" ")
f.close()


# In[8]:


N_word = ''
for string in s:
  N_word += string
  N_word += ' '


# In[12]:


font_path = input("フォントのパスを入力してください：")
wc = WordCloud(font_path,width=480,height=320,background_color="white",collocations=False)
wc.generate(N_word)
wc.to_file("wordcloud.png")

