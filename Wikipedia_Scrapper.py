from bs4 import BeautifulSoup
import requests
import numpy
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import os.path


end=False
array=[]
df = pd.DataFrame(columns=['text'])
counter=0

url=('')


while end==False:
    url=input("Enter URL : ")
    page=requests.get(url)
    wiki_page=BeautifulSoup(page.text,"html.parser")    

    for paragraph in wiki_page.select("p"):
        sentences = sent_tokenize(paragraph.getText()) 
        for sentence in sentences:
            array.append(sentence) 
            df = df.append({'text': sentence}, ignore_index=True) 
            counter+=1
    
    end=input("Do you want to continue? y/n ")
    if end=="n":
        end=True
    elif end=="y":
        end=False

filename = "WikipediaFileSentences.csv"

# Check if the file already exists
if os.path.isfile(filename):
    # If the file exists, open it in append mode
    with open(filename, 'a', encoding='utf-8-sig', newline='') as file:
        # Append the data to the file
        df.to_csv(file, header=False, index=False)
else:
    # If the file does not exist, create a new file and write the data to it
    df.to_csv(filename, encoding='utf-8-sig', index=False)


#count = df['text'].str.count('\.').sum() 
print(f'The CSV file contains {counter} sentences.')