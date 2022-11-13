import os
import csv
import re 
from jiwer import cer


''' Enter The Directory in which your letters are made
if it does not exist mkdir <lang-name>
cd <lang-name>
touch letters.tsv
'''
lettersDirectory = 'tamil'
sourcefile = 'tamilFile.txt'



def generateMapAndReverseMap(letters,vowels,consonents):
    hashMap = dict()
    reverseHashMap = dict()
    for i in range(1,len((letters))):
        for j in range(1,len((letters[i]))):
            ele = letters[i][j].strip()
            hashMap[ele] = letters[i][0].strip()+ letters[0][j].strip()
            reverseHashMap[letters[i][0].strip() + letters[0][j].strip()] = ele 
    return  hashMap , reverseHashMap 
def init():
    with open(os.path.join(lettersDirectory,'letters.tsv'),encoding='utf-8') as fhandle:
       reader = csv.reader(fhandle,delimiter='\t') 
       letters = list((reader))
    # first row is the vowels 
    vowels = letters[0][1:]
    consonents = [letters[i][0] for i in range(1,len(letters))]
    consonentsWithoutDot = [i[0] for i in consonents]
    hashMap , reverseHashMap = generateMapAndReverseMap(letters,vowels,consonents)
    return vowels , consonentsWithoutDot , consonents , hashMap , reverseHashMap 
def decompose(lines):
    #keys = sorted(hashMap.keys(),reverse=True)
    lines = lines + ' '
    vowels, consonentsWithoutDot , consonents , hashMap , _ = init()
    res = ''
    i = 0
    while(i<len(lines)):
        if lines[i] in consonentsWithoutDot:
            if lines[i+1] == '்':
                res = res + lines[i] + lines[i+1]
                i = i + 1
            elif hashMap.get(lines[i]+lines[i+1],0) != 0:
                res = res + hashMap[lines[i]+lines[i+1]]
                i = i + 1
            else:
                res = res + hashMap[lines[i]]
        else:
            res = res + lines[i]
        i = i + 1
    return res[:-1]
def recompose(lines):
    vowels, consonentsWithoutDot, consonents, _ , reverseHashMap = init()
    res = ''
    i = 0
    for key , value in reverseHashMap.items():
        lines = re.sub(key,value,lines)
    return lines

    
def main():
   # main code 
    with open(sourcefile) as fhandle:
        lines = fhandle.read()
    temp = str(lines)
    lines = decompose(lines)
    #print(lines)
    lines = recompose(lines)
    error = cer(lines,temp)
    print(error)
if __name__ == '__main__':
    main()
