import re
import os
def opening(path):
    file = open(path,'r', encoding = 'utf-8') 
    f = file.read()
    file.close()
    return f

def search(f):
    res=re.findall('((?:[А-ЯЁ]\. [А-ЯЁ][^ .].+?)[ .,])', f)
    text=' \n'.join(res)
    return text

def printing(text):
    print(text)

def main():
    main = printing(search(opening('mih.html')))
main()

def search1(f):
    res=re.findall('([А-ЯЁ]\. [А-ЯЁ][^ .][а-яё]+?[ .,])', f)
    res1=re.findall('([А-ЯЁ]\.[А-ЯЁ]\. [А-ЯЁ][а-яё]+?[ .,])', f)
    res2=re.findall('([А-ЯЁ][а-яё]+? [А-ЯЁ][а-яё]+?[ .,])',f)
    res3=res+res1+res2
    text ='\n'.join(res3)
    return text

def search2(f):
    res=re.findall('([А-ЯЁ]\. [А-ЯЁ][^ .][а-яё]+?[ .,])', f)
    res1=re.findall('([А-ЯЁ]\.[А-ЯЁ]\. [А-ЯЁ][а-яё]+?[ .,])', f)
    res2=re.findall('([А-ЯЁ][а-яё]+? [А-ЯЁ][а-яё]+?[ .,])',f)
    res3=res+res1+res2
    return res

def writing (text):
    file = open('demo.tsv', 'w', encoding='utf-8')
    file.write(text)
    file.close
    
def main1():
    main1=printing(search1(opening('mih.html')))
main1()

def creation(massiv):
    for names in massiv:
        newname=names.split(' ')
        string = str(newname[1])
        try:
             os.makedirs(string)
        except OSError:
             pass
        file = open('mih.html','r', encoding = 'utf-8') 
        f = file.read()
        file.close()
        res = re.findall('([А-ЯЁ].+?[^А-ЯЁ]\.)', f)
        for sent in res:
            if string in sent:
                file=open('C:/Users/Tanya/Documents/Программирование/подготовка к контрольной' + os.sep + string + os.sep +'string.tsv', 'w', encoding='utf-8')
                file.write(str(sent))
                file.close()
            else:
                continue
def main2():
    main2= creation(search2(opening('mih.html')))
main2()



        
