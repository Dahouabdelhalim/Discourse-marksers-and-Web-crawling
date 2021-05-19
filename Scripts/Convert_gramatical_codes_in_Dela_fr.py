#!/usr/bin/env python
# coding: utf-8

# ***Function to search for Gramatical codes***

# In[1]:


def contains_word(s, w):
    return ('' + w + '') in (' ' + s + ' ')


# ***Importing libraries***

# In[2]:


get_ipython().system('pip install termcolor')


# In[3]:


# Importing libraries
from io import open
import re
from termcolor import colored


# ***Reading Dela_fr file***

# In[6]:


# Reading Dela_fr file
filename = "Dela_fr.dic"
with open(filename, 'r', encoding='utf8') as f:
    text = f.readlines()


# ***Specify the format of gramatical codes***

# In[7]:


# Precise the motifs
motifs = [".A:",".A+",".ADV:",".ADV+",".V:",".V+",".DET:",".DET+",".PREP:",".PREP+",".PREPDET:",".PREPDET+",".PRO:",".PRO+"]
motif_1 = ".A:"
motif_2 = ".A+"


# ***Apply the loop to search and modify***

# In[8]:


# Search and modify
for i in range(len(text)):

    if contains_word (text[i],motif_1 ): # Test if the motif_1 exist

      print(colored('Before', 'red'),text[i])
      text[i] = re.sub(motif_1, ".In",text[i]) # make the modification by using the "inutile" word (in place of the motif)
      print(colored("After",'green'), text[i])

    elif contains_word (text[i],motif_2 ): # Test if the motif_2 exist

      print(colored('Before', 'red'),text[i])
      text[i] = re.sub(motif_2, ".In",text[i]) # make the modification by using the "inutile" word (in place of the motif)
      print(colored("After",'green'), text[i])


# ***Check the existence of the previous gramatical codes***

# In[52]:


# Reading Dela_fr file
filename = "Dela_fr_modify.dic"
with open(filename, 'w', encoding='utf8') as f:
    for line in text:
      f.write(line)
    f.close()

