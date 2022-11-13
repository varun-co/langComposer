# langComposer
for Other Languages change the language name 
``` 
python3 -m venv env
```
``` 
source env/bin/activate
```
``` 
pip install -r requirments.txt
```
``` 
mkdir <lang-name>
```

``` 
cd <lang-name>
```
Now we Need to Create letters.tsv file
```
touch letters.tsv
```
In this File the first row should contain all the vowels with the exception of the first element 
and the first column should contain all the columns with the exception of the first element
the first element needs to be an empty string 

and all the compund letters should be in their corresponding row and columns 
i.e  if a + b  = c where a is the vowel and b is the consonent and c is the compound letter
then c should be in the row where a is and in column where b is


Edit lettersDirectory to <lang-name>
and create a new file where you want to check for the conversion 
and save its path in sourcefile variable inside the code
