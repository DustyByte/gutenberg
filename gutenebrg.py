import os
import requests
from google.colab import drive
from google.colab import files
import time


def find_author(text):
  key = 'Author: '
  flag = False
  author = ''
  running_word = '        '#8 spaces
  for char in text:
    running_word = running_word[1:]
    running_word += char
    if running_word==key:
      flag = True
    if flag==True:
      author += char
      if char=='\n':
        flag = False
        break
  author=author[1:-2]
  if len(author)>40:
    author = 'unknown'
  return author

def normalize(text):
  if text=='':
    text='unknown'
  return text.replace(' ', '_')

start=1#(set the value manually from where you want to start download)
end=70000#(set the value manually from where you want to end download)
dn=0#total successful downloads 
rj=0#total rejects
rejected=[]#rejected ones

while start<=end:
  url = "https://www.gutenberg.org/cache/epub/"+str(start)+"/pg"+str(start)+".txt"
  response = requests.get(url)
  text= response.content.decode('utf-8')
  author = normalize(find_author(text))
  directory_path = '/content/Books/'+author
  os.makedirs(directory_path, exist_ok=True)#replace with local folder builder code if running locally
  output_file = "/content/Books/"+author+"/"+str(start)+".txt"
  if response.status_code==200:
      with open(output_file, 'wb') as f:
          f.write(response.content)
      print("File "+str(start)+" downloaded successfully!")
      dn+=1
  else:
      print("Failed to download file "+str(start)+" Status code:", response.status_code)
      rj+=1
      rejected.append(start)
  start+=1